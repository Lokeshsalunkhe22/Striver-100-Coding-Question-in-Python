def repeating_element(arr):

    frequency = { }
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    for num, count in frequency.items():
        if count < 2:
            print(num, end=" ")

if __name__ == "__main__":
    elements = input()
    arr = list(map(int, elements.split()))

    repeating_element(arr)