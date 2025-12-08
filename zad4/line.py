import math

from vector import Vector
from vector import find_angle
from plane import Plane

class Line(object):
    def __init__(self, point: "Vector", vector: "Vector"):
        self.point = point
        self.vector = vector

    def calculate_point(self, t):
        return self.point + self.vector * t

    def line_and_line_cross(self, other: "Line"):
        """
        Returns point where the line crosses the other line.
        """
        v1_v2_cross = self.vector.cross_product(other.vector)
        p2_p1_diff = other.point - self.point

        t_norm = v1_v2_cross.length()
        t_norm *= t_norm

        t1_cross = other.vector.cross_product(v1_v2_cross)

        t1 = p2_p1_diff.dot_product(t1_cross) / t_norm

        t2_cross = self.vector.cross_product(v1_v2_cross)

        t2 = p2_p1_diff.dot_product(t2_cross) / t_norm

        result = self.calculate_point(t1)
        if result != other.calculate_point(t2):
            return None
        return result

    def angle(self, other):
        return radians_to_degrees(find_angle(self.vector, other.vector))

class Segment(object):
    def __init__(self, endpoint1: "Vector", endpoint2: "Vector"):
        point = endpoint1
        vector = endpoint2 - endpoint1
        self.line = Line(point, vector)
        self.endpoint1 = endpoint1
        self.endpoint2 = endpoint2

    def segment_and_segment_cross(self, other: "Segment"):
        A = self.endpoint1
        B = self.endpoint2
        C = other.endpoint1
        D = other.endpoint2

        AB = B - A
        AC = C - A

        # punkty sa wspoliniowe wiec nie daloby sie stworzyc plaszczyzny
        normal = AB.cross_product(AC)
        if normal.length() == 0:
            return None

        plane = Plane(normal.x, normal.y, normal.z, normal.dot_product(A))

        if not plane.contains_point(D):
            return None

        def check_side(P0, P1, Q1, Q2):
            v = P1 - P0
            n = v.cross_product(normal)

            s1 = (Q1 - P0).dot_product(n)
            s2 = (Q2 - P0).dot_product(n)

            if s1 == 0 or s2 == 0:
                return 0

            return 1 if s1 * s2 < 0 else -1

        # sprawdzenie AB względem CD
        if check_side(C, D, A, B) == -1:
            return None

        # sprawdzenie CD względem AB
        if check_side(A, B, C, D) == -1:
            return None

        return self.line.line_and_line_cross(other.line)




def radians_to_degrees(radians):
    return radians * 180 / math.pi