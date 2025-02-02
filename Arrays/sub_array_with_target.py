def subarraySumAndPrint(nums, target):
    count = 0

    # Outer loop: Start index of subarray
    for i in range(len(nums)):
        current_sum = 0

        # Inner loop: End index of subarray
        for j in range(i, len(nums)):
            current_sum += nums[j]  # Add current element to the subarray sum
            
            # Check if the current sum equals the target
            if current_sum == target:
                count += 1
                print(nums[i:j+1])  # Print subarray
    
    print(f"Total number of subarrays with sum {target}: {count}")
    return count

# Test Case
nums = [1, 2, 3, 3, 1, 1, 1]
target = 3
subarraySumAndPrint(nums, target)
