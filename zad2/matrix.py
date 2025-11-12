import math

from vector import Vector


class Matrix4x4:

    def __init__(self, numbers):
        self.matrix = []
        if len(numbers) == 0:
            for i in range(4):
                self.matrix.append([])
                for j in range(4):
                    self.matrix[i].append(0)
            self.matrix[0][0] = 1
            self.matrix[1][1] = 1
            self.matrix[2][2] = 1
            self.matrix[3][3] = 1

        elif len(numbers) == 16:
            for i in range(4):
                self.matrix.append([])
                for j in range(4):
                    self.matrix[i].append(numbers[i * 4 + j])

        else:
            raise ValueError('Matrix must have 16 elements')

    def __str__(self):
        string = ''
        for i in range(4):
            for j in range(4):
                string += str(self.matrix[i][j]) + '\t'
            string += '\n'
        return string[:-1]

    def __add__(self, other):
        if not isinstance(other, Matrix4x4):
            raise ValueError('Cannot add anything other than Matrix4x4')

        new_matrix = []
        for i in range(16):
            new_matrix.append(0)

        for i in range(4):
            for j in range(4):
                new_matrix[i * 4 + j] = self.matrix[i][j] + other.matrix[i][j]

        return Matrix4x4(new_matrix)

    def __sub__(self, other):
        if not isinstance(other, Matrix4x4):
            raise ValueError('Cannot sub anything other than Matrix4x4')

        new_matrix = []
        for i in range(16):
            new_matrix.append(0)

        for i in range(4):
            for j in range(4):
                new_matrix[i * 4 + j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix4x4(new_matrix)

    def __mul__(self, other):
        new_matrix = []
        for i in range(16):
            new_matrix.append(0)

        if isinstance(other, int) or isinstance(other, float):
            for i in range(4):
                for j in range(4):
                    new_matrix[i * 4 + j] = self.matrix[i][j] * other

            return Matrix4x4(new_matrix)

        elif isinstance(other, Matrix4x4):
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        new_matrix[i * 4 + j] += self.matrix[i][k] * other.matrix[k][j]

            return Matrix4x4(new_matrix)

        elif isinstance(other, Vector):
            # UWAGA - ucinana jest ostatnia wartosc wektora - jest on traktowany jako wektor [x, y, z, 1] na potrzeby obliczen
            new_x = self.matrix[0][0] * other.x + self.matrix[0][1] * other.y + self.matrix[0][2] * other.z + self.matrix[0][3]
            new_y = self.matrix[1][0] * other.x + self.matrix[1][1] * other.y + self.matrix[1][2] * other.z + self.matrix[1][3]
            new_z = self.matrix[2][0] * other.x + self.matrix[2][1] * other.y + self.matrix[2][2] * other.z + self.matrix[2][3]
            #print(self.matrix[3][0] * other.x + self.matrix[3][1] * other.y + self.matrix[3][2] * other.z + self.matrix[3][3])
            return Vector(new_x, new_y, new_z)

        else:
            raise ValueError('Cannot multiply by parsed type')



    def __eq__(self, other):
        if not isinstance(other, Matrix4x4):
            raise ValueError('Cannot compare anything other than Matrix4x4')

        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def transpose(self):
        new_matrix = []
        for i in range(16):
            new_matrix.append(0)

        for i in range(4):
            for j in range(4):
                new_matrix[i * 4 + j] = self.matrix[j][i]

        return Matrix4x4(new_matrix)
    
    
    # a, b - wiersz, kolumna usuwane
    def _macierz_dopelnienia(self, a:int, b:int):
        out_row = 0
        m_out = []
        for i in range(len(self.matrix)):
            if (i == a):
                continue
            else:
                m_out.append([])
            for j in range(len(self.matrix[0])):
                if (j == b):
                    continue
                else:
                    m_out[out_row].append(self.matrix[i][j])
            out_row += 1
        return m_out
                    
    
    def _determinant3x3(self, m:list):
        a, b, c = m[0][0], m[0][1], m[0][2]
        d, e, f = m[1][0], m[1][1], m[1][2]
        g, h, i = m[2][0], m[2][1], m[2][2]
        return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    
    
    # dla macierzy 4x4
    def determinant(self):
        det = self.matrix[0][0] * self._determinant3x3(self._macierz_dopelnienia(0, 0))
        det -= self.matrix[0][1] * self._determinant3x3(self._macierz_dopelnienia(0, 1))
        det += self.matrix[0][2] * self._determinant3x3(self._macierz_dopelnienia(0, 2))
        det -= self.matrix[0][3] * self._determinant3x3(self._macierz_dopelnienia(0, 3))
        
        return det
    
    
    # wyznacznik macierzy dopelnienia ale ze znakiem
    def _getCofactor(self, a:int, b:int):
        det = self._determinant3x3(self._macierz_dopelnienia(a, b))  # Calculate determinant, not the matrix
        
        if ((a+b) % 2 == 0):
            return det * 1
        else:
            return det * -1
    
    def calculateInverse(self):
        determinant = self.determinant()
        
        ## macierz z det==0 nie moze miec odwrotnej
        if ( abs(determinant) < 1e-6 ):
            return False
        
        lista_dopelnien = []
        
        ## policz dopelnienia bez ukladania w macierz
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                lista_dopelnien.append(self._getCofactor(i, j))
        
        ## uluz w macierz uzywajac konstruktora
        m_dopelnien_matrix = Matrix4x4(lista_dopelnien)
        
        ## transpozycja macierzy dopelnien
        m_tran = m_dopelnien_matrix.transpose()
        
        ## podzielenie wszystkiego przez wyznacznik
        inverse_det = 1.0 / determinant
        
        for i in range(len(m_tran.matrix)):
            for j in range(len(m_tran.matrix[0])):
                m_tran.matrix[i][j] = m_tran.matrix[i][j] * inverse_det
        
        return m_tran
    
    
    @staticmethod
    def set_scale(vector):
        new_matrix = Matrix4x4([])
        new_matrix.matrix[0][0] = vector[0]
        new_matrix.matrix[1][1] = vector[1]
        new_matrix.matrix[2][2] = vector[2]

        return new_matrix

    @staticmethod
    def set_uniform_scale(factor):
        new_matrix = Matrix4x4([])
        new_matrix.matrix[0][0] = factor
        new_matrix.matrix[1][1] = factor
        new_matrix.matrix[2][2] = factor

        return new_matrix

    @staticmethod
    def set_rotation_axis(axis: 'Vector', angle):
        # angle jest w stopniach
        if not isinstance(axis, Vector):
            raise ValueError('Axis must be of type Vector')
        if not (isinstance(angle, float) or isinstance(angle, int)):
            raise ValueError('Axis must be of type float or int')

        u = axis.normalise()
        matrix = Matrix4x4([])

        sin_angle = math.sin(math.pi * angle / 180.0)
        cos_angle = math.cos(math.pi * angle / 180.0)

        matrix.matrix[0][0] = u.x * u.x + cos_angle * (1 - u.x * u.x)
        matrix.matrix[1][0] = u.x * u.y * (1 - cos_angle) - sin_angle * u.z
        matrix.matrix[2][0] = u.x * u.x * (1 - cos_angle) + sin_angle * u.y

        matrix.matrix[0][1] = u.x * u.y * (1 - cos_angle) + sin_angle * u.z
        matrix.matrix[1][1] = u.y * u.y + cos_angle * (1 - u.y * u.y)
        matrix.matrix[2][1] = u.y * u.z * (1 - cos_angle) - sin_angle * u.x

        matrix.matrix[0][2] = u.x * u.z * (1 - cos_angle) - sin_angle * u.y
        matrix.matrix[1][2] = u.y * u.z * (1 - cos_angle) + sin_angle * u.x
        matrix.matrix[2][2] = u.z * u.z + cos_angle * (1 - u.z * u.z)

        return matrix

    @staticmethod
    def set_rotation_x(angle):
        if not (isinstance(angle, float) or isinstance(angle, int)):
            raise ValueError('Axis must be of type float or int')

        matrix = Matrix4x4([])
        matrix.matrix[1][1] = math.cos(math.pi * angle / 180.0)
        matrix.matrix[1][2] = math.sin(math.pi * angle / 180.0)

        matrix.matrix[2][1] = -matrix.matrix[1][2]
        matrix.matrix[2][2] = -matrix.matrix[1][1]

        return matrix

    @staticmethod
    def set_rotation_y(angle):
        if not (isinstance(angle, float) or isinstance(angle, int)):
            raise ValueError('Axis must be of type float or int')

        matrix = Matrix4x4([])
        matrix.matrix[0][0] = math.cos(math.pi * angle / 180.0)
        matrix.matrix[0][2] = -math.sin(math.pi * angle / 180.0)

        matrix.matrix[2][0] = -matrix.matrix[0][2]
        matrix.matrix[2][2] = matrix.matrix[0][0]

        return matrix

    @staticmethod
    def set_rotation_z(angle):
        if not (isinstance(angle, float) or isinstance(angle, int)):
            raise ValueError('Axis must be of type float or int')

        matrix = Matrix4x4([])
        matrix.matrix[0][0] = math.cos(math.pi * angle / 180.0)
        matrix.matrix[0][1] = math.sin(math.pi * angle / 180.0)

        matrix.matrix[1][0] = -matrix.matrix[0][1]
        matrix.matrix[1][1] = matrix.matrix[0][0]

        return matrix
    
    
