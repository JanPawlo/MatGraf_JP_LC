from vector import Vector
from line import Line
from math import sqrt

class Sphere(object):
    def __init__(self, radius: float, center: "Vector"):
        self.radius = radius
        self.center = center

    def sphere_and_line_cross(self, line: "Line"):
        # wg. wzoru szukamy współczynników równania kwadratowego
        P0 = line.point
        v = line.vector
        C = self.center
        r = self.radius

        # wektor od środka sfery do punktu początkowego prostej
        oc = P0 - C

        a = v.dot_product(v)
        b = 2 * v.dot_product(oc)
        c = oc.dot_product(oc) - r * r

        delta = b * b - 4 * a * c

        if delta < 0:
            return None, None  # brak przecięć
        elif delta == 0:
            t = -b / (2 * a)
            return line.calculate_point(t), None  # jedno przecięcie
        else:
            sqrt_d = sqrt(delta)
            t1 = (-b - sqrt_d) / (2 * a)
            t2 = (-b + sqrt_d) / (2 * a)
            return line.calculate_point(t1), line.calculate_point(t2) # dwa
