class Vehicle:
    def move(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing on the water 🚢"

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(f"{v.__class__.__name__} is moving by: {v.move()}")