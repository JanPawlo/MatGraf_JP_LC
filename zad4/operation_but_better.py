from vector import Vector
from plane import Plane



def intersection_line_plane(line, plane):
    
    p0, v = line.point, line.vector
    n, d = plane.normal, plane.d
    
    n_dot_v = n.dot_product(v)
    
    # czy "rowne" 0?
    if abs(n_dot_v) < 1e-10:
        if abs(n.dot_product(p0) - d) < 1e-10:
            return "linia lezy w plaszczyznie"
        else:
            return "linia rownolegla, poza plaszczyzna, brak przeciecia"
        
        
    t = (d - n.dot_product(p0)) / n_dot_v
    
    return p0 + (v * t)
    

