# A set is a mutable, unordered data structure that prohibits duplicate values
# The set is made up of comma-separated values in curly braces
# It should not be used for order or to show relationship / association. Those responsibilities are best suited for lists and dictionaries instead

stocks = { "MSFT", "IBM", "OPR", "IBM" }
print(type(stocks))
print(stocks) # Only 3 items will be printed because sets prohibit duplicate values

# The values inside a set must be immutable
lottery_numbers = { (1,2,3), (4,5,6), (1,2,3), (7,8,9) }
print(lottery_numbers)

# Simlarities between sets and lists
# Length
print(len(lottery_numbers))

# in and not in (Inclusion and Exclusion) 
print('MSFT' in stocks)
print('GOOG' in stocks)

# Iteration
for numbers in lottery_numbers:
    print(numbers)

# They both support comprehension
numbers = [-5, 2, 4, 5, 3, 7, 3]
squares = { number ** 2 for number in numbers }
print(squares) # As expected the values printed will be lesser in length than the original list because set prohibits duplication


# print(dir(set))

