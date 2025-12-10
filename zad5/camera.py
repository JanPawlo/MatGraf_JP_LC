from vector import Vector
from line import Line


class Camera(object):
    def __init__(self, width, height, starting_point: "Vector", distance: "Vector"):
        self.width = width
        self.height = height
        self.point = starting_point
        self.distance = distance

    def generate_ray(self, x_scalar, y_scalar):
        if x_scalar > 1 or x_scalar < -1:
            raise ValueError("x_scalar must be between -1 and 1")
        if y_scalar > 1 or y_scalar < -1:
            raise ValueError("y_scalar must be between -1 and 1")
        ray = Line(self.point, self.distance + Vector((self.width / 2) * x_scalar, (self.height / 2) * y_scalar, 0))

