from matrix import Matrix4x4


m1 = Matrix4x4([1, 2, 3, 0,
                0, 1, 4, 0,
                5, 6, 0, 0,
                0, 0, 0, 1])

m2 = Matrix4x4([22, -6, -26, 0,
                -17, 5, 20, 0 ,
                -1, 0, 2, -1,
                4, -1, -5, 3])



def test_inverse_confirm():
    # print(m1.is_inverse(m2))
    # print(m1.is_inverse(m1.invert()))
    print(m1.calculateInverse())
    

test_inverse_confirm()