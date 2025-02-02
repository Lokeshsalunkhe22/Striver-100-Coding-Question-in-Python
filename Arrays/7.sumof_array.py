def sum_of_array(arr):
    sum = 0

    for num in arr:
        sum = sum + num

    return sum

if __name__ == "__main__":
    element = input()
    arr = list(map(int, element.split()))

    print(sum_of_array(arr))