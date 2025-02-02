def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def permutation(n ,r):
    num = factorial(n)
    den = factorial(n-r)

    return num // den

if __name__ == "__main__":
    n = int(input("Enter value of N: "))
    r = int(input("Enter value of R: "))

    print(permutation(n, r))