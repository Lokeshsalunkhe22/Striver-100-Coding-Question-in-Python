def rmv_duplicates(arr):
    j = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    return j+1

if __name__ == "__main__":
    elements = input()
    arr = list(map(int, elements.split()))
    
    k = rmv_duplicates(arr)
    print(arr[:k])