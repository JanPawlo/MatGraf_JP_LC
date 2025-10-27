from matrix import Matrix4x4

if __name__ == '__main__':
    matrix1 = Matrix4x4([1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 10, 11, 12,
                     13, 14, 15, 16])

    matrix2 = Matrix4x4([1, 2, 1, 2,
                     5, 2, 3, 4,
                     5, 8, 1, 0,
                     10, 1, 3, 2])

    # dodawanie macierzy
    print(matrix1 + matrix1, end='\n\n')

    # mnożenie macierzy
    print(matrix1 * matrix1, end='\n\n')

    # mnożenie skalarne
    print(matrix1 * 5, end='\n\n')

    # sprawdzenie działania equals
    print(matrix1 == matrix1)
    print(matrix1 == (matrix1 * 2))

    # sprawdzenie przemienności mnożenia macierzy
    matrix3 = matrix1 * matrix2
    matrix3_prim = matrix2 * matrix1
    print(matrix3 == matrix3_prim, end='\n\n')

    # mnożenie macierzy
    print(matrix3, end='\n\n')
    print(matrix3_prim, end='\n\n')

    print(matrix1.transpose(), end='\n\n')
