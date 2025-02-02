def median(arr):
    arr.sort()
    n = len(arr)

    if n % 2 != 0:
        return arr[n // 2]
    else:
        mid1, mid2 = arr[n//2], arr[(n//2)-1]
        return (mid1 + mid2) / 2
    
if __name__ == "__main__":
    elements = input()
    arr = list(map(int, elements.split()))

    print(median(arr))

    