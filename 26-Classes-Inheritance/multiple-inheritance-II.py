class Restaurant():
  def make_reservation(self, party_size):
    print(f"Booked a table for {party_size}")

class Steakhouse(Restaurant):
  pass

class Bar():
  def make_reservation(self, party_size):
    print(f"Booked a lounge for {party_size}")

class BarAndGrill(Steakhouse, Bar):
  pass

# Python does DFS
bag = BarAndGrill()
bag.make_reservation(2)

# To check the search order
print(BarAndGrill.mro())

# Because the Steakhouse class inherits from the Restaurant class, it also has the make_reservation
# ...method available to it. By default, Python carries out a DFS to search for the method, hence, it will
# ...go through the Steakhouse class and get to the Restaurant class if it doesn't find the method in the
# ...Steakhouse class before coming out of that depth to then go to the Bar class to find the make_reservation method.

# Depth First Search
# The algorithm prioritises getting to the deepest level, layer or tier first.

# Breadth First Search
# The algorithm prioritises clearing out the current level, layer or tier before going deeper.


