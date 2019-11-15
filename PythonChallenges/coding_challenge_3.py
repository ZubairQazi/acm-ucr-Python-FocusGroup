import numpy as np


def main():

    mat1 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    mat2 = np.matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

    mat3 = mat1*mat2
    print(mat3)

    mat4 = np.multiply(mat1, mat2)
    print(mat4)

    mat5 = np.eye(5)
    print(mat5)


if __name__ == "__main__":
    main()


""""""""""
    Please use the following Numpy arrays and
    perform a matrix multiplication, elemental matrix
    multiplication. What's the difference between the two?

    Also create a 3x3 identity matrix!

    mat1 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    mat2 = np.matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
"""""""""""


