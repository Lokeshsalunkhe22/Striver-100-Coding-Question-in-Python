def find_equilibrium_index(nums):
    total_sum = sum(nums)  # Total sum of the array
    left_sum = 0  # Start with no sum on the left side
    
    for i in range(len(nums)):
        total_sum -= nums[i]  # This is equivalent to calculating right_sum
        
        if left_sum == total_sum:  # Check if left and right sums are equal
            return i  # If they are equal, return the index
        
        left_sum += nums[i]  # Update left_sum for the next iteration
    
    return -1  # If no equilibrium index is found, return -1

if __name__ == "__main__":
    elements = input()
    arr = list(map(int, elements.split()))

    print(find_equilibrium_index(arr))