import math
def isarmstrong(n):
    
    #k = len(str(n))   
    k = int (math.log10(n)+1)    #MORE EFFCIENT WITH 0(1) Time Complexity

    temp = n
    sum = 0

    while n>0:
        lastdigit = n % 10
        sum = sum + (lastdigit ** k)
        n = n // 10

    if (temp == sum):
        return True

if __name__ == "__main__":
    n = int(input(""))
    
    if (isarmstrong(n)):
        print("Yes")
    else:
        print("No")