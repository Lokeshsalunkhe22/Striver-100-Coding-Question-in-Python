def change_case_of_char(s):
    result = ""

    """for char in s:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()"""
    
    for char in s:
        if char.isalpha():
            ascii = ord(char)
            if ascii >= 65 and ascii <= 90:
                result += chr(ascii + 32)
            elif ascii >= 97 and ascii <= 122:
                result += chr(ascii - 32)

    return result
                
if __name__ == "__main__":
    input = input()

    print(change_case_of_char(input))