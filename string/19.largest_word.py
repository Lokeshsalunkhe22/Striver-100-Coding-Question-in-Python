def largest_word_in_string(s):
    words = s.split()

    largest_word = ""
    max_length = 0

    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            largest_word = word
    
    return largest_word

if __name__ == "__main__":
    input = input()
    
    print(largest_word_in_string(input))