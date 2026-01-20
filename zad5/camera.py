from vector import Vector
from line import Line

ASPECT_RATIO = 0.8  # Korekta, ponieważ znaki w konsoli są wyższe niż szersze

class Camera:
    def __init__(self, position: Vector, fov_scale: float = 1.0):
        self.position = position
        self.fov_scale = fov_scale

    def get_ray(self, x_pixel, y_pixel, screen_width, screen_height) -> Line:
        """
        Tworzy promień biegnący od kamery przez dany piksel ekranu.
        """
        # Normalizacja współrzędnych ekranu do zakresu -1 do 1
        # Uwzględniamy aspect ratio znaków w konsoli
        x_norm = (x_pixel - screen_width / 2) / (screen_width / 2)
        y_norm = (y_pixel - screen_height / 2) / (screen_height / 2) * ASPECT_RATIO

        # Punkt na wirtualnym ekranie (z = 0, kamera jest cofnięta na Z)
        screen_point = Vector(x_norm * 10 * self.fov_scale, y_norm * 10 * self.fov_scale, 0)

        # Wektor kierunkowy promienia
        direction = screen_point - self.position

        return Line(self.position, direction)