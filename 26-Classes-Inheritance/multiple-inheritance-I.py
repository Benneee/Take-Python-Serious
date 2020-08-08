class Sport():
    def run(self):
        print("We have the marathon!")
    
    def time(self, minutes):
        print(f'Record time in {minutes} minutes')

class FitnessExercise():
    def jog(self):
        print("Fitfam bro! It's important")

    def time(self, minutes):
        print(f'Exercise for {minutes} minutes')

class LongDistanceRacing(FitnessExercise, Sport):
    # Because long distance running can be any of the two other classes
    pass

# As it is now, the class LDR inherits from both Sport Class and FitnessExercise class,
# However, the order in which things happen will be dependent on the proximity of said event to the main subclass

# e.g because both parent classes have the same time method, the one that will be executed first when I call time on the LDR class is the FitnessExercise class because of the order it is written
# However, if we have a time method in the LDR class and we call time on LDR, that time method will run first.

ldr = LongDistanceRacing();

# It exhibits methods from both parent classes
ldr.run()
ldr.jog()
ldr.time(35);

# To check order of method resolution, the mro method prints and array of the order at which methods will be executed from the level of the class referenced, in our case, it is the LDR class 
print(LongDistanceRacing.mro())