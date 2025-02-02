import ast

def find_symmetric_pairs(pairs):
    store = {}
    for pair in pairs:
        first, second = pair
        if second in store and store[second] == first:
            print((first, second), end= " ")
        else:
            store[first] = second   

if __name__ == "__main__":

    elements = input()
    pairs = ast.literal_eval(f"[{elements}]")  # Safely convert the input string to a list of tuples

    """elements = input()
    arr = list(map(int, elements.split()))
    # Convert flat list of integers into pairs
    pairs = [(arr[i], arr[i + 1]) for i in range(0, len(arr), 2)]"""

    find_symmetric_pairs(pairs)