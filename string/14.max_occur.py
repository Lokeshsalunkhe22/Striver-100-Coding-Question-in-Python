def maximum_occuring_str(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    max_freq = 0
    max_char = ""
    for char, count in frequency.items():
        """if count == max(frequency.values()): #using max function
            return char"""
        if count > max_freq:
            max_freq =  count
            max_char = char

    return max_char

if __name__ == "__main__":
    input_str = input()
    print(maximum_occuring_str(input_str))