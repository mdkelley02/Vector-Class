import math

class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x}, {self.y}>"

    def __add__(self, other):
        if type(other) is Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError('Unsupported type')

    def __sub__(self, other):
        if type(other) is Vector:
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError('Unsupported type')

    def __rmul__(self, other):
        if type(other) is int or type(other) is float:
            return Vector(other*self.x, other*self.y)
        elif type(other) is Vector:
            return  Vector(self.x * other.x, self.y * other.y)
        else:
            raise TypeError('Unsupported type')

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def toUnitVector(self):
        return Vector(self.x/self.magnitude(), self.y/self.magnitude())

    


k = -((math.sqrt(265)) / (math.sqrt(265/4)))
print((k*Vector(8,(-3/2))).magnitude())
print(math.sqrt(265))


     

