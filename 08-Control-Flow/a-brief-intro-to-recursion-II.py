# First line of thought
def reverse(word: str):
    print(word[::-1])

# Using a while loop
def reverse(word: str):
    start_index = 0;
    last_index = len(word) - 1
    reversed_string = ""

    while last_index >= start_index:
        reversed_string += word[last_index]
        last_index -= 1
    
    return reversed_string

# Using recursion
def reverse(word: str):
    # First, the base case
    if len(word) <= 1:
        return word
    # Now, the main implementation 
    else:
        return word[-1] + reverse(word[:-1])


# print(reverse("straw"))