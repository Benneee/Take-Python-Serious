import argparse

parser = argparse.ArgumentParser(description="I want to know you, here's how we will do that. If your answers will be more than one word, please wrap them in quotes.")

parser.add_argument('--name', type=str, help= ' enter your name ')
parser.add_argument('--age', type=str, help= ' enter your age ')
parser.add_argument('--mission', type=str, help= ' why are you here? ')
parser.add_argument('--book', type=str, help= ' if this was a book about you, give us a title ')

# This creates an object with the arguments created above as strings
args = parser.parse_args()

name, age, mission, book = args.name, args.age, args.mission, args.book

# print(name)
# print(age)
# print(mission)
# print(book)

# Tip: if arguments value is more than one word, wrap in quotes

# Let us write the stuff to a file
with open(book+'.txt', "a") as new_book:
    new_book.write(f"Hello there, my name is {name}")
    new_book.write(f"\nI am {age} years old")
    new_book.write(f"\nI want to {mission}")

print("Book created!")

with open(book+'.txt', "r") as file_object:
    print(file_object.read())