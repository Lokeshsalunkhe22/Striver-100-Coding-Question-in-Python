def sum_AP(a,d,n):
    #return (n/2) * (2*a + (n-1)*d) directly using formula

    sum = 0
    for i in range(1, n+1):
        sum = sum + a
        a = a + d

    return sum

if __name__ == "__main__":
    a = int(input("1st Terms: "))
    d = int(input("Common Difference: "))
    n = int(input("Last Terms: "))

    print(sum_AP(a,d,n))