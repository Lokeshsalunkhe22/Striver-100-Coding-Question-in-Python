def isPalindrome(s):
    #return s == s[::-1] #shortcut by reversing it
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower != s[right].lower:
            return False
        else:
            left += 1
            right -= 1
    return True

if __name__ == "__main__":
    input_str = input()

    if isPalindrome(input_str):
        print("YES")
    else:
        print("NO")


        