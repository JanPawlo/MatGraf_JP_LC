class Matrix4x4():
    def __init__(self, numbers):
        if len(numbers) == 0:
            self.matrix = []
            for i in range(4):
                self.matrix.append([])
                for j in range(4):
                    self.matrix[i].append(0)
            self.matrix[0][0] = 1
            self.matrix[1][1] = 1
            self.matrix[2][2] = 1
            self.matrix[3][3] = 1

        elif len(numbers) == 16:
            self.matrix = []
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

        elif isinstance(other, Matrix4x4):
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        new_matrix[i * 4 + j] += self.matrix[i][k] * other.matrix[k][j]

        return Matrix4x4(new_matrix)

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
