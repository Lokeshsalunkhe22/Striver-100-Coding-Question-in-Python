from collections import *
def sort_by_freq(nums):
    #frequency = { }
    
    frequency = defaultdict(int)
    for num in nums:
        frequency[num] += 1

    """for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1"""

    ans = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    result = []
    for value, count in ans:
        result.extend([value] * count)

    return result

    """for num in ans:
        first, second = num
        for i in range(second):
            print(first, end = " ")"""

if __name__ == "__main__":
    elements = input()
    nums = list(map(int, elements.split()))

    print(*sort_by_freq(nums))