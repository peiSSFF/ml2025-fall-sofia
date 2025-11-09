import numpy as np

class XYPoints:
    def __init__(self):
        self.x = np.array([], dtype=float)
        self.y = np.array([], dtype=float)

    def insertPoints(self, n):
        for i in range(n):
            numX = int(input("Enter x for point {i} : "))
            numY = int(input("Enter y for point {i} : "))
            self.x = np.append(self.x, numX)
            self.y = np.append(self.y, numY)

    def predictKNN(self, k, x):
        if self.x.size == 0:
            raise ValueError("No training data.")

        # Compute distances
        distances = np.abs(self.x - float(x))

        # Get indices of k smallest distances
        nearest_indices = np.argsort(distances)[:k]

        # Average their y values
        y_pred = np.mean(self.y[nearest_indices])
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

    x = int(input("Enter integer X for output: "))
    if k > N:
        print(f"k {k} is less than N {N}")
        return

    output = processor.predictKNN(k, x)
    print("Output is: ", output)

if __name__ == "__main__":
    main()

