import math
import calculator

# Every module has a private dunder name variable
print(math.__name__)
print(calculator.__name__)

# If we print __name__ in the file where we are currently working, __main__ would be the output
# If a file is being used as a module, __name__ would evaluate to the name of the file

# If we compare __main__ to __name__, can compare both values to see the file being run as a script