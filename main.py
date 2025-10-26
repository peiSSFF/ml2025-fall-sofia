def findNumber():
    N = int(input("Please enter a positive integer N: "))
    while N <= 0:
        print(f"Please enter a positive integer instead of {N}")
        N = int(input("Please enter a positive integer N: "))

    nums = []
    for i in range(N):
        num = nums.append(int(input("Please provide N numbers (one by one): ")))
        nums.append(num)

    X = int(input("Enter integer X to search for: "))
    if X in nums:
        idx = nums.index(X) + 1
        print(f"{X} is present at index {idx}")
    else:
        print("-1")


if __name__ == '__main__':
    findNumber()

