import pandas as pd
from funcs import tokenize, remove_stopwords, lemmatize_text, WordCompletor, NGramLanguageModel, TextSuggestion, test_all 

class NGramGenerator():
    def __init__(self):
        pass
        #tokenized_messages=remove_stopwords(messages)
        #lemmatized_messages = lemmatize_text(tokenized_messages)

    def train(self, n=3):
        emails = pd.read_csv('../emails.csv')
        emails["message"]=emails["message"].apply(lambda x: x[x.find("\n", x.lower().find("x-filename")):].strip())
        self.tokenized_messages=[tokenize(t.lower()) for t in emails["message"]]
        word_completor = WordCompletor(self.tokenized_messages)
        n_gram_model = NGramLanguageModel(corpus=self.tokenized_messages, n=n)
        self.text_suggestion = TextSuggestion(word_completor, n_gram_model)

    def suggest(self, prompt, n_words, n_texts=1):
        return self.text_suggestion.suggest_text(tokenize(prompt.lower()), n_words=n_words, n_texts=n_texts)

'''
test_all()
generator=NGramGenerator()
generator.train()
print("waiting for input:")
while True:
    prompt=tokenize(input().lower())
    n=int(input())
    print(f"generating with prompt {prompt} and n_words {n}")
    print("generated:", generator.suggest(prompt, n))
'''
