from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import re


def get_stopwords():
    stop = set(stopwords.words("english"))
    return stop

def preprocess(text):
    text_input = re.sub('[^a-zA-Z0-9\.]+', ' ', str(text))
    output = re.sub(r'\d+', '', text_input)
    output = re.sub('[\.]+', ' . ', output)
    return output.lower().strip()

def remove_words(text, filter):
    filtered_words = [word.lower() for word in text.split() if word.lower() not in filter]
    return " ".join(filtered_words)


def create_corpus(text):
    corpus = []

    for i in sent_tokenize(text):
        temp = []

        for j in word_tokenize(i):
            if j != '.':
                temp.append(j)

        corpus.append(temp)

    return corpus

