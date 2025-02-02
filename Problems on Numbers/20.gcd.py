def gcd(a,b):
    
    while (a>0 and b>0):
        if (a>b):
            a = a % b
        else:
            b = b % a
    
    if (a == 0):
        return b
    else:
        return a
            
if __name__ == "__main__":
    n1 = int(input("N1: "))
    n2 = int(input("N2: "))

    print(gcd(n1,n2))