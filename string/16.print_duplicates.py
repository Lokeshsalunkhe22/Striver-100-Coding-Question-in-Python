def print_duplicates(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char, count in sorted(frequency.items()):
        if count > 1:
            print(f"{char} - {count}")

if __name__ == "__main__":
    input_str = input()
    print_duplicates(input_str)