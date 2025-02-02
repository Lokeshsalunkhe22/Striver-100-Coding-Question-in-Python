def sum_gp(a,r,n):

    sum = 0

    for i in range(1,n+1):
        sum = sum + a
        a = r*a

    return sum

if __name__ == "__main__":
    a = int(input("First Term: "))
    r = float(input("Common Ratio: "))
    n = int(input("Last Term: "))

    print(sum_gp(a,r,n))