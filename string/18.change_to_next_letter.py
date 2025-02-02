def change_to_next_letter(s):
    result = ""

    for char in s:
        if char.isalpha():
            if char == "z":
                result += "a"
            elif char == "Z":
                result += "A"
            else:
                result += chr(ord(char)+1)
        else:
            result += char
    
    return result

if __name__ == "__main__":
    string = input()

    print(change_to_next_letter(string))