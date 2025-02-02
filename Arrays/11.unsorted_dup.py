def rmv_dup(arr):
    unique = []

    for num in arr:
        if num not in unique:
            unique.append(num)
            
    return unique

if __name__ == "__main__":
    elements = input()
    arr = list(map(int, elements.split()))
    print(*rmv_dup(arr))



 



