def remove_duplicates(s):
    result = ""

    for char in s:
        if char not in result:
            result += char
    
    return result

if __name__ == "__main__":
    input_str = input()
    print(remove_duplicates(input_str))