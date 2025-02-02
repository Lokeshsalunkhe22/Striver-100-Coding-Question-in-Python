def find_lcm(num1, num2):
    gcd = 1

    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i # Update gcd if a common divisor is found
            break  # No need to check further; we found the GCD

    lcm = (num1 * num2) // gcd

    return lcm

if __name__ == "__main__":
    n1 = int(input("Num1: "))
    n2 = int(input("Num2: "))

    print(find_lcm(n1, n2))