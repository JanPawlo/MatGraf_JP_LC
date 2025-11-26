from vector import Vector


class Plane:
    
    
    # wejscie: wspolczynniki rownania plaszczyzny
    # ax + by + cz = d
    
    # zapis wewnetrzny: normalna i punkt plaszczyzny
    def __init__(self, a, b, c, d):
        self.normal = Vector(a, b, c)
        if (a != 0):
            self.point = Vector(d/a, 0, 0)
        elif (b != 0):
            self.point = Vector(0, d/b, 0)
        elif (c != 0):
            self.point = Vector(0, 0, d/c)
        else:
            raise ValueError("Plaszczyzna 0,0,0 to zadna plaszczyzna!")
        
        
    
    

        
        