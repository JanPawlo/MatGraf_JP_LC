



class Vector:
    
    def __init___(self, x:float, y:float, z:float):
        self.x = x;
        self.y = y
        self.z = z
        
    def __add__(self, other:"Vector"):
        if (not isinstance(other, Vector)):
            raise ValueError("Non-vector added")
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)
    
    
