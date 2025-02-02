def num_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
            "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 0:
        return "zero"
    
    result = ""

    # Handling the thousands place
    if n >= 1000:
        result += ones[n // 1000] + " thousand "
        n %= 1000

    # Handling the hundreds place
    if n >= 100:
        result += ones[n // 100] + " hundred "
        n %= 100

    # Handling the tens and ones places
    if n >= 20:
        result += tens[n // 10] + " "
        n %= 10

    if n > 0:
        result += ones[n]
    
    return result.strip()

if __name__ == "__main__":
    n = int(input("Number in Digit: "))

    print(num_to_words(n))