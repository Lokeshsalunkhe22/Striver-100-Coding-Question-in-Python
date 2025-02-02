def greatest(a, b, c):
    if a>=b and a>=c:
        print(a)
    elif b>=a and b>=c:
        print(b)
    else:
        print(c)

    """n = max(a, b, c)  #using max() function

    return n"""

if __name__ == "__main__":
    a = int(input("1st No.: "))
    b = int(input("2nd No.: "))
    c = int(input("3rd No.: "))

    greatest(a,b,c)

    #print(greatest(a,b,c))