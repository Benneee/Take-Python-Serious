# Much like the map function, you can pass each character of an iterable through another function
# ...using the filter, however, the return value of the other function has to be a boolean
# So the filter's return value will only contain elements that meet whatever condition set within the 
# ... external function
# Filter also returns a filter object

def return_even(number):
    if number % 2 == 0:
        return number


numbers = range(10);

even_numbers = list(filter(return_even, numbers))
# print(even_numbers)
