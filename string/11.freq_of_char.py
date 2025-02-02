def freq_of_characters(s):
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    for char, freq in sorted(frequency.items()):
        print(f"{char}{freq}", end = " ")

if __name__ == "__main__":
    input_str = input()

    freq_of_characters(input_str)