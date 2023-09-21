import pickle as pkl
import utils.nlp_model as nlp_model
import pandas as pd


model = nlp_model.load_model("models", "nlp_model")
allowed_words = []

dict = pd.read_csv("texts/dictionary.csv")
dict = dict['Word']

for word in dict:
    if isinstance(word, str):
        allowed_words.append(word.lower().strip())

similars = model.wv.most_similar(positive = ["casino", 'lock'], negative = ["mail"], topn = 50)

for (key, val) in similars:
    if key in allowed_words:
        print(f'{key}: {val}')
    # print(f'{key}: {val}')
