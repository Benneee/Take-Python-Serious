# Attributes are public by default and they can be accessed using the dot syntax
class Guitar():
  def __init__(self):
    print(f'A new guitar is being created. This object is {self}')

acoustic = Guitar()
electric = Guitar()

# This style of attribute assignment is anti-pattern
acoustic.wood = 'Mahogany'
acoustic.strings = 6
acoustic.year = 1990

electric.nickname = 'Sound Viking 3000'
