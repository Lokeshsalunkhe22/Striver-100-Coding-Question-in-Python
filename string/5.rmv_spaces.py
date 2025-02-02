def remove_spaces(s):
    result = ""

    for char in input_str:
        if not char.isspace():  #if char != " ":
            result += char
            
    return result

if __name__ == "__main__":
    input_str = input()

    print(remove_spaces(input_str))