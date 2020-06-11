# name, adjective, noun
mad_libs = "{} laughed at the {} {}." # Positional

mad_libs_with_numbers = "{0} laughed at the {1} {2}." # Ordinal

mad_libs_with_keywords = "{name} laughed at the {adjective} {noun}." # Keyword respective


# The format method allows you to inject strings within a string, however, there are two things to note
# The order in which the format method receives the argument to inject is important
# Also, if not enough arguments are provided, an index error will be thrown
# If two many arguments are provided, python will only pick out what it needs and move along without throwing any error

# print(mad_libs.format("Cindy", "silly", "clown"))

# We can also pass the values with numeric characters by assigning number into the curly braces
# What it means is that the order at which the numbers are placed in the curly braces respects the order that arguments are passed
# print(mad_libs_with_numbers.format("Cindy", "silly", "clown"))

# Instead of numbers, we can use descriptive variables within the curly braces, however, they word like keyword arguments which means that when assigning values, you have to assign directly to the keyword provided within the curly brace
# print(mad_libs_with_keywords.format(name="Cindy", adjective="silly", noun="clown"))

# Play with a user
name = input("Enter a name: ").title()
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")

print(mad_libs_with_keywords.format(name=name, adjective=adjective, noun=noun))

