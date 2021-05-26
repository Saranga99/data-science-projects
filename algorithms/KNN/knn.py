import collections
import numpy as np
from collections import Counter

# globel function


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum(x1-x2)**2)


class KNN:
    # default value is 3 , number of neghibours
    def __init__(self, k=3):
        self.k = k

    # train method
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    # predict method
    def predict(self, X):
        prerdicted_labels = [self._predict(x) for x in X]
        return np.array(prerdicted_labels)

    # helper method for predict method
    def _predict(self, x):
        # calculate all distences
        distences = [euclidean_distance(x, x_train)
                     for x_train in self.X_train]

        # look nearest neghibours (samples,labels)
        k_indicies = np.argsort(distences)[:self.k]

        k_nearest_labels = [self.y_train[i] for i in k_indicies]

        # get the majority vote
        most_common = Counter(k_nearest_labels).most_common(1)
        # chose the most common class label
        return most_common[0][0]
