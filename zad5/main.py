from camera import Camera
from vector import Vector
from cube import Cube

if __name__ == '__main__':
    print('hello world')
    camera1 = Camera(40, 40, Vector(10, 20, -50), Vector(0, 10, 30))
    cube1 = Cube(10, 0, -10, 20)
    camera1.calculate_cube_cross(cube1)
    camera1.print_image()
    # for i in camera1.generate_ray_list(60, 60):
    #     print(i)

