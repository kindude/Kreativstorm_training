import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        try:
            return math.pi * self.radius**2
        except TypeError as error:
            print(f"You cannot pass string as a radius parameter {error}")

    def calculate_circumference(self):
        try:
            return 2 * math.pi * self.radius
        except TypeError as error:
            print(f"You cannot pass string as a radius parameter {error}")


circle = Circle(3)

print(f"Area: {circle.calculate_area()}")
print(f"Circumference: {circle.calculate_circumference()}")
