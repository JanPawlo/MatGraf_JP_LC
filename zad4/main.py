from vector import Vector
from line import Line, Segment

if __name__ == '__main__':
    # zle przepisalem linie wczesniej x d
    line1 = Line(Vector(-2,4, 0), Vector(3,1, 5))
    line2 = Line(Vector(-2,4, 0), Vector(1,-5, 3))
    t1, t2 = line1.line_and_line_cross(line2)
    print(line1.angle(line2))
    print(t1, t2)
    print(line1.calculate_point(t1))
    print(line2.calculate_point(t2))

    segment1 = Segment(Vector(5, 5, 4), Vector(10, 10, 6))
    segment2 = Segment(Vector(5, 5, 5), Vector(10, 10, 3))
    segment1.segment_and_segment_cross(segment2)
