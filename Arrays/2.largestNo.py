def largest_element(arr):
    maximum = arr[0]

    for elements in arr:
        if maximum < elements:
            maximum = elements

    return maximum

if __name__ == "__main__":
    elements = input()

    arr = list(map(int,elements.split()))

    print(largest_element(arr))