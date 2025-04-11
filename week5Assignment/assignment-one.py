# Base class
class Character:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Encapsulated attribute

    def intro(self):
        print(f"I'm {self.name}, and I'm {self._age} years old.")

# Subclass with extra attributes and methods
class Superhero(Character):
    def __init__(self, name, age, power, alias):
        super().__init__(name, age)
        self.power = power
        self.alias = alias

    def use_power(self):
        print(f"{self.alias} uses {self.power}! 💥")

    def intro(self):  # Polymorphism: method overriding
        print(f"I am {self.alias}, aka {self.name}, and I fight for justice! 🦸")

# Create objects
hero1 = Superhero("Bruce Wayne", 35, "Stealth and Gadgets", "Batman")
hero2 = Superhero("Clark Kent", 33, "Super Strength", "Superman")
hero3 = Superhero("Tony Stark", 40, "Superhuman strength, durability, and the ability to fly", "Iron man")

hero1.intro()
hero1.use_power()

hero2.intro()
hero2.use_power()

hero3.intro()
hero3.use_power()
