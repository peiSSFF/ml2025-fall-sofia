import numpy as np
from sklearn.metrics import precision_score, recall_score

class XYPoints:
    def __init__(self, n):
        self.x = np.zeros(n, dtype=int)
        self.y = np.zeros(n, dtype=int)

    def insertPoints(self, n):
        for i in range(n):

            numX = int(input(f"Enter x for point {i}, must be either 0 or 1: "))
            while numX != 0 and numX != 1:
                print(f"Please enter 0 or 1 instead of {numX}")
                numX = int(input(f"Enter x for point {i}, must be either 0 or 1: "))

            numY = int(input(f"Enter y for point {i}, must be either 0 or 1: "))
            while numY != 0 and numY != 1:
                print(f"Please enter 0 or 1 instead of {numY}")
                numY = int(input(f"Enter y for point {i}, must be either 0 or 1: "))
            self.x[i] = numX
            self.y[i] = numY


def main():
    N = int(input("Please enter a positive integer N: "))
    while N <= 0:
        print(f"Please enter a positive integer instead of {N}")
        N = int(input("Please enter a positive integer N: "))

    processor = XYPoints(N)
    processor.insertPoints(N)

    precision = precision_score(processor.x, processor.y, zero_division=0)
    recall = recall_score(processor.x, processor.y, zero_division=0)

    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()

