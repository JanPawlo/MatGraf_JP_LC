from vector import Vector
from line import Line


class Cube():
    
    def __init__(self, x, y, z, edge):
        
        self._planes = list()
        self.vertices = [Vector(x+(edge/2), y+(edge/2), z+(edge/2)),
                        Vector(x-(edge/2), y-(edge/2), z-(edge/2))]

    def calculate_ray_cross(self, line: "Line"):
        return False