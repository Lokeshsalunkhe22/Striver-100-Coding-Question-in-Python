def binary_to_decimal(n):
    
    #return int(n, 8)

    decimal_number = 0
    power = 0

    for digit in reversed(n):
        decimal_number +=  int(digit) * (8 ** power)
        power += 1
    
    return decimal_number

if __name__ == "__main__":
    n = input("Binary Number: ")

    print(binary_to_decimal(n))