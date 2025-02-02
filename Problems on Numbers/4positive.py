def ispositive(n):
    if (n>0):
        return True

if __name__ == "__main__":
    a = int(input())

    if (ispositive(a)):
        print("Positive")
    else:
        print("Negative")