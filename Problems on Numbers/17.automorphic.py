def isautomorphic(n):
    sqr = n * n

    str_n = str(n)
    str_sqr = str(sqr)

    return str_sqr.endswith(str_n)
    
if __name__ == "__main__":
    n = int(input())

    if isautomorphic(n):
        print("Automorphic")
    else:
        print("Not Automorphic")