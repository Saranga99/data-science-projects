import numpy as np

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
        # look nearest neghibours (samples,labels)
        # get the majority vote
        # chose the most common class label
