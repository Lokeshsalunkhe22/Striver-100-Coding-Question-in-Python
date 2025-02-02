def sum_of_num_of_str(s):
    current_number = 0
    tota_sum = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            total_sum += current_number
            current_number = 0

    total_sum += current_number

    return total_sum

if __name__ == "__main__":
    input_str = input()

    print(sum_of_num_of_str(input_str))