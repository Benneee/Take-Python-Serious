class Employee():
    def do_work(self):
        print("I'm working!")


class Manager(Employee):
    def waste_time(self):
        print("Wow! This YouTube video looks fun!")


e = Employee()
m = Manager()

e.do_work()
m.do_work()

# I can only invoke this method on this class because it is a method that exists only on the subclass, Manager
m.waste_time()