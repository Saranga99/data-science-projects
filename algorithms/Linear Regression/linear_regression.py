

class LinearRegression:
    # default learining rate is 0.001 (small value), no of iterations in gradient method
    def __init__(self, learnigRate=0.001, noIteratons=1000):
        self.learnigRate = learnigRate
        self.noIterations = noIteratons
        self.weights = None
        self.bias = None

    # fit method which takes training samples and labels
    def fit(self, X, y):
        pass

    # predict method which takes the testing samples

    def predict(self, X):
        pass
