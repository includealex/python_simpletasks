import numpy as np

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(other * self.x, other * self.y)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other
    
    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("unsupported operand type(s)\n\tfor -: 'Vector' and '{}'".format(type(other).__name__))
    
    def __truediv__(self, val):
        if isinstance(val, (int,float)):
            if val == 0:
                raise ValueError("Division by zero is not allowed.")
            return Vector(self.x / val, self.y / val)
        else:
            raise TypeError("unsupported operand type(s)\n\tfor -: 'Vector' and '{}'".format(type(val).__name__))
    
    def __abs__(self):
        return np.sqrt(self.x**2 + self.y**2)
