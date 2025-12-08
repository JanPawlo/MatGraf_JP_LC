from vector import Vector
from line import Line

class Sphere(object):
    def __init__(self, radius, center: "Vector"):
        self.radius = radius
        self.center = center

    def sphere_and_line_cross(self, line: "Line"):
        return None