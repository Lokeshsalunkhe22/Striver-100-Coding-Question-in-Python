def rotate(arr, k):
    N = len(arr)
    temp = [0] * N
    
    for i in range(N):
        temp [i] = arr[(i + k) % N]

    print(temp)
    
if __name__ == "__main__":
    elements = input()
    arr = list(map(int, elements.split()))
    k = int(input())
    
    rotate(arr, k)
