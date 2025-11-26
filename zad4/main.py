from vector import Vector
from line import Line

if __name__ == '__main__':
    line1 = Line(Vector(2,4, 0), Vector(3,1, 5))
    line2 = Line(Vector(-2,4, 0), Vector(1,-5, 3))
    t1, t2 = line1.line_and_line_cross(line2)
    print(line1.angle(line2))
    print(t1, t2)
    print(line1.calculate_point(t1))
    print(line2.calculate_point(t2))
