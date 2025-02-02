def sumofdigit(n):
    
    sum = 0

    for i in range(1,n+1):
        sum = sum + i

    print (sum)

if __name__ == "__main__":
    a = int(input())
    sumofdigit(a)