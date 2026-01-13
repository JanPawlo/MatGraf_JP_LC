from plane import Plane

class LimitedPlane(Plane):
    
    def __init__(self, a, b, c, d, x_up, x_down, y_up, y_down, z_up, z_down):
        super.__init__(self, a, b, c, d)
        
    def contains_point(self, P)