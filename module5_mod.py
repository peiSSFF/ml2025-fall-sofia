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
