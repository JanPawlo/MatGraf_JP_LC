import vector
from vector import Vector
import math



class Quaternion:
    def __init__(self, a, vector):
        self.a = a
        self.vector = Vector(vector.x, vector.y, vector.z)

    def __add__(self, other):
        return Quaternion(self.a + other.a,
                          self.vector + other.vector)

    def __sub__(self, other):
        return Quaternion(self.a - other.a,
                          self.vector - other.vector)

    def __mul__(self, other):
        return Quaternion(self.a * other.a - self.vector.dot_product(other.vector),
                          other.vector * self.a + self.vector * other.a + self.vector.cross_product(other.vector))

    def __truediv__(self, other):
        divider = other.a * other.a + other.vector.dot_product(other.vector)
        if divider == 0:
            raise ZeroDivisionError
        result_scalar = (self.a * other.a + self.vector.dot_product(other.vector)) / divider
        result_vector = (other.vector * self.a * -1.0 + self.vector * other.a - self.vector.cross_product(other.vector)) * (1.0 / divider)
        return Quaternion(result_scalar, result_vector)

    def __eq__(self, other):
        if not isinstance(other, Quaternion):
            return False
        return (self.a == other.a and 
            self.vector.x == other.vector.x and
            self.vector.y == other.vector.y and
            self.vector.z == other.vector.z)

        
    def __str__(self):
        return f"({str(self.a)}, {str(self.vector)})"
    
    
def degrees_to_radians(degrees:float):
    return degrees * math.pi /180