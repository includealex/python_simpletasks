import numpy as np
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

class Segment3D:
    p1 = None
    p2 = None

    def __init__(self, p1: Point3D, p2:Point3D):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return (self.p1).distance_to(self.p2)

    def middle(self) -> Point3D:
        return Point3D((self.p1.x + self.p2.x)/2, (self.p1.y + self.p2.y)/2, (self.p1.z + self.p2.z)/2);

    def vectorise(self):
        vec = [(self.p2.x - self.p1.x), (self.p2.y - self.p1.y), (self.p2.z - self.p1.z)];
        return vec

    def cos_to(self, other):
        vec_f = self.vectorise()
        vec_s = other.vectorise()

        numenator = sum(np.abs(vec_f[i] * vec_s[i]) for i in range(len(vec_f)))
        denumenator = sqrt(sum(map(lambda i: i * i, vec_f))) * sqrt(sum(map(lambda i: i * i, vec_s)))

        res = numenator / denumenator
        return res
