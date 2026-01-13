from vector import Vector
from line import Line
from cube import Cube
from colorama import init, Back, Style, Fore
init()

class Camera(object):
    def __init__(self, width, height, starting_point: "Vector", distance: "Vector"):
        self.width = width
        self.height = height
        self.point = starting_point
        self.distance = distance
        self.rays = []
        self.image = []

    def generate_ray(self, x_scalar, y_scalar):
        if x_scalar > 1 or x_scalar < -1:
            raise ValueError("x_scalar must be between -1 and 1")
        if y_scalar > 1 or y_scalar < -1:
            raise ValueError("y_scalar must be between -1 and 1")
        ray = Line(self.point, self.distance + Vector((self.width / 2) * x_scalar, (self.height / 2) * y_scalar, 0))
        return ray

    def generate_ray_list(self, x_pixels=60, y_pixels=60):
        self.rays = []
        # idk co tu sie dziele temporarily robie fix:
        x_pixels = self.width
        y_pixels = self.height
        for x in range(x_pixels):
            for y in range(y_pixels):
                self.rays.append(self.generate_ray(1 - x / (x_pixels / 2) , 1 - y / (y_pixels / 2 )))
        return self.rays.copy()

    def calculate_cube_cross(self, cube: "Cube"):
        self.generate_ray_list()
        self.image = [] 
        min_dist = float('inf')
        max_dist = 0
        distances = []
        for ray in self.rays:
            result = cube.calculate_ray_cross(ray)
            if result is None:
                distances.append(None)
            else:
                point, distance, normal = result
                distances.append(distance)
                min_dist = min(min_dist, distance)
                max_dist = max(max_dist, distance)
            
            # if no hits detected, just in case
            if min_dist == float('inf'):
               min_dist = 0
               max_dist = 1
              
        self.image = distances
        self.min_dist = min_dist
        if (max_dist < min_dist):
            max_dist = min_dist + 1
        self.max_dist = max_dist 
        print(max_dist, min_dist)

    def print_image(self):
        for i in range(len(self.image)):
            if i % self.width == 0:
                print(Style.RESET_ALL)
            
            if self.image[i] is None:
                print(".", end="")
            else:
                # min-max brightness
                brightness = 1.0 - ((self.image[i] - self.min_dist) / 
                                   (self.max_dist - self.min_dist + 1e-9))
                brightness = max(0.1, min(1.0, brightness))
                
                # colorama
                if brightness > 0.9:
                    color = Fore.WHITE
                elif brightness > 0.7:
                    color = Fore.LIGHTWHITE_EX  
                elif brightness > 0.5:
                    color = Fore.LIGHTBLACK_EX
                elif brightness > 0.3:
                    color = Fore.BLACK
                else:
                    color = Fore.RED #legacy i guess
                
                print(color + "#" + Style.RESET_ALL, end="")
        print()
