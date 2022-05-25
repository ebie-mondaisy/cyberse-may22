# using underscores can privatise variable e.g. _breed <-- this is now a private variable

class Bark():
    def __init__(self, breed, name, age):
        #can also use __repr__
        self.breed = breed
        self.name = name
        self.age = age

    def __repr__(self):
        pass
        
    def speak(self):
        return self.breed


bark1 = Bark("Alsatian", "Rosie", 7)
bark2 = Bark("BIschon Frise", "Gloria", 4)

# bark1.name = "Maria"


print(bark1.speak())
print(bark2.speak())