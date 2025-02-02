def count(s):
    vowels = 0
    consonants = 0
    spaces = 0
    lower_str = s.lower()

    for chara in lower_str:
        if chara == "a" or chara == "e" or chara == "i" or chara == "o" or chara == "u":
            vowels += 1
        elif chara >= "a" and chara <= "z":
            consonants += 1
        elif chara == " ":
            spaces += 1
    return vowels, consonants, spaces        

if __name__ == "__main__":
    input_str = input()

    vowels, consonants, spaces = count(input_str)
    
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"White spaces: {spaces}")