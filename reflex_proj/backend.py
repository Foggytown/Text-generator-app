import pandas as pd
from reflex_proj.funcs import tokenize, WordCompletor, NGramLanguageModel, TextSuggestion, test_all
            
class NGramGenerator():
    def __init__(self):
        pass

    def load(self, n=3, test=True):
        if test:
            dummy_corpus = [
            ['aa', 'aa', 'aa', 'aa', 'ab'],
            ['aaa', 'abab'],
            ['abb', 'aa', 'ab', 'bba', 'bbb', 'bcd']
            ]
		
            word_completor = WordCompletor(dummy_corpus)
            n_gram_model = NGramLanguageModel(corpus=dummy_corpus, n=2)
            self.text_suggestion = TextSuggestion(word_completor, n_gram_model)

        else:
            word_completor=WordCompletor.load("completer2.gzip")
            print("Backend: loaded word completor")
            n_gram_model=NGramLanguageModel.load("ngram_model.gzip")
            print("Backend: loaded language model, loading complete!")
            self.text_suggestion = TextSuggestion(word_completor, n_gram_model)
            
    def suggest(self, prompt, n_words, n_texts=1, greedy=True):
        return self.text_suggestion.suggest_text(tokenize(prompt.lower()), n_words=n_words, n_texts=n_texts, greedy=greedy)


if __name__=="__main__":
    test_all()
    generator=NGramGenerator()
    generator.load(test=True)

    print("generated:", generator.suggest("I really like", 3, 5, False))
    
    print("waiting for input:")
    while True:
        prompt=input()
        n=int(input())
        print(f"generating with prompt {prompt} and n_words {n}")
        print("generated:", generator.suggest(prompt, n, 5, False))

