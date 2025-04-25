print("sv: trần nguyễn viết đức.")
print ("mssv:235752020710013")

####
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

circle = Circle(5)  # Thay 5 bằng bán kính mong muốn
print("Diện tích:", circle.area())
print("Chu vi:", circle.circumference())