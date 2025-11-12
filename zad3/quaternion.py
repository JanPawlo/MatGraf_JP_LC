from vector import Vector


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

    def __str__(self):
        return f"({str(self.a)}, {str(self.vector)})"