def sum_of_digits(n):
    sum = 0 

    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n//10
    
    return sum

if __name__ == "__main__":
    n =  int(input())

    print("Sum:",sum_of_digits(n))