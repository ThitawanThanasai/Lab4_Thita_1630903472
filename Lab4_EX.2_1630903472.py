class pyramid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    def volume(self):
        return self.length * self.width * self.height / 3
pyramid1 = pyramid(10, 7, 17)
# measure of pyramid
print("Volume of pyramid1: ", pyramid1.volume())