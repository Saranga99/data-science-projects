import numpy as np


class LinearRegression:
    # default learining rate is 0.001 (small value), no of iterations in gradient method
    def __init__(self, learnig_rate=0.001, number_iterations=1000):
        self.learnig_rate = learnig_rate
        self.number_iterations = number_iterations
        self.weights = None
        self.bias = None

    # fit method which takes training samples and labels
    def fit(self, X, y):
        # implement gradient decent method
        number_samples, number_features = X.shape
        # initilize all the weights with zero
        # each component we put zero
        self.weights = np.zeros(number_features)
        self.bias = 0

        # gradient decent
        for _ in range(self.number_iterations):
            # approximation
            y_predicted = np.dot(X, self.weights)+self.bias

            dw = (1/number_samples)*np.dot(X.T, (y_predicted-y))
            db = (1/number_samples)*np.sum(y_predicted-y)

            # update weight
            self.weights = self.weights-self.learnig_rate*dw
            # update bias
            self.bias = self.bias-self.learnig_rate*db

    # predict method which takes the testing samples
    def predict(self, X):
        y_predicted = np.dot(X, self.weights)+self.bias
        return y_predicted
