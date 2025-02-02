import cmath

def roots(a, b, c):
    d = b * b - 4 * a * c
    sqrt_val = cmath.sqrt(abs(d))  # cmath.sqrt handles complex numbers

    if d > 0:
        print("Roots are real and different")
        root1 = (-b + sqrt_val) / (2 * a)
        root2 = (-b - sqrt_val) / (2 * a)
        print("(",root1.real,",", root2.real,")")  # Only real part since the roots are real

    elif d == 0:
        print("Roots are real and same")
        root1 = -b / (2 * a)
        root2 = -b / (2 * a)
        print("(",root1,",", root2,")")

    else:  # d < 0
        print("Roots are complex")
        real_part = -b / (2 * a)
        imaginary_part = sqrt_val.imag
        print("(",(f"{real_part} + i{imaginary_part}"),",",(f"{real_part} - i{imaginary_part}"),")")
        

if __name__ == "__main__":
    a = int(input("Enter coefficient a: "))
    b = int(input("Enter coefficient b: "))
    c = int(input("Enter coefficient c: "))

    roots(a, b, c)
