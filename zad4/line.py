import math

from vector import Vector
from vector import find_angle

class Line(object):
    def __init__(self, point: "Vector", vector: "Vector"):
        self.point = point
        self.vector = vector

    def calculate_point(self, t):
        return self.point + self.vector * t

    def line_and_line_cross(self, other: "Line"):
        v1_v2_cross = self.vector.cross_product(other.vector)
        p2_p1_diff = other.point - self.point

        t_norm = v1_v2_cross.length()
        t_norm *= t_norm

        t1_cross = other.vector.cross_product(v1_v2_cross)

        t1 = p2_p1_diff.dot_product(t1_cross) / t_norm

        t2_cross = self.vector.cross_product(v1_v2_cross)

        t2 = p2_p1_diff.dot_product(t2_cross) / t_norm

        return t1, t2

    def angle(self, other):
        return radians_to_degrees(find_angle(self.vector, other.vector))

def radians_to_degrees(radians):
    return radians * 180 / math.pi