class FilmMaker():
  def give_interview(self):
    print("I love making movies!")

class Director(FilmMaker):
  pass

class Screenwriter(FilmMaker):
  def give_interview(self):
    print("I love writing scripts")

class JackOfAllTrades(Director, Screenwriter):
  pass


stallone = JackOfAllTrades()

stallone.give_interview()

print(JackOfAllTrades.mro())

# The exception to the DFS thing
# If there are two or more occurrences of the parent class in the search order, Python disposes the earlier occurrences and uses the last one in the mro.
