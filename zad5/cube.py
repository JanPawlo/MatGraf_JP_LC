from vector import Vector


class Cube():
    
    def __init__(self, x, y, z, edge):
        
        self._planes = list()
        self.vertices = list(Vector(x+(edge/2), y+(edge/2), z+(edge/2)),
                             Vector(x-(edge/2), y-(edge/2), z-(edge/2)))
        
        
        
        
        
        