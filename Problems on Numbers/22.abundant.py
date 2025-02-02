def isabundant(n):
    sum_of_div = 0

    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            if (i*i == n) or (i == 1):
                sum_of_div += i
            else:
                sum_of_div += i + n//i
    
    return n < sum_of_div
    

if __name__ == "__main__":
    n = int(input())

    if isabundant(n):
        print("Its abundant")
    else:
        print("Its not abundant")

