def minmax(n):

    digits = [int(d) for d in str(n)]

    print("Max: ", max(digits))
    print("Min: ", min(digits))

if __name__ == "__main__":
    n = int(input())

    minmax(n)