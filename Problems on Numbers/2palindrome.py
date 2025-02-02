def ispalindrome(n):
    temp = n
    rev = 0

    while n>0:
        rev = (rev*10) + (n%10)
        n = n//10
    if (temp == rev):
        return True
    else:
        return False

if __name__ == "__main__":
    a = int (input("Enter a starting Number:"))
    b = int(input("Enter ending Number:"))

    for i in range(a,b+1):
        if (ispalindrome(i)):
            print(i, end = " ")
