from utils import clustering
from utils import nlp_model
import numpy as np
import pandas as pd

model = nlp_model.load_model('models', 'nlp_model')

# Threshold: .63
# words = ["apple", "pear", "banana", "skip", "cancel", "construction", "red"]
# assasin = "orange"

# words = ["pencil", "notebook", "paper", "tree", "grass", "sleep"]
# assasin = "apple"

# words = ["box", "model", "soldier", "leprechaun", "ship", "fire", "mole", "cast", "telescope"]
# assasin = "hood"

words = ["bar", "table", "cotton", "teacher", "racket", "park", "superhero"]
assasin = "hood"

clusters = clustering.agg_cluster(words, assasin , model)

allowed_words = []

dict = pd.read_csv("texts/dictionary.csv")
dict = dict['Word']

for word in dict:
    if isinstance(word, str):
        allowed_words.append(word.lower().strip())

# largest, size = clustering.largets_cluster(clusters)

for cluster in clusters:
    print(cluster.get_words())
    similars = model.wv.most_similar(positive = cluster.get_words(), negative = [assasin], topn = 50)
    for (key, val) in similars:
        if key in allowed_words:
            print(f'{key}: {val}')
            break


# similars = model.wv.most_similar(positive = ["casino", 'lock'], negative = ["mail"], topn = 50)

# for (key, val) in similars:
#     if key in allowed_words:
#         print(f'{key}: {val}')

