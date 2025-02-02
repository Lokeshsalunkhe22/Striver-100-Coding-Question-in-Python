def reverse_string(input_str):
    stack = []

    for char in input_str:
        stack.append(char)

    while stack:
        reverse_str += stack.pop()
    
    return reverse_str

if __name__ == "__main__":
    input_str = input()

    print(reverse_string(input_str))