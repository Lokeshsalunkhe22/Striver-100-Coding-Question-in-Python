def factors(n):

    fact_list = []

    for i in range (1, int(n**0.5) + 1):
        if (n % i == 0):
            if (i * i == n):
                fact_list.append(i)
            else:
                fact_list.append(i)
                fact_list.append(n // i)

    return sorted(fact_list)
                
if __name__ == "__main__":
    n = int(input())

    #print(factors(n))  #it will print as a list [1,2,3,6]

    for fact in factors(n): #it will print as a 1, 2, 3, 6
        print(fact, end = " ")