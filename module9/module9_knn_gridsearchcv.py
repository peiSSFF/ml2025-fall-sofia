import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


class XYPoints:
    def __init__(self, n):
        self.x = np.zeros(n, dtype=float)
        self.y = np.zeros(n, dtype=int)

    def insertPoints(self, n):
        for i in range(n):
            numX = float(input(f"Enter x for point {i}: "))
            numY = int(input(f"Enter y for point {i}: "))
            self.x[i] = numX
            self.y[i] = numY


def main():
    N = int(input("Please enter a positive integer N (size of training set): "))
    while N <= 0:
        print(f"Please enter a positive integer instead of {N}")
        N = int(input("Please enter a positive integer N: "))
    trainData = XYPoints(N)
    trainData.insertPoints(N)


    M = int(input("Please enter a positive integer M (size of test set): "))
    while M <= 0 or M > N :
        print(f"Please enter a positive integer instead of {M}. should be a positive integer and less than {N}")
        M = int(input("Please enter a positive integer M: "))
    testData = XYPoints(M)
    testData.insertPoints(M)

    xTrain = trainData.x.reshape(-1, 1)
    yTrain = trainData.y

    xTest = testData.x.reshape(-1, 1)
    yTest = testData.y

    bestK = None
    bestAccuracy = -1

    for k in range(1, min(N+1, 11)):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(xTrain, yTrain)

        yPred = model.predict(xTest)
        acc = accuracy_score(yTest, yPred)
        print(f"k = {k}, Test Accuracy = {acc:.4f}")
        if acc > bestAccuracy:
            bestAccuracy = acc
            bestK = k

    print(f"Best k: {bestK}")
    print(f"Best Test Accuracy: {bestAccuracy:.2f}")

if __name__ == "__main__":
    main()



