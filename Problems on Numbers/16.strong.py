def factorial(f):
    prod = 1

    for i in range(1,f+1):
        prod = prod * i
    
    return prod

def strong(n):
    temp = n
    sum = 0
    while n > 0:
        ld = n % 10
        sum =  sum + factorial(ld)
        n = n //10
        
    if sum == temp:
        return True   
     
if __name__ == "__main__":
    n = int(input())
    
    if (strong(n)):
        print("Yes")
    else:
        print("No")
        