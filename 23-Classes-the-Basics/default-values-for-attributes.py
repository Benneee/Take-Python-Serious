class Book():
    def __init__(self, title, author, price = 14.99):
        self.title = title
        self.author = author
        self.price = price


animal_farm = Book("Animal Farm", "George Orwell", 19.99)
gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")

print(animal_farm.price)
print(gatsby.title)