from linear_regression import LinearRegression
from matplotlib import colors
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

# import random example data
X, y = datasets.make_regression(
    n_samples=100, n_features=1, noise=20, random_state=4)
# take testing and training samples
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234)

# plotting scatter plot
# fig = plt.figure(figsize=(8, 6))
# plt.scatter(X[:, 0], y, color="b", marker="o", s=30)
# plt.show()


# testing
# count = 0
# while count <= 1:
#     regressor = LinearRegression(learnig_rate=count)
#     regressor.fit(X_train, y_train)
#     Predicted = regressor.predict(X_test)
#     acc = np.sum(Predicted == y_test)
#     # mean square error

#     def mean_square_error(y_true, y_predicted):
#         return np.mean((y_true-y_predicted)**2)
#     mse = mean_square_error(y_test, Predicted)
#     print(mse)
#     count += 0.001


regressor = LinearRegression(learnig_rate=0.001)
regressor.fit(X_train, y_train)
Predicted = regressor.predict(X_test)
acc = np.sum(Predicted == y_test)
# mean square error


def mean_square_error(y_true, y_predicted):
    return np.mean((y_true-y_predicted)**2)


mse = mean_square_error(y_test, Predicted)
print(mse)

# plotting
y_predicred_line = regressor.predict(X)
cmap = plt.get_cmap("viridis")
fig = plt.figure(figsize=(8, 6))
m1 = plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)
plt.plot(X, y_predicred_line, color="black", linewidth=2, label="rediction")
plt.show()
