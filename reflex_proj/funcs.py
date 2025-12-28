import numpy as np
import re
from typing import List
from collections import Counter, defaultdict
import pickle
import gzip
from nltk.stem import WordNetLemmatizer

def tokenize(text):
    reg = re.compile(r'\w+')
    return reg.findall(text)    

class WordCompletor:
    def __init__(self, corpus, min_freq=1):
        self.counter = Counter()
        for message in corpus:
            self.counter.update(word.lower() for word in message)
       
        if min_freq > 1:
            self.counter = Counter({
                word: count for word, count in self.counter.items() 
                if count >= min_freq
            })
        
        self.num_words = sum(self.counter.values())
        self.cache = {}
        
        self.words_by_prefix = defaultdict(list)
        for word in vocabulary:
            for i in range(1, len(word) + 1):
                self.words_by_prefix[word[:i]].append(word)
                
        for prefix in self.words_by_prefix:
            self.words_by_prefix[prefix].sort(
                key=lambda w: self.counter[w], 
                reverse=True
            )
    
    def get_words_and_probs(self, prefix: str) -> Tuple[List[str], List[float]]:
        prefix = prefix.lower()
        
        if prefix in self.cache:
            return self.cache[prefix]
        
        words = self.words_by_prefix.get(prefix, [])
        if not words:
            self.cache[prefix] = ([], [])
            return [], []
        
        probs = [self.counter[word] / self.num_words for word in words]
        self.cache[prefix] = (words, probs)
        return words, probs

    @classmethod
    def load(cls, filename: str):
        with gzip.open(filename, 'rb') as f:
            data = pickle.load(f)

        obj = cls.__new__(cls)
        obj.words_by_prefix = defaultdict(list, data['words_by_prefix'])
        obj.counter=data['counter']
        obj.num_words=data['num_words']
        
        obj.cache = {}
        
        return obj


class NGramLanguageModel:
    def __init__(self, corpus: List[List[str]], n: int):
        self.n = n
        self.ngram_counts = defaultdict(Counter)
        self._build_model(corpus)
        self.cache = {}
    
    def _build_model(self, corpus: List[List[str]]) -> None:
        for text in corpus:
            padded_text = ['<BOS>'] * (self.n) + text + ['<EOS>']
            
            for i in range(len(padded_text) - self.n-1):
                context = tuple(padded_text[i:i + self.n])
                next_word = padded_text[i + self.n]
                
                self.ngram_counts[context][next_word] += 1

                
    def _normalize_prefix(self, prefix: List[str]) -> tuple:
        if len(prefix) < self.n:
            normalized = ['<BOS>'] * (self.n  - len(prefix)) + prefix
        elif len(prefix) > self.n:
            normalized = prefix[-(self.n):]
        else:
            normalized = prefix
      
        return tuple(normalized)

    def get_next_words_and_probs(self, prefix: list) -> (List[str], List[float]):
        prefix_key = tuple(prefix)
        if prefix_key in self.cache:
            return self.cache[prefix_key]
        
        context = self._normalize_prefix(prefix)
        next_word_counter = self.ngram_counts.get(context, Counter())
        
        if not next_word_counter:
            self.cache[prefix_key] = ([], [])
            return [], []

        total = sum(next_word_counter.values())

        next_words=[]
        probs=[]
        
        for word, count in next_word_counter.items():
            next_words.append(word)
            probs.append(count / total)
        
        self.cache[prefix_key] = (next_words, probs)
        return next_words, probs

    @classmethod
    def load(cls, filename: str):
        with gzip.open(filename, 'rb') as f:
            data = pickle.load(f)

        obj = cls.__new__(cls)
        obj.n = data['n']
        obj.ngram_counts = defaultdict(Counter)
        for context, counter_dict in data['ngram_counts'].items():
            obj.ngram_counts[context] = Counter(counter_dict)
        
        obj.cache = {}
        
        return obj


class TextSuggestion:
    def __init__(self, word_completor, n_gram_model):
        self.word_completor = word_completor
        self.n_gram_model = n_gram_model

    def suggest_text(self, text: Union[str, list], n_words=3, n_texts=1, greedy=True) -> list[list[str]]:
        if isinstance(text, str):
            text = [w.strip() for w in text.split() if w.strip()]

        if not text:
            text = ["<BOS>"]
            
        if greedy:
            eos=False
            words, probs=self.word_completor.get_words_and_probs(text[-1])
            if words == []:
                text[-1]="<EOS>"
                eos=True
            else:
                text[-1]=words[np.argmax(probs)]
            
            for i in range(n_words):
                next_words, probs=self.n_gram_model.get_next_words_and_probs(text)
                if next_words == []:
                    if eos:
                        text.append("<PAD>")
                    else:
                        text.append("<EOS>")
                        eos=True
                    continue
                text.append(next_words[np.argmax(probs)])
                if text[-1]=="<EOS>":
                        eos=True
            return [text[-n_words-1:]]
            
        else:
            n=self.n_gram_model.n
            res=[]
            
            eos=[False]*n_texts
            for i in range(n_texts):
                res.append([])
                res[i]=text[-n:-1]
                
            words, probs=self.word_completor.get_words_and_probs(text[-1])
            if words == []:
                for i in range(n_texts):
                    res[i].append("<EOS>")
                    eos[i]=True
            else:
                n_texts=min(n_texts, len(words))
                res=res[:n_texts]
                sum_probs=sum(probs)
                words=np.random.choice(words, size=n_texts, p=np.array(probs)/sum_probs, replace=False)
                for i in range(n_texts):
                    res[i].append(str(words[i]))
                    
            for i in range(n_texts):
                for j in range(n_words):
                    next_words, probs=self.n_gram_model.get_next_words_and_probs(res[i])
                    if next_words == []:
                        if eos[i]:
                            res[i].append("<PAD>")
                        else:
                            res[i].append("<EOS>")
                            eos[i]=True
                        continue
                    next_word=str(np.random.choice(next_words, p=probs, replace=False))
                    res[i].append(next_word)
                    if res[i][-1]=="<EOS>":
                        eos[i]=True
                    
                res[i]=res[i][-n_words-1:]
            return res


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

    word_completor = WordCompletor(dummy_corpus, min_freq=1)
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

    word_completor = WordCompletor(dummy_corpus, min_freq=1)
    n_gram_model = NGramLanguageModel(corpus=dummy_corpus, n=2)
    text_suggestion = TextSuggestion(word_completor, n_gram_model)

    assert text_suggestion.suggest_text(['aa', 'aa'], n_words=3, n_texts=1) == [['aa', 'aa', 'aa', 'aa']]
    assert text_suggestion.suggest_text(['abb', 'aa', 'ab'], n_words=2, n_texts=1) == [['ab', 'bba', 'bbb']]
