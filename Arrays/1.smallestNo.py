def smallest_element(arr):
    minimum = arr[0]

    for elements in arr:
        if minimum > elements:
            minimum = elements

    return minimum

if __name__ == "__main__":
    elements = input()

    # CASE 1: [1,2,3,4,5]
    arr = list(map(int,elements.strip("[]").split(",")))

    # CASE 2: 1,2,3,4,5
    arr = list(map(int,elements.split(",")))

    # CASE 3: 1 2 3 4 5
    arr = list(map(int,elements.split()))

    print(smallest_element(arr))
    