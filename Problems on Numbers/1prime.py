# Function to check if a number is prime
def checkPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

"""
if __name__ == "__main__":
    n = 17
    if checkPrime(n):
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")
"""
        
if __name__ == "__main__":
    first = int(input())
    second = int(input())
    
    for i in range(first, second+1):
        if checkPrime(i):
            print(i, end = " ")
