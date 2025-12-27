import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from typing import List
from collections import Counter

def tokenize(text):
    reg = re.compile(r'\w+')
    return reg.findall(text)


def remove_stopwords(tokenized_texts):
    clear_texts = []
    for words in tokenized_texts:
        clear_texts.append([word for word in words if word not in stop_words])

    return clear_texts


def lemmatize_text(tokenized_texts):
    lemmatized_data = []
    lemmatizer = WordNetLemmatizer()
    for words in tokenized_texts:
        lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
        lemmatized_data.append(lemmatized_words)
    return lemmatized_data


class PrefixTreeNode:
    def __init__(self):
        self.children: dict[str, PrefixTreeNode] = {}
        self.is_end_of_word = False

class PrefixTree:
    def __init__(self, vocabulary: List[str]) -> None:
        """
        vocabulary: список всех уникальных токенов в корпусе
        """
        self.root = PrefixTreeNode()
        
        for word in vocabulary:
            self._insert_word(word)

    def _insert_word(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = PrefixTreeNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix: str) -> List[str]:
        """
        Возвращает все слова, начинающиеся на prefix
        prefix: str – префикс слова
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        self._collect_words(node, prefix, results)
        return results

    def _collect_words(self, node: PrefixTreeNode, cur_prefix: str, results: List[str]) -> None:
        if node.is_end_of_word:
            results.append(cur_prefix)
        
        for char, child_node in node.children.items():
            self._collect_words(child_node, cur_prefix + char, results)


class WordCompletor:
    def __init__(self, corpus):
        """
        corpus: list – корпус текстов
        """

        self.counter = Counter()
        for message in corpus:
            self.counter.update(message)
        vocabulary = list(self.counter.keys())
        self.num_words=sum(self.counter.values())
        
        self.prefix_tree = PrefixTree(vocabulary)

    def get_words_and_probs(self, prefix: str) -> (List[str], List[float]):
        """
        Возвращает список слов, начинающихся на prefix,
        с их вероятностями (нормировать ничего не нужно)
        """
        words=self.prefix_tree.search_prefix(prefix)
        if len(words)==0:
            return [],[]
        probs=[0]*len(words)
        for i in range(len(words)):
            probs[i]=self.counter[words[i]]/self.num_words
        return words, probs


class NGramLanguageModel:
    def __init__(self, corpus, n):
        self.corpus=corpus
        self.n=n

    def get_next_words_and_probs(self, prefix: list) -> (List[str], List[float]):
        """
        Возвращает список слов, которые могут идти после prefix,
        а так же список вероятностей этих слов
        """
        counter=dict()
        if len(prefix)<self.n:
            raise ValueError("Not enough data to generate next word")
        if len(prefix)>self.n:
            prefix=prefix[-self.n:]
        for text in self.corpus:
            for i in range(len(text)-self.n):
                for j in range(i, i+self.n):
                    if text[j]!=prefix[j-i]:
                        break
                    if j==i+self.n-1:
                        counter[text[j+1]]=counter.get(text[j+1],0)+1

        sum_counts=sum(counter.values())
        next_words=list(counter.keys())
        probs=list(counter.values())
        for i in range(len(next_words)):
            probs[i]/=sum_counts

        return next_words, probs


class TextSuggestion:
    def __init__(self, word_completor, n_gram_model):
        self.word_completor = word_completor
        self.n_gram_model = n_gram_model

    def suggest_text(self, text: Union[str, list], n_words=3, n_texts=1) -> list[list[str]]:
        """
        Возвращает возможные варианты продолжения текста (по умолчанию только один)
        
        text: строка или список слов – написанный пользователем текст
        n_words: число слов, которые дописывает n-граммная модель
        n_texts: число возвращаемых продолжений (пока что только одно)
        
        return: list[list[srt]] – список из n_texts списков слов, по 1 + n_words слов в каждом
        Первое слово – это то, которое WordCompletor дополнил до целого.
        """

        words, probs=self.word_completor.get_words_and_probs(text[-1])
        best_end=""
        max_prob=-1
        for i in range(len(words)):
            if probs[i]>max_prob:
                max_prob=probs[i]
                best_end=words[i]
        text[-1]=best_end
        
        for i in range(n_words):
            next_words, probs=self.n_gram_model.get_next_words_and_probs(text)
            best_word=""
            max_prob=-1
            for i in range(len(next_words)):
                if probs[i]>max_prob:
                    max_prob=probs[i]
                    best_word=next_words[i]
            text.append(best_word)
                

        return text[-n_words-1:]


def test_all():
    vocabulary = ['aa', 'aaa', 'abb', 'bba', 'bbb', 'bcd']
    prefix_tree = PrefixTree(vocabulary)

    assert set(prefix_tree.search_prefix('a')) == set(['aa', 'aaa', 'abb'])
    assert set(prefix_tree.search_prefix('bb')) == set(['bba', 'bbb'])

    dummy_corpus = [
        ["aa", "ab"],
        ["aaa", "abab"],
        ["abb", "aa", "ab", "bba", "bbb", "bcd"],
    ]

    word_completor = WordCompletor(dummy_corpus)
    words, probs = word_completor.get_words_and_probs('a')
    words_probs = list(zip(words, probs))
    assert set(words_probs) == {('aa', 0.2), ('ab', 0.2), ('aaa', 0.1), ('abab', 0.1), ('abb', 0.1)}

    dummy_corpus = [
        ['aa', 'aa', 'aa', 'aa', 'ab'],
        ['aaa', 'abab'],
        ['abb', 'aa', 'ab', 'bba', 'bbb', 'bcd']
    ]

    n_gram_model = NGramLanguageModel(corpus=dummy_corpus, n=2)

    next_words, probs = n_gram_model.get_next_words_and_probs(['aa', 'aa'])
    words_probs = list(zip(next_words, probs))

    assert set(words_probs) == {('aa', 2/3), ('ab', 1/3)}
    dummy_corpus = [
    ['aa', 'aa', 'aa', 'aa', 'ab'],
    ['aaa', 'abab'],
    ['abb', 'aa', 'ab', 'bba', 'bbb', 'bcd']
    ]

    word_completor = WordCompletor(dummy_corpus)
    n_gram_model = NGramLanguageModel(corpus=dummy_corpus, n=2)
    text_suggestion = TextSuggestion(word_completor, n_gram_model)

    assert text_suggestion.suggest_text(['aa', 'aa'], n_words=3, n_texts=1) == [['aa', 'aa', 'aa', 'aa']]
    assert text_suggestion.suggest_text(['abb', 'aa', 'ab'], n_words=2, n_texts=1) == [['ab', 'bba', 'bbb']]
