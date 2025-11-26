from operation_but_better import intersection_line_plane
from vector import Vector
from plane import Plane
from line import Line


def test_0():
    
    l1 = Line(Vector(0,0,0), Vector(1,1,1))
    p1 = Plane(1, 1, 1, 3)
    print(intersection_line_plane(l1, p1))
    
    
    
    
test_0()