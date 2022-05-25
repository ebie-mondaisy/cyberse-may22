from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, no_of_legs, fur_colour):
        self.no_of_legs = no_of_legs
        self.fur_colour = fur_colour

    def __repr__(self) -> str:
        return f"{self.no_of_legs} legs and fur colour is {self.fur_colour}"

    ##@abstractmethod
    def speak(self):
            pass

class Cat(Animal):
    def __init__(self, no_of_legs, fur_colour, love_of_fish):
        super().__init__(no_of_legs, fur_colour)
        self.love_of_fish = love_of_fish

    def __repr__(self) -> str:
        return f"{self.no_of_legs} legs and fur colour is {self.fur_colour} and level of love for fish is {self.love_of_fish}"

    def speak(self):
        return f"Meow"
    

class Dog(Animal):
    def __init__(self, no_of_legs, fur_colour):
        super().__init__(no_of_legs, fur_colour)

cat1 = Cat(4, "Tabby", 5)
dog1 = Dog(4, "Brindle")

print(cat1)
print(dog1)