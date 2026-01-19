from camera import Camera
from vector import Vector
from cube import Cube

if __name__ == '__main__':
    print('hello world')
    camera1 = Camera(60, 60, Vector(0, 0, 0), Vector(10, 0, 0), 40, 20)
    cube1 = Cube(15, 0, 0, 10)
    camera1.calculate_cube_cross(cube1)
    camera1.print_image()
    camera1.rotate(45, Vector(0, 1, 0), Vector(15, 0, 0))
    camera1.calculate_cube_cross(cube1)
    camera1.print_image()
    # for i in camera1.generate_ray_list(60, 60):
    #     print(i)

