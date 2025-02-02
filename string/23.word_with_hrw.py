def word_with_highest_repeated_word(s):
    words = s.split()

    max_repeat = 1
    max_word = ""

    for word in words:
        repeat = count_repeat(word)
        if repeat > max_repeat:
            max_repeat = repeat
            max_word = word

    if max_repeat > 1:
        return max_word
    else:
        return -1

def count_repeat(word):
    frequency = {}
    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return max(frequency.values())


if __name__ == "__main__":
    input = input()
    print(word_with_highest_repeated_word(input))