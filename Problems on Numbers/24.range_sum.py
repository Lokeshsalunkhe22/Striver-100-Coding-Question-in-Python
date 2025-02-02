def sum_of_range(l,r):

    sum = 0

    for i in range (l, r+1):
        sum = sum + i

    return sum

if __name__ == "__main__":
    first = int(input("Starting No.: "))
    second = int(input("Ending No.: ")) 

    print("sum of digit from",first, "to", second, "is", sum_of_range(first, second))