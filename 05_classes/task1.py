from math import sqrt

class Point3D:
    x = None
    y = None
    z = None

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        return sqrt((self.x-other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

