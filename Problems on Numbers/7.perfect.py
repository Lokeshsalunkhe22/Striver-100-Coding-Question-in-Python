def isperfect_num(n):
    sum_of_div = 0

    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            if i*i == n or i == 1:
                sum_of_div += i
            else:
                sum_of_div += i + n//i
 
    return sum_of_div == n

if __name__ == "__main__":
    a = int(input())

    if (isperfect_num(a)):
        print("Perfect Number")
    else:
        print("Not Perfect Number")