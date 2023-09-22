import gensim
import math


class cluster:

    def __init__(self, words: list, model):
        self.words = words
        self.model = model

    # Calculates distance value of cluster
    def get_val(self):
        pass

    # Calculates center of a given group
    # Returns vector coordinates
    def get_center(self):
        pass

    def get_words(self):
        return self.words


# Agglomaritive hierarchical clustering
# Adjusted to avoid assasin
# Returns list of clusters

def agg_cluster(words: list, assasin: str, model, min_clusters = None, max_clusters = None):

    assasin_vec = model.wv[assasin]
    clusters = []


    #Fusion is determined by disimilarity between groups -- pick a height and cut it off
    for word in words:
        clusters.append(cluster(words, model))


def find_closest(clusters: list):
    pass

    

# Returns vector of given word
def get_vector(word, model):
    pass

# Returns distance between two points
def get_distance(a, b, model):
    pass

