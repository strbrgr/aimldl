import numpy as np


class Perceptron:
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta  # LR,
        self.n_iter = n_iter  # Iterations over training data set
        self.random_state = random_state  # Random generator seed for init of weights

    # Fit our training data
    def fit(self, X, y):
        # X is our training vector of [n_examples, n_features]
        # y are our target values
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])  # weights
        self.b_ = np.float_(0.0)  # bias
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_ += update * xi
                self.b_ += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    # Calculate the net_input (z)
    def net_input(self, X):
        # Calculates the vector dot product
        return np.dot(X, self.w_) + self.b_

    # Return a class label after training step
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, 0)
