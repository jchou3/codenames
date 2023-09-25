import gensim
import math
import numpy as np


class cluster:

    def __init__(self, words: list, model):
        self.words = words
        self.model = model
        self.center = np.zeros(32)

        word_vectors = np.zeros(model.wv[self.words[0]].shape[0])
        for word in self.words:
            for k in range(32):
                word_vectors[k] += model.wv[word][k]

        for k in range(32):
            self.center[k] = word_vectors[k] / len(self.words)

    # Calculates distance value of cluster
    def get_val(self):
        pass

    # Calculates center of a given group
    # Returns vector coordinates
    def get_center(self):
        return self.center

    def get_words(self):
        return self.words
    
    def get_model(self):
        return self.model
    


# Agglomaritive hierarchical clustering
# Adjusted to avoid assasin
# Returns list of clusters

def agg_cluster(words: list, assasin: str, model, min_clusters = 1, max_clusters = None):

    assasin = cluster([assasin], model)
    clusters = []
    cluster_his = []

    #Fusion is determined by disimilarity between groups -- pick a height and cut it off
    for word in words:
        word_list = [word]
        clusters.append(cluster(word_list, model))

    cluster_his = agg_rec(clusters, assasin, min_clusters)
    
    history_dis = []
    for history in reversed(cluster_his):
        dissims = []
        for i in range(len(history)):
            for j in range(i+1, len(history)):
                dissims.append(model.wv.wmdistance(history[i].get_words(), history[j].get_words()))
                # print(f'Cluster A: {history[i].get_words()} Cluster B: {history[j].get_words()} Dissimilarity: {model.wv.wmdistance(history[i].get_words(), history[j].get_words())}')
        # if np.mean(dissims) > 0.78:
        #     return history
        if len(dissims) > 1:
            history_dis.append(np.mean(dissims))
    
    largest_jump = 0
    largest_index = 0
    for i in range(1, len(history_dis)):
        jump = history_dis[i] - history_dis[i - 1]
        if jump > largest_jump:
            largest_jump = largest_jump
            largest_index = i

    return cluster_his[largest_index]

# Returns history of clusters
def agg_rec(clusters, assasin, min):

    if len(clusters) <= min:
        hist = [clusters]
        return hist
    
    else:
        a, b = find_closest_two(clusters, assasin)
        c = clusters[a].get_words() + clusters[b].get_words()
        new_clus = cluster(c, clusters[a].get_model())
        new_clusters = [cl for i, cl in enumerate(clusters) if (i != a and i != b)]
        new_clusters.append(new_clus)
        cluster_his = agg_rec(new_clusters, assasin, min)
        cluster_his.append(clusters)
        return cluster_his

# Returns indices
def find_closest_two(clusters, assasin):

    n = len(clusters)
    closest = {0, 1}
    closest_dist = np.inf
    model = clusters[0].get_model()

    for i in range(n):
        for j in range(i + 1, n):
            dist = get_distance(clusters[i].get_center(), clusters[j].get_center())
            hyp_cluster = cluster(clusters[i].get_words() + clusters[j].get_words(), model)
            dist_to_assasin = get_distance(hyp_cluster.get_center(), assasin.get_center())

            if (dist/dist_to_assasin) < closest_dist:
                closest_dist = dist/dist_to_assasin
                closest = {i, j}

    closest = list(closest)
    return closest[0], closest[1]



# Returns distance between two clusters
# def get_distance(cluster_a: cluster, cluster_b: cluster):

#     a = cluster_a.get_center()
#     b = cluster_b.get_center()

#     temp = a - b
#     sum_sq = np.dot(temp.T, temp)

#     return np.sqrt(sum_sq)

# Distance between two points
def get_distance(a, b):

    temp = a - b
    sum_sq = np.dot(temp.T, temp)

    return np.sqrt(sum_sq)



def largets_cluster(clusters: list):
    largest = clusters[0]
    largest_size = 0

    for cluster in clusters:
        size = len(cluster.get_words())
        if size > largest_size:
            largest_size = size
            largest = cluster

    return largest, size
