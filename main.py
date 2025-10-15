import math

from vector import Vector
from vector import find_angle

def radians_to_degrees(radians:float):
    return radians * 180 / math.pi


if __name__ == "__main__":
    
    v1 = Vector(4, 5, 1)
    print(v1)
    v2 = Vector(4, 1, 3)
    print(v2)
    print(v1 + v2)
    print(v2 + v1)
    print((v1 + v2) == (v2 + v1))
    print(v1 / 4)
    angle = find_angle(Vector(0, 3, 0), Vector(5, 5, 0))
    print(f"kat w radianach: {angle}")
    print(f"kat w stopniach: {radians_to_degrees(angle)}")
    v3 = v1.cross_product(v2)
    print(v3)
    angle = find_angle(v1, v3)
    print(f"kat w radianach: {angle}")
    print(f"kat w stopniach: {radians_to_degrees(angle)}")
    angle = find_angle(v2, v3)
    print(f"kat w radianach: {angle}")
    print(f"kat w stopniach: {radians_to_degrees(angle)}")
    v4 = v3.normalise()
    print(v4)
    print(v4.length())


