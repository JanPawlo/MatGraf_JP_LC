from vector import Vector
from line import Line
from cube import Cube
from colorama import init, Back, Style, Fore
init()

class Camera(object):
    def __init__(self, width, height, starting_point: "Vector", distance: "Vector", x_pixels, y_pixels):
        self.width = width
        self.height = height
        self.point = starting_point
        self.distance = distance
        self.rays = []
        self.image = []
        self.x_pixels = x_pixels
        self.y_pixels = y_pixels

    def generate_ray(self, x_scalar, y_scalar):
        if x_scalar > 1 or x_scalar < -1:
            raise ValueError("x_scalar must be between -1 and 1")
        if y_scalar > 1 or y_scalar < -1:
            raise ValueError("y_scalar must be between -1 and 1")

        direction_on_plane = Vector(
            (self.width / 2) * x_scalar,
            (self.height / 2) * y_scalar,
            0
        )
        ray_direction = self.distance + direction_on_plane

        ray = Line(self.point, ray_direction)
        return ray

    def generate_ray_list(self):
        self.rays = []

        up_guide = Vector(0, 1, 0)

        # Kierunek patrzenia (znormalizowany)
        forward = self.distance.normalise()
        # Wektor w prawo (iloczyn wektorowy forward i up)
        right = forward.cross_product(up_guide).normalise()
        # Rzeczywisty wektor w górę (prostopadły do forward i right)
        up = right.cross_product(forward).normalise()

        # Obliczamy lewy górny róg ekranu
        # Środek ekranu to self.point + self.distance
        screen_center = self.point + self.distance

        # Przesunięcie do lewego górnego rogu:
        # środek - (width/2 * right) + (height/2 * up)
        top_left = screen_center - (right * (self.width / 2)) + (up * (self.height / 2))

        # Rozmiar pojedynczego piksela w jednostkach świata
        pixel_w = self.width / self.x_pixels
        pixel_h = self.height / self.y_pixels

        for y in range(self.y_pixels):
            row = []
            for x in range(self.x_pixels):
                # Wyznaczamy punkt na ekranie dla piksela (x, y)
                # Dodajemy 0.5, aby promień przechodził przez środek piksela
                world_x = right * ((x + 0.5) * pixel_w)
                world_y = up * ((y + 0.5) * pixel_h)

                pixel_point = top_left + world_x -world_y

                # Kierunek promienia: od kamery do punktu na ekranie
                ray_direction = pixel_point - self.point.normalise()

                row.append(Line(self.point, ray_direction + self.distance))
            self.rays.append(row)

    def calculate_cube_cross(self, cube: "Cube"):
        self.generate_ray_list()
        self.image = [] 
        min_dist = float('inf')
        max_dist = 0
        distances = []
        for row in self.rays:
            for ray in row:
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
            if i % self.x_pixels == 0:
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

    def rotate(self, angle, axis, pivot):
        self.point = (self.point - pivot).rotate_point(angle, axis) + pivot
        self.distance = (self.distance - pivot).rotate_point(angle, axis) + pivot
        print(self.point, self.distance)
