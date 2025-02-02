def sort_characters(string):
    s = list(string)
    n = len(string)
    for i in range(n):
        for j in range(0, n - i - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    
    return "".join(s)

if __name__ == "__main__":
    input = input()
    
    print(sort_characters(input))