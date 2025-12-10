from vector import Vector
from plane import Plane
from line import Line
import math
from vector import find_angle

def intersection_line_plane(line, plane):
    
    p0, v = line.point, line.vector
    n, d = plane.normal, plane.d
    
    n_dot_v = n.dot_product(v)
    
    # czy "prawie że rowne" 0?
    if abs(n_dot_v) < 1e-10:
        if abs(n.dot_product(p0) - d) < 1e-10:
            return "linia lezy w plaszczyznie"
        else:
            return "linia rownolegla, poza plaszczyzna, brak przeciecia"
        
        
    t = (-d - n.dot_product(p0)) / n_dot_v
    
    return p0 + (v * t)
    

def angle_line_plane(line, plane):
    

    v = line.vector
    n = plane.normal
    
    # Iloczyn skalarny v·n
    v_dot_n = v.dot_product(n)
    
    # Długości wektorów
    norm_v = v.length()
    norm_n = n.length()
    
    # sin(φ) = |v·n| / (|v| * |n|)
    sin_phi = abs(v_dot_n) / (norm_v * norm_n)

    # Kąt między prostą a płaszczyzną
    phi_rad = math.asin(sin_phi)
    phi_deg = math.degrees(phi_rad)
    
    return phi_deg


def intersection_plane_plane(plane1, plane2):
    n1 = plane1.normal
    n2 = plane2.normal
    
    # w ktorym kierunku bedzie prosta (kolejnosc n'ow wplywa na wynik)
    direction = n1.cross_product(n2)
    
    # czy plaszczyzny sa rownolegle
    if direction.length() < 1e-10:
        return None # zwracamy none i nie przejmujemy sie zadnymi przypadkami
    
    a1, b1, c1 = n1.x, n1.y, n1.z
    a2, b2, c2 = n2.x, n2.y, n2.z
    d1 = plane1.d
    d2 = plane2.d
    
    #x=0
    det_x = b1 * c2 - b2 * c1
    if abs(det_x) > 1e-8:
       y = (c2 * (-d1) - c1 * (-d2)) / det_x
       z = (b1 * (-d2) - b2 * (-d1)) / det_x
       return Line(Vector(0, y, z), direction)
   
    #y=0
    det_y = a1 * c2 - a2 * c1
    if abs(det_y) > 1e-8:
        x = (c2 * (-d1) - c1 * (-d2)) / det_y
        z = (a1 * (-d2) - a2 * (-d1)) / det_y
        return Line(Vector(x, 0, z), direction)
    
    #z=0
    det_z = a1 * b2 - a2 * b1
    if abs(det_z) > 1e-8:
        x = (b2 * (-d1) - b1 * (-d2)) / det_z
        y = (a1 * (-d2) - a2 * (-d1)) / det_z
        return Line(Vector(x, y, 0), direction)
    
    return None

def angle_plane_plane(plane1, plane2):
    n1 = plane1.normal
    n2 = plane2.normal
    
    # Iloczyn skalarny
    dot_product = n1.dot_product(n2)
    
    # Długości wektorów
    norm1 = n1.length()
    norm2 = n2.length()
    
    
    # cos(θ) = |n1·n2| / (|n1|·|n2|)
    cos_theta = abs(dot_product) / (norm1 * norm2)
    
    theta_rad = math.acos(cos_theta)
    theta_deg = math.degrees(theta_rad)
        
    return theta_deg
    