from quaternion import Quaternion
from vector import Vector

if __name__ == '__main__':
    q1 = Quaternion(3, Vector(1, 2, 3))
    q2 = Quaternion(4, Vector(5, 6, 7))
    p1 = Vector(-1, -1, -1)
    
    print(q1)
    print(q2)
    print(q1 + q2)
    print(q1 - q2)
    print(q1 * q2)
    print(q1 / q2)
    print(q1 * q2 != q2 * q1)
    print(q1 * q2, "|", q2 * q1)
    
    
    print(p1.rotate_point(270, Vector(1, 0, 0)))
    
    print()