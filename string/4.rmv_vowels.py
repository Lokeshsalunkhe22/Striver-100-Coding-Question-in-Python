def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""

    for char in s:
        if char not in vowels:
            result += char
    
    return result
"""
    result = [char for char in input_str if char not in vowels] # This is a list comprehension version of the above code
    return "".join(result)   #with O(n) Complexity
"""
if __name__ == "__main__":
    input_str = input()
    
    print(remove_vowels(input_str))