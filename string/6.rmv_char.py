def remove_char(s):
    result = ""

    for i in range(len(s)):
        ascii_value = ord(s[i])

        if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):
            result += s[i] 

    """for char in input_str:
        if char.isalpha(): #using predefined function
            result += char"""

    return result

if __name__ == "__main__":
    input_str = input()

    print(remove_char(input_str))