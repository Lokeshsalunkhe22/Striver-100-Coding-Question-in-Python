def rearrange(arr):
    arr.sort()

    mid = len(arr) // 2
    first_half = arr[:mid] #ascending i.e. increasing
    second_half = arr[mid:] #descending i.e. decreasing

    second_half.reverse()

    return first_half + second_half

if __name__ == "__main__":
    element = input()
    arr = list(map(int, element.split()))

    """for num in rearrange(arr):
        print(num, end=" ")"""

    print(*rearrange(arr))