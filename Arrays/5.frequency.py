def frequency(arr):

    frequency = {}

    for nums in arr:
        if nums in frequency:
            frequency[nums] += 1
        else:
            frequency[nums] = 1

    for key, val in frequency.items():
        print(f"{key}{val}")

if __name__ == "__main__":
    elements = input()
    arr = list(map(int, elements.split()))

    frequency(arr)