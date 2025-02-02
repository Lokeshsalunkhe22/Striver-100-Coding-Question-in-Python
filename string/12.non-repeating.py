def non_repeating_char(s):
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    for char, count in frequency.items():
        if count == 1:
            print(char, end = "")

if __name__ == "__main__":
    input_str = input()

    non_repeating_char(input_str)