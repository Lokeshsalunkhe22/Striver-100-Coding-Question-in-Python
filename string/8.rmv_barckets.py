def rmv_brackets(s):
    result = ""

    for char in s:
        if char != "(" and char != ")":
            result += char

    return result

if __name__ == "__main__":
    input_str = input()

    print(rmv_brackets(input_str))