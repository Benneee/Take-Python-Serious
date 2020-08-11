# Composition: when an object stores another object as its attribute and delegates responsibilities to that object
class Paper():
  def __init__(self, text, case):
    self.text = text
    self.case = case


class Briefcase():
  def __init__(self, price):
    self.price = price
    self.papers = []

  def add_paper(self, paper):
    self.papers.append(paper)

  def view_notes(self):
    return [paper.text for paper in self.papers]


class Lawyer():
  def __init__(self, name, briefcase):
    self.name = name
    self.briefcase = briefcase

  def write_note(self, text, case):
    paper = Paper(text, case)
    self.briefcase.add_paper(paper)

  def view_notes(self):
    print(self.briefcase.view_notes())


cheap_briefcase = Briefcase(200)

vinny = Lawyer(name="Vincent", briefcase=cheap_briefcase)
vinny.write_note("My client is innocent", "BC123")
vinny.write_note("There is no evidence of a crime", "BC123")
vinny.view_notes()
