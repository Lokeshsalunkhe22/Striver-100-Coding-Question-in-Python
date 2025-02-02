def second_smallest_largest(arr):
    elements = sorted(set(arr))

    if len(elements) < 2:
        return -1, -1

    sec_largest = elements[-2]
    sec_smallest = elements[1]

    return sec_smallest, sec_largest

if __name__ == "__main__":
    element = input()
    arr = list(map(int,element.split()))

    sec_smallest, sec_largest = second_smallest_largest(arr)

    print(f"Second Smallest: {sec_smallest}")
    print(f"Second largest: {sec_largest}")