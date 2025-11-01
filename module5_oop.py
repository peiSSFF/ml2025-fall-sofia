class FindNumber:
    def __init__(self):
        self.nums = []

    def readNumbers(self, n):
        for i in range(n):
            num = int(input("Please provide N numbers (one by one): "))
            self.nums.append(num)

    def searchNumber(self, n):
        for idx, num in enumerate(self.nums, start=1):
            if num == n:
                return idx
        return -1

def main():
    N = int(input("Please enter a positive integer N: "))
    while N <= 0:
        print(f"Please enter a positive integer instead of {N}")
        N = int(input("Please enter a positive integer N: "))

    processor = FindNumber()
    processor.readNumbers(N)

    x = int(input("Enter integer X to search for: "))
    idx = processor.searchNumber(x)
    print(idx)

if __name__ == "__main__":
    main()

