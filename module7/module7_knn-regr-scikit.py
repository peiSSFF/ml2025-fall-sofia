import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class XYPoints:
    def __init__(self):
        self.x = np.array([], dtype=float)
        self.y = np.array([], dtype=float)

    def insertPoints(self, n):
        for i in range(n):
            numX = float(input("Enter x for point {i} : "))
            numY = float(input("Enter y for point {i} : "))
            self.x = np.append(self.x, numX)
            self.y = np.append(self.y, numY)

    def labels_variance(self):
        if self.y.size == 0:
            raise ValueError("No training data to compute variance.")
        return np.var(self.y)

    def predictKNN(self, k, x):
        if self.x.size == 0:
            raise ValueError("No training data.")

        X_train = self.x.reshape(-1, 1)
        y_train = self.y

        # Create and train k-NN Regressor
        model = KNeighborsRegressor(n_neighbors=k)
        model.fit(X_train, y_train)

        # Predict for the given query x
        X_test = np.array([[float(x)]], dtype=float)
        y_pred = model.predict(X_test)[0]
        return y_pred


def main():
    N = int(input("Please enter a positive integer N: "))
    while N <= 0:
        print(f"Please enter a positive integer instead of {N}")
        N = int(input("Please enter a positive integer N: "))

    k = int(input("Please enter a positive integer k: "))
    while k <= 0:
        print(f"Please enter a positive integer instead of {k}")
        N = int(input("Please enter a positive integer k: "))

    processor = XYPoints()
    processor.insertPoints(N)

    labels_var = processor.labels_variance()

    x = int(input("Enter integer X for output: "))
    if k > N:
        print(f"k {k} is less than N {N}")
        return

    output = processor.predictKNN(k, x)
    print("Output is: ", output)
    print(f"Variance of labels in the training dataset: : {labels_var:.4f}")

if __name__ == "__main__":
    main()

