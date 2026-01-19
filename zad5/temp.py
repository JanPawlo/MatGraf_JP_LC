import os
import time
import math
from vector import Vector, degrees_to_radians, find_angle
from line import Line
from cube import Cube

# Konfiguracja wyświetlania
WIDTH = 60
HEIGHT = 30
ASPECT_RATIO = 0.5  # Korekta, ponieważ znaki w konsoli są wyższe niż szersze


class Camera:
    def __init__(self, position: Vector, fov_scale: float = 1.0):
        self.position = position
        self.fov_scale = fov_scale

    def get_ray(self, x_pixel, y_pixel, screen_width, screen_height) -> Line:
        """
        Tworzy promień (Line) biegnący od kamery przez dany piksel ekranu.
        """
        # Normalizacja współrzędnych ekranu do zakresu -1 do 1
        # Uwzględniamy aspect ratio znaków w konsoli
        x_norm = (x_pixel - screen_width / 2) / (screen_width / 2)
        y_norm = (y_pixel - screen_height / 2) / (screen_height / 2) * ASPECT_RATIO

        # Punkt na wirtualnym ekranie (z = 0, kamera jest cofnięta na Z)
        screen_point = Vector(x_norm * 10 * self.fov_scale, y_norm * 10 * self.fov_scale, 0)

        # Wektor kierunkowy promienia
        direction = screen_point - self.position

        # Zwracamy obiekt Line (punkt startowy, wektor kierunkowy)
        return Line(self.position, direction)


def render_scene():
    # 1. Inicjalizacja obiektów
    # Sześcian o środku (0,0,0) i krawędzi 8
    cube = Cube(0, 0, 0, 8)

    # Kamera cofnięta o 20 jednostek na osi Z
    camera = Camera(Vector(0, 0, -20), fov_scale=1.5)

    # Oś obrotu sześcianu (przekątna)
    rotation_axis = Vector(1, 1, 0).normalise()
    angle = 0.0

    while True:
        # Bufor na klatkę obrazu
        output_buffer = []

        # Przygotowanie obrotu (symulacja obrotu obiektu poprzez odwrotny obrót promienia)
        # Dzięki temu możemy używać statycznej definicji Cube (AABB) do kolizji,
        # a wizualnie sześcian będzie się obracał.
        # Kwaterniony są używane wewnątrz metody rotate_point w vector.py

        # Pętla po pikselach (Y, X)
        for y in range(HEIGHT):
            row_str = ""
            for x in range(WIDTH):
                # 1. Pobierz promień z kamery
                ray = camera.get_ray(x, y, WIDTH, HEIGHT)

                # 2. Transformacja promienia do przestrzeni lokalnej sześcianu
                # Zamiast obracać sześcian o kąt A, obracamy punkt i wektor promienia o kąt -A.
                local_ray_origin = ray.point.rotate_point(-angle, rotation_axis)
                local_ray_vector = ray.vector.rotate_point(-angle, rotation_axis)

                local_ray = Line(local_ray_origin, local_ray_vector)

                # 3. Sprawdzenie przecięcia
                # calculate_ray_cross zwraca (punkt, dystans, normalna) lub None
                hit_data = cube.calculate_ray_cross(local_ray)

                if hit_data:
                    point, distance, normal = hit_data

                    # 4. Obliczenie cieniowania
                    # Normalna jest w przestrzeni lokalnej sześcianu. Ponieważ kąt między
                    # wektorem promienia a normalną jest taki sam w obu przestrzeniach,
                    # nie musimy transformować normalnej z powrotem do świata,
                    # by policzyć jasność (o ile używamy local_ray_vector).

                    # Wektor widzenia (od punktu do kamery) to przeciwieństwo wektora promienia
                    view_vector = local_ray_vector * -1.0

                    # Oblicz kąt w stopniach
                    hit_angle = radians_to_degrees(find_angle(normal, view_vector))

                    # Logika znaków (zgodnie z poleceniem)
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

        # Wyświetlanie klatki
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


if __name__ == "__main__":
    try:
        render_scene()
    except KeyboardInterrupt:
        print("\nZakończono renderowanie.")