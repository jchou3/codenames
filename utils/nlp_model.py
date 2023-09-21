import gensim
import pickle as pkl


def create_model(corpus, vector_size = 100, window = 5):
    model = gensim.models.Word2Vec(corpus, min_count = 1, 
                                   vector_size = vector_size, window = window)
    return model

def save_model(model, filepath, filename):
    pkl.dump(model, open(f'{filepath}/{filename}.pkl', 'wb'))

def load_model(filepath, filename):
    pickled_model = pkl.load(open(f'{filepath}/{filename}.pkl', 'rb'))
    return pickled_model
