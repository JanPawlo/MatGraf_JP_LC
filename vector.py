import math



class Vector:
    
    def __init__(self, x:float, y:float, z:float):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other:"Vector"):
        if (not isinstance(other, Vector)):
            raise ValueError("Non-vector added")
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)
    
    def __sub__(self, other:"Vector"):
        if (not isinstance(other, Vector)):
            raise ValueError("Non-vector subtracted")
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector(x, y, z)
    
    def __mul__(self, scalar:float):
        if (not isinstance(scalar, float)):
            raise ValueError("Non-scalar multiplied!")
        x = self.x * scalar
        y = self.y * scalar
        z = self.z * scalar
    
        return Vector(x, y, z)
    
    def __div__(self, scalar:float):
        if (not isinstance(scalar, float)):
            raise ValueError("Non-scalar divided!")
        x = self.x / scalar
        y = self.y / scalar
        z = self.z / scalar
    
        return Vector(x, y, z)
    
    def length(self):
        return math.sqrt((self.x*self.x)
                         + (self.y*self.y)
                         + (self.z*self.z))
    
    def normalise(self):
        length = self.length()
        if (length == 0):
            raise ValueError("Vector lenght is 0")
        return self / length
    
    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"
    
    def dot_product(self, other:"Vector"):
        return (self.x * other.x +
                self.y * other.y +
                self.z * other.z)
    
    def cross_product(self, other:"Vector"):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)