def binary_to_decimal(n):
    
    #return int(n, 2)

    decimal_number = 0
    power = 0

    for bit in reversed(n):
        if bit == "1":
            decimal_number += 2 ** power
        power += 1
    
    return decimal_number

if __name__ == "__main__":
     n = input("Binary Number: ")

     print(binary_to_decimal(n))