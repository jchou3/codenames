import gensim
import math


class cluster:

    def __init__(self, words: list):
        self.words = words

    # Calculates distance between 2 vector coordinates
    def get_distance(self):
        pass

    # Calculates center of a given group
    # Returns vector coordinates
    def get_center(self):
        pass

    # Returns vector of given word
    def get_vector(self):
        pass

    def get_words(self):
        return self.words


# Agglomaritive hierarchical clustering
# Adjusted to avoid assasin
# Returns list of clusters

def agg_cluster(words: cluster, assasin: str, min_clusters = None, max_clusters = None):
    pass