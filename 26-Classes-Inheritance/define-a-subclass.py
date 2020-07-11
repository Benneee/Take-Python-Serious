class Store():
  def __init__(self):
    self.owner = 'Benedict'

  def exclaim(self):
    return "Lots of stuff buy, come inside!"

# To inherit from the superclass, we pass the name of the superclass as an argument to the subclass
class CoffeeShop(Store):
  pass

starbucks = CoffeeShop()
print(starbucks.exclaim())
