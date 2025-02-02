def reverse_words_in_string(input):
    words = input.split()

    left = 0
    right = len(words) - 1

    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return " ".join(words)    
    
if __name__ == "__main__":
    input = input()

    print(reverse_words_in_string(input))