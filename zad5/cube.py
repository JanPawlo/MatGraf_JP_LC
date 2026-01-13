from vector import Vector
from line import Line
from plane import Plane


class Cube():
    
    # x,y,z - srodek cube'a
    # edge - dlugosc krawedzi
    def __init__(self, x, y, z, edge):
        
        self.center = Vector(x, y, z)
        self.edge = edge
        
        # dwa punkty w postaci wektorowej na przeciwnych wierzcholkach cube'a
        self.min_point = Vector(x-(edge/2), y-(edge/2), z-(edge/2))
        self.max_point = Vector(x+(edge/2), y+(edge/2), z+(edge/2))
        
        # stworz 6 plane'ow: 
        self.planes = [
            Plane(1, 0, 0, x + edge/2), 
            Plane(-1, 0, 0, -(x - edge/2)),  
            
            Plane(0, 1, 0, y + edge/2),  
            Plane(0, -1, 0, -(y - edge/2)),  
            
            Plane(0, 0, 1, z + edge/2),  
            Plane(0, 0, -1, -(z - edge/2))
            ]
        
    # czy punkt jest w cub'ie wlaczajac w to krawedzie
    def contains_point(self, point: Vector, eps=1e-9):
        return (self.min_point.x - eps <= point.x <= self.max_point.x + eps and
                self.min_point.y - eps <= point.y <= self.max_point.y + eps and
                self.min_point.z - eps <= point.z <= self.max_point.z + eps)




    def calculate_ray_cross(self, line: "Line"):
        # pomysl 1: sprawdz czy linia "wkracza" w sfere dookola srodka cube'a
        # sfera ta ma promien = sqrt(edge/sqrt(2))
        # potencjalnie moze to pomoc w odrzuceniu wielu zbednych lini (kilkanascie %)
        
        # pomysl 2:stworzyc powierzchnie dla kazdej sciany cube'a, sprawdzic kolizje
        # i dodac dodatkowe sprawdzenie granicy???
        
        
        intersections = []   
        for i in range(len(self.planes)):
            point, t = self.planes[i].intersect_line(line)
            
            if point is not None:
                if self.contains_point(point):
                    distance = t
                    intersections.append((point, distance, self.planes[i].normal))
        

        # zwroc tylko najblizsze przeciecie
        if not intersections:
            return None  

        # posortuj wedlug dlugosci (drugi element)
        intersections.sort(key=lambda x: x[1])
        
        return intersections[0]
    
    
    