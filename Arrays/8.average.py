def avg_of_array(arr):
    sum = 0

    for num in arr:
        sum = sum + num

    avg = round((sum / len(arr)), 2)

    return avg
if __name__ == "__main__":
    element = input()
    arr = list(map(int, element.split()))

    print(avg_of_array(arr))