def search_element(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1  
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print (search_element(arr, k))