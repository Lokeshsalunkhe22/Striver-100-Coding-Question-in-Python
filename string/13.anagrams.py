def anagrams(string1, string2):
    return sorted(string1) == sorted(string2)

if __name__ == "__main__":
    string1 = input()
    string2 = input()

    if anagrams(string1, string2):
        print("True")
    else:
        print("False")
