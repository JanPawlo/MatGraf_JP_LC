from vector import Vector


class Plane:
    
    
    # wejscie: wspolczynniki rownania plaszczyzny
    # ax + by + cz - d = 0
    
    # zapis wewnetrzny: wlasciwie ten "normal" to zadna normalna
    def __init__(self, a, b, c, d):
        self.normal = Vector(a, b, c)
        self.d = d


    def contains_point(self, P, eps=1e-9):
        return abs(self.normal.dot_product(P) + self.d) < eps

        
    

        
        