from typing import List, Tuple
from numpy import array
from joblib import Memory
import hdbscan
from sklearn.metrics import pairwise_distances

class Clustering:
    
    def cluster(self, vectors: List[array]) -> Tuple[array, array]:
        clusterer = hdbscan.HDBSCAN(algorithm='best', alpha=1.0, approx_min_span_tree=True,
        gen_min_span_tree=False, leaf_size=40, memory=Memory(cachedir=None),
        metric='braycurtis', min_cluster_size=2, min_samples=None, p=None)
        clusterer.fit(vectors)
        return (clusterer.labels_, clusterer.probabilities_)
    
    def distances_within_cluster(self, vectors: List[array]) -> array:
        """
        Returns
        -------
        D : array [n_samples_a, n_samples_a] or [n_samples_a, n_samples_b]
            A distance matrix D such that D_{i, j} is the distance between the
            ith and jth vectors of the given matrix X, if Y is None.
            If Y is not None, then D_{i, j} is the distance between the ith array
            from X and the jth array from Y.
        """
        return pairwise_distances(vectors, metric='cosine')
