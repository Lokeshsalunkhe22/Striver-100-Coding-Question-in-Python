def capitalize_first_and_last_word(s):
    string = list(s)
    
    for i in range(len(string)):
        if i == 0 or i == len(string) - 1:
            string[i] = string[i].upper()
        elif string[i] == " ":
            string[i + 1] = string[i + 1].upper()
            string[i - 1] = string[i - 1].upper()
        
    return "".join(string)

if __name__ == "__main__":
    input_str = input()

    print(capitalize_first_and_last_word(input_str))