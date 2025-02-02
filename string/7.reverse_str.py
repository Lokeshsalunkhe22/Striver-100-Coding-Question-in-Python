def reverse_string(input_str):
    char_list = list(input_str)

    left, right = 0, len(input_str)-1

    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]

        left += 1
        right -= 1

    return "".join(char_list)


if __name__ == "__main__":
    input_str = input()

    print(reverse_string(input_str))