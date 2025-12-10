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
        return ray

    def generate_ray_list(self, x_pixels, y_pixels):
        ray_list = []
        for x in range(x_pixels):
            for y in range(y_pixels):
                ray_list.append(self.generate_ray(1 - x / (x_pixels / 2) , 1 - y / (y_pixels / 2 )))
        return ray_list
