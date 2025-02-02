def issubset(arr1, arr2):
    set_arr1 = set(arr1)
    set_arr2 = set(arr2)

    if set_arr1.issubset(set_arr2):
        print("arr1[] is a subset of arr2[]")
    else:
        print("arr1[] is not a subset of arr2[]")

if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    issubset(arr1, arr2)