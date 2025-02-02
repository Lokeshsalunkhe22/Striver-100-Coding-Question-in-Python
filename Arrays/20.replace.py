def replace_with_rank(arr):
    n = len(arr)
    brr = arr.copy()
    
    # Sort the array
    brr.sort()

    # Create a map to store rank of each element
    rank_map = {}
    temp = 1
    
    # Assign rank to each element
    for element in brr:
        if element not in rank_map:
            rank_map[element] = temp
            temp += 1
    
    # Replace original elements with their rank

    #result = [rank_map[element] for element in arr]  #if want to store in list

    for element in arr:
        print(rank_map[element], end = " " )

if __name__ == "__main__":
    elements = input()
    arr = list(map(int, elements.split()))

    replace_with_rank(arr)