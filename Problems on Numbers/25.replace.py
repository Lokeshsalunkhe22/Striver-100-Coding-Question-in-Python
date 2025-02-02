def replace(n):
    s = str(n)

    replace_str = s.replace("0","1")

    return int(replace_str)

if __name__ == "__main__":
    n = int(input())

    print(replace(n))