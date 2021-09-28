from random import choice, sample, randint

# The choice method returns a random element from an iterable sequence such as a string, tuple or list
# The key idea here is that the sequence must have some form of order, hence, dictionary or set aren't supported

names = ['Bob', 'Moe', 'Curly']
name_tuple = ('Bob', 'Moe', 'Curly')
word = 'elephant'

print(choice(word))
print(choice(names))
print(choice(name_tuple))


# The sample method allows us to extract more than one element from a sequence - returns a list
lottery_numbers = [randint(1, 50) for value in range(50)]
# print(lottery_numbers)
print(sample(lottery_numbers, 5))

