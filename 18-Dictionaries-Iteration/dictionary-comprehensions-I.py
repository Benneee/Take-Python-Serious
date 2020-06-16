# Comprehensions create objects out of other objects

languages = ["JavaScript", "Python", "Ruby"]

# For dictionary comprehension
lengths = { language:len(language) for language in languages }
print(lengths)

# For languages that have the letter "t"
lengths = { language:len(language) for language in languages if 't' in language }
print(lengths)

word = "supercalifragilisticexpialidocious"
# Return the number of times each character appear in the word as the value to the letter which will be the key
letter_count = { letter: word.count(letter) for letter in word }
print(letter_count)

# If the letter is greater than "j"
letter_count = { letter: word.count(letter) for letter in word if letter > "j" }
print(letter_count)