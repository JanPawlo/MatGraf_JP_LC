from math import sqrt
from sphere import Sphere
from vector import Vector
from line import Line, Segment

if __name__ == '__main__':
    # zle przepisalem linie wczesniej x d
    line1 = Line(Vector(-2,4, 0), Vector(3,1, 5))
    line2 = Line(Vector(-2,4, 0), Vector(1,-5, 3))
    print(line1.line_and_line_cross(line2))

    segment1 = Segment(Vector(5, 5, 4), Vector(10, 10, 6))
    segment2 = Segment(Vector(5, 5, 5), Vector(10, 10, 3))
    print(segment1.segment_and_segment_cross(segment2))

    sphere1 = Sphere(sqrt(26), Vector(0, 0, 0))
    line3 = Line(Vector(3, 1, 2), Vector(5, 3, -4) - Vector(3, -1, -2))
    point1, point2 = sphere1.sphere_and_line_cross(line3)
    print(str(point1) + " " + str(point2))

    line4 = Line(Vector(0, 0, -5), Vector(0, 0, 1))
    sphere2 = Sphere(2, Vector(0, 0, 0))

    point1, point2 = sphere2.sphere_and_line_cross(line4)
    print(str(point1) + " " + str(point2))
