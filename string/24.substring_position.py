def find_substring_position(str1, str2):

    index = str1.find(str2)
    if index != -1:
        return index
    else:
        return -1

if __name__ == "__main__":
    str1 = input()
    str2 = input()

    print(find_substring_position(str1, str2))
    