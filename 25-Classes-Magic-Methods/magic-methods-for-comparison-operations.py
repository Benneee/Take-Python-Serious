class Student():
    def __init__(self, math, physics, chemistry, biology):
        self.math = math
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology

    @property
    def grades(self):
        return sum([self.math, self.physics, self.chemistry, self.biology])

    # The dunder eq method checks for equality two objects created from a class
    def __eq__(self, other_student):
        return self.grades == other_student.grades

    def __gt__(self, other_student):
        return self.grades > other_student.grades

    

bola = Student(math=70, physics=80, chemistry=90, biology=90)
seun = Student(math=80, physics=90, chemistry=90, biology=70)
dotun = Student(math=50, physics=60, chemistry=55, biology=70)

print(bola.grades)
print(seun.grades)
print(dotun.grades)

print(seun.grades == dotun.grades)
print(seun.grades == bola.grades)

# We also invariably get inequality
print(seun.grades != dotun.grades)