from vector import Vector

class Line(object):
    def __init__(self, point: "Vector", vector: "Vector"):
        self.point = point
        self.vector = vector

    def calculate_point(self, t):
        return self.point + self.vector * t

    def line_and_line_cross(self, other: "Line"):
        v1_v2_cross = self.vector.cross_product(other.vector)
        t1 = (other.point - self.point).cross_product(other.vector).dot_product(v1_v2_cross)

        t1_norm = (self.vector.cross_product(other.vector)).length()
        t1 /= t1_norm * t1_norm

        t2 = (other.point - self.point).cross_product(self.vector).dot_product(v1_v2_cross)
        t2_norm = (self.vector.cross_product(other.vector)).length()
        t2 /= t2_norm * t2_norm

        return t1, t2