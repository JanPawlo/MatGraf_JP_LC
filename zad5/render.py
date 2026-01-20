import os
import time
import math

from vector import Vector, find_angle
from line import Line
from cube import Cube
from camera import Camera

# globalne ustawienie wyświetlania
WIDTH = 60
HEIGHT = 30

def render_scene():
    cube = Cube(0, 0, 0, 8)

    camera = Camera(Vector(0, 0, -20), fov_scale=1.5)

    # Oś obrotu sześcianu
    rotation_axis = Vector(1, 1, 0).normalise()
    angle = 0.0

    while True:
        output_buffer = []

        # Przygotowanie obrotu (symulacja obrotu obiektu poprzez odwrotny obrót promienia)

        # Pętla po pikselach (Y, X)
        for y in range(HEIGHT):
            row_str = ""
            for x in range(WIDTH):
                # dla każdego ray'a
                ray = camera.get_ray(x, y, WIDTH, HEIGHT)

                # zamiast obracać sześcian o kąt A, obracamy punkt i wektor promienia o kąt -A.
                local_ray_origin = ray.point.rotate_point(-angle, rotation_axis)
                local_ray_vector = ray.vector.rotate_point(-angle, rotation_axis)

                local_ray = Line(local_ray_origin, local_ray_vector)

                hit_data = cube.calculate_ray_cross(local_ray)

                if hit_data:
                    point, distance, normal = hit_data

                    # Obliczenie cieniowania

                    # Wektor widzenia (od punktu do kamery) to przeciwieństwo wektora promienia
                    view_vector = local_ray_vector * -1.0

                    hit_angle = radians_to_degrees(find_angle(normal, view_vector))

                    if hit_angle < 45:
                        pixel_char = "@"  # Ścianka skierowana prosto do nas
                    elif hit_angle < 60:
                        pixel_char = "%"
                    elif hit_angle < 75:
                        pixel_char = "#"
                    else:
                        pixel_char = "."  # Krawędzie/duży kąt
                else:
                    pixel_char = " "  # Tło

                row_str += pixel_char
            output_buffer.append(row_str)


        clear_screen()
        print("\n".join(output_buffer))
        print(f"Kąt obrotu: {angle:.1f}° | Oś: {rotation_axis}")

        # Aktualizacja animacji
        angle += 5.0
        if angle >= 360:
            angle = 0

        time.sleep(0.05)


def radians_to_degrees(radians):
    return radians * 180 / math.pi


def clear_screen():
    # Komenda czyszczenia ekranu zależna od systemu
    os.system('cls' if os.name == 'nt' else 'clear')
