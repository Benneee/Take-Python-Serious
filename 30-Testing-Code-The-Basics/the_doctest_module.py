# Doctest is a lightweight test module

def sum_of_list(numbers):
    """Returns the sum of all numbers in a list
    >>> sum_of_list([1, 2, 3])
    6
    >>> sum_of_list([5, 8, 13])
    26
    """
    total = 0
    for num in numbers:
        total += num
    return total


if __name__ == "__main__":
    import doctest
    # testmod is going to go through our function
    # and look for pieces of text that look like python expression
    # and run the python code and validate that what it gets back is
    # what is written as the answer in the line below

    # If the test code in the docstring is incorrect, there will be an error message in the terminal
    # Also, if the code is wrong, there would also be another error in the terminal

    doctest.testmod()