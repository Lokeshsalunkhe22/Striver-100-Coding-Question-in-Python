def decimal_to_binary(n):

    #return oct(n).replace("0b", "")  #shortcut method using bin() function

    if n == "0":
        return 0
    
    binary_str = ""

    while n > 0:
        remainder = n % 8
        binary_str = str(remainder) + binary_str
        n = n // 8
    
    return binary_str

if __name__ == "__main__":
    n = int(input("Decimal Number: "))

    print(decimal_to_binary(n))