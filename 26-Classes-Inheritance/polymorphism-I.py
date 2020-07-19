# Polymorphism is a concept that describes the way objects reacts to a particular method.
# It's more concerned about behavior than object type
class Person():
  def __init__(self, name, height):
    self.name = name
    self.height = height

  def __len__(self):
    return self.height

# The inbuilt len() function will always return the length of any object as long as dunder len
# ... method applies to that object.
values = [
  "Ben",
  [1, 2, 3],
  (4, 5, 6, 7),
  { "a": 1, "b": 2 },
  Person(name="Ben", height=71)
]

for value in values:
  print(len(value))
