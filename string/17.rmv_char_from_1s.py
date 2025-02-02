def rmv_char_from_1_present_in_2(s1, s2):
    char_set = set(s2)  #convert to set for efficient checking
    
    for char in s1:
        if char not in char_set:
            print(char, end = "")

if __name__ == "__main__":
    string1 = input()
    string2 = input()

    rmv_char_from_1_present_in_2(string1, string2)