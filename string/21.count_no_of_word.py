def count_no_of_words(s):
    split_str = s.split()

    count = 0

    for word in split_str:
        count += 1

    """ #without using split()
    count = 1
    for char in s:
        if char == " ":
            count += 1"""

    return count

if __name__ == "__main__":
    input = input()
    
    print(count_no_of_words(input))