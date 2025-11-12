from matrix import Matrix4x4
from vector import Vector

if __name__ == '__main__':
    matrix1 = Matrix4x4([1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 10, 11, 12,
                     13, 14, 15, 16])

    matrix2 = Matrix4x4([1, 2, 1, 2,
                     5, 2, 3, 4,
                     5, 8, 1, 0,
                     10, 1, 3, 2])

    print("Macierze")
    print(matrix1, end='\n\n')
    print(matrix2, end='\n\n')

    # dodawanie macierzy
    print("Dodawanie")
    print(matrix1 + matrix1, end='\n\n')

    # mnożenie skalarne
    print("Mnożenie przez skalar")
    print(matrix1 * 5, end='\n\n')

    # sprawdzenie działania equals
    print("Equals")
    print("Macierz1 == Macierz1: " + str(matrix1 == matrix1))
    print("Macierz 1 == Macierz1 * 2: " + str(matrix1 == (matrix1 * 2)))

    # mnożenie macierzy
    matrix3 = matrix1 * matrix2
    matrix3_prim = matrix2 * matrix1
    print("Mnożenie macierzy")
    print(matrix3, end='\n\n')
    print(matrix3_prim, end='\n\n')

    # sprawdzenie przemienności mnożenia macierzy
    print("Przemienność mnożenia (m1 * m2 == m2 * m1): " + str(matrix3 == matrix3_prim), end='\n\n')

    # transpozycja macierzy
    print("Transpozycja macierzy")
    print(matrix1.transpose(), end='\n\n')

    # mnozenie przez wektor czyt. uwaga w __mul__
    matrix3 = Matrix4x4([1, 2, 1, 0,
                         2, 1, 2, 0,
                         1, 2, 1, 0,
                         2, 1, 2, 1])
    print("Mnożenie przez wektor")
    print(matrix3 * Vector(1, 2, 3), end='\n\n')

    # rotacja wektora
    print("Rotacja wektora [1, 0, 0, 1] o 90 stopni w osi Y")
    print(Matrix4x4.set_rotation_y(90) * Vector(1, 0, 0), end='\n\n')
