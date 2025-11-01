from module5_mod import FindNumber

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

