class cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def volume(self):
        return self.radius**2 * 3.14 * self.height
    def surface_area(self):
        return 2 * 3.14 * self.radius * self.height + 2 * 3.14 * self.radius**2
cylinder1 = cylinder(5, 10)
cylinder2 = cylinder(7, 13)
# measure of cylinders
print("Volume of cylinder1: ", cylinder1.volume())
print("Surface area of cylinder1: ", cylinder1.surface_area())
print("Volume of cylinder2: ", cylinder2.volume())
print("Surface area of cylinder2: ", cylinder2.surface_area())