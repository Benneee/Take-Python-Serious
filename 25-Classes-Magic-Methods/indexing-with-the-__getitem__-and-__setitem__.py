# The dunder getitem method helps us access the properties of an object by the index, they tell python
# ... what property is being sought

class CrayonBox():
    def __init__(self):
        self.crayons = []

    # Push crayons into the list declared above
    def add(self, crayon):
        self.crayons.append(crayon)

    # Ordinary, we can't use get the items pushed into the crayons list as we need to tell Python exactly how to
    # ... ask this class for what it wants
    def __getitem__(self, index):
        return self.crayons[index]

    # To overwrite values
    def __setitem__(self, index, newvalue):
        self.crayons[index] = newvalue



cb = CrayonBox()
cb.add('blue')
cb.add('purple')
cb.add('yellow')
cb.add('grey')
cb.add('brown')

# print(cb[0]);
# print(cb[1]);


# cb[0] = 'red'
# print(cb[0])


#  We can also iterate over this object as a result of the getitem magic method set
for crayon in cb:
    print(crayon)