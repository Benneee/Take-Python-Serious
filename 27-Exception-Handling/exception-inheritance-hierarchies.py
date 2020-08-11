class Mistake(Exception):
  pass

class StupidMistake(Mistake):
  pass

class SillyMistake(Mistake):
  pass


try:
  raise StupidMistake("Extra stupid mistake")
except StupidMistake as e:
  print(f"Caught the error: {e}")

# A parent class will always produce the same effect as its child classes
# Sibling classes will not catch each other's errors
try:
  raise SillyMistake("Extra silly mistake")
except Mistake as e:
  print(f"Caught the error: {e}")


try:
  raise StupidMistake("Extra stupid mistake")
except Mistake as e:
  print(f"Caught the error: {e}")
