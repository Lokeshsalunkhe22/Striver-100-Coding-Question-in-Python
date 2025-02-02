def reverse_array(arr):
    
    """arr.reverse()
    return arr"""

    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr

if __name__ == "__main__":
    user_input = input()
    arr = list(map(int, user_input.split()))

    print(reverse_array(arr))