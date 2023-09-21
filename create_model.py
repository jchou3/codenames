#Needs a lot more training
#Filter out more names if possible
#Add dictionary to training


import pandas as pd
import utils.preprocess as preprocess
import utils.nlp_model as nlp_model
from nltk.corpus import brown
from pydictionary import Dictionary
from nltk.tokenize import word_tokenize

textpath = "texts"
textnames = ['AliceInWonderland.txt', 'book4.txt', 'TheStranger.txt']
stop = preprocess.get_stopwords()


dict_corpus = []
dict_words = []

dict = pd.read_csv(f'{textpath}/dictionary.csv')
dict = dict[['Word', 'Definition']]

for row in dict.itertuples(index = False):
    if (isinstance(getattr(row, 'Word'), str)) and (isinstance(getattr(row, 'Definition'), str)):
        dict_temp = getattr(row, 'Word') + getattr(row, 'Definition')
        dict_temp = preprocess.preprocess(dict_temp)
        dict_temp = preprocess.remove_words(dict_temp, stop)
        dict_temp = preprocess.remove_words(dict_temp, ["."])
        dict_corpus.append([i for i in word_tokenize(dict_temp)])




names = set()
with open('texts/names.txt') as f:
    lines = f.readlines()
    for line in lines:
        names.add(line.lower().strip())
    

news = pd.read_csv(f'{textpath}/bbc-news-data.csv', sep="\t")
news = news['content']

news_text = " ".join(news)
books = []

# brown_corpus = brown.sents().lower()

for name in textnames:
    with open(f'{textpath}/{name}', encoding='utf-8') as f:
        books.append(f.read())

book_texts = " ".join(books)
texts = " ".join([news_text, book_texts])


text = preprocess.preprocess(texts)
text = preprocess.remove_words(text, stop)
text = preprocess.remove_words(text, names)

corpus = preprocess.create_corpus(text)
# corpus.extend(brown_corpus)
corpus.extend(dict_corpus)

print("Creating model")

model = nlp_model.create_model(corpus)

nlp_model.save_model(model, "models", "nlp_model")



