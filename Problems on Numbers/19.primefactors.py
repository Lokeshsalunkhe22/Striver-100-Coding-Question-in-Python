def prime_factors(n):
    for i in range(2, n + 1):
        if n % i == 0:
            print(i, end=" ")

        while n % i == 0:
            
            n //= i

if __name__ == "__main__":
    n = int(input())

    prime_factors(n)
