def leap_yr(n):

    if ((n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)):
        print ("Yes")
    else:
        print ("No")
    

if __name__ == "__main__":
    n = int(input())

    leap_yr(n)