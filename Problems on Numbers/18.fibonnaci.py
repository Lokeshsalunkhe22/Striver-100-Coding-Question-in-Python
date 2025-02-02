def fibonnaci(n):
    a = 0
    b = 1

    series = [a]

    for _ in range(n):
        series.append(b)
        
        a, b = b, a+b

        """
        temp = a
        a = b
        b = temp + b
        """
          
    return series

if __name__ == "__main__":
    n = int(input())

    series = fibonnaci(n)
    print(*series)