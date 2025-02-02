def harshad(n):
    
    temp = n
    sum = 0

    while n > 0:
        sum = sum + (n % 10)
        n = n // 10
    
    if (temp % sum == 0):
        return True

if __name__ == "__main__":
    n = int(input())

    if (harshad(n)):
        print("Its Harshad Number.")
    else:
        print("Its not Harshad Number.")