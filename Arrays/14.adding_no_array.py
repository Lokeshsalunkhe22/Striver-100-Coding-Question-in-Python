def insert_begin(arr,  value):
    nums = [0] * (len(arr)+1)
    for i in range(len(arr)-1, -1, -1):
        nums[i+1] = arr[i]
    nums[0] = value
    print(nums)

def insert_end(arr, value):
    arr.append(value)
    print(arr)
    
def insert_position(arra, value, locaction):
    #location = loc - 1
    num = [0] * (len(arra)+1)
    for i in range(location):
        num[i] = arr[i]

    for i in range(location, len(arra)):
        num[i+1] = arr[i]

    num[location] = value
    print(num)

if __name__ == "__main__":
    elements = input()
    arr = list(map(int, elements.split()))
    value = 200
    location = 2

    insert_begin(arr,value)
    insert_position(arr, value, location)
    insert_end(arr, value)
    
