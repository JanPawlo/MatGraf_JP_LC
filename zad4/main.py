from math import sqrt
from sphere import Sphere
from vector import Vector
from line import Line, Segment
from plane import Plane
from operation_but_better import intersection_line_plane, angle_line_plane, intersection_plane_plane, angle_plane_plane

if __name__ == '__main__':
    # zle przepisalem linie wczesniej x d
    line1 = Line(Vector(-2,4, 0), Vector(3,1, 5))
    line2 = Line(Vector(-2,4, 0), Vector(1,-5, 3))
    print("Zadanie 1:")
    print("pkt. przeciecia prostej z prosta:",
          line1.line_and_line_cross(line2))

    print("Zadanie 2:")
    print("kat. miedzy prosta z prosta:",
          line1.angle(line2))
    
    # zadanie 3:
    linia3 = Line(Vector(-2, 2, -1), Vector(3, -1, 2))
    plaszczyzna3 = Plane(2, 3, 3, -8)
    print("Zadanie 3:")
    print("pkt. przeciecia prostej z plaszczyzna:",
          intersection_line_plane(linia3, plaszczyzna3))
    
    # zadanie 4:
    print("Zadanie 4:")
    print("kat przeciecia prostej z plaszczyzna:",
          angle_line_plane(linia3, plaszczyzna3))

    # zadanie 5:
    pl5a = Plane(2, -1, 1, -8)
    pl5b = Plane(4, 3, 1, 14)
    
        
    print("Zadanie 5:")
    print("prosta przeciecia plaszczyzn:",
          intersection_plane_plane(pl5a, pl5b))
    
    print("Zadanie 6:")
    print("kat przeciecia plaszczyzn:", 
          angle_plane_plane(pl5a, pl5b))

    segment1 = Segment(Vector(5, 5, 4), Vector(10, 10, 6))
    segment2 = Segment(Vector(5, 5, 5), Vector(10, 10, 3))

    print("Zadanie 7:")
    print("pkt. przeciecia odcinkow:",
          segment1.segment_and_segment_cross(segment2))

    sphere1 = Sphere(sqrt(26), Vector(0, 0, 0))
    line3 = Line(Vector(3, 1, 2), Vector(5, 3, -4) - Vector(3, -1, -2))
    point1, point2 = sphere1.sphere_and_line_cross(line3)
    print("Zadanie 8:")
    print("pkt. przeciecia sfery i prostej: " + str(point1) + " " + str(point2))