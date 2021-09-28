# The random module helps with aspects of randomness
# Effective if you're building a card game or something with dice rolling or coin toss

from random import random, randint, randrange

print(random() * 100)

# The randint method accepts two arguments, a lower bound and an upper bound
print(randint(1, 5)) # The upper and lower bounds are inclusive in the results

# The randrange method provides a means for Python to jump steps when generating random numbers between two provided bounds/limits
print(randrange(20, 80, 5)) # The upper bound here is exclusive i.e it cannot be a part of the generated number