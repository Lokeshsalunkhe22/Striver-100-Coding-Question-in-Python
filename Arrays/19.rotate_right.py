def rotate_array(arr, k, direction):
    N = len(arr)
    k %= N  # Handle cases where k > N (rotation repeats every N)
    
    # Convert direction to lowercase to handle case insensitivity
    direction = direction.lower()

    if direction == "right":
        arr = arr[-k:] + arr[:-k]

    elif direction == "left":
        arr = arr[k:] + arr[:k]
    else:
        raise ValueError("Invalid direction! Use 'left' or 'right'.")
    
    return arr

if __name__ == "__main__":
    elements = input()
    arr = list(map(int, elements.split()))
    k = int(input())
    direction = input()
    
    print(*rotate_array(arr, k, direction))
