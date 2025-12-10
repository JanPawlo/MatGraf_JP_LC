from camera import Camera
from vector import Vector

if __name__ == '__main__':
    print('hello world')
    camera1 = Camera(100, 100, Vector(0, 0, -50), Vector(0, 0, 45))
    for i in camera1.generate_ray_list(60, 60):
        print(i)

