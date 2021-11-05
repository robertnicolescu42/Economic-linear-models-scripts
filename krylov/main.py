import numpy as np
from fractions import Fraction

from numpy import polydiv


def inv(matrix):
    return np.linalg.inv(matrix)


def multiply_matrix_vector(matrix, vector):
    return matrix.dot(vector)


def print_matrix_as_fraction(matrix):
    new_matrix = []
    for line in matrix:
        array_line = []
        for elem in line:
            elem = Fraction(elem).limit_denominator()  # turn numbers into fractions
            array_line.append(str(elem))
        new_matrix.append(array_line)
    print(new_matrix)


def print_arr_as_fraction(arr):
    new_matrix = []
    for elem in range(arr.size):
        new_matrix.append(str(Fraction(arr[elem]).limit_denominator()))

    print(new_matrix)


def krylov(matrix, y):
    iterations = matrix[0].size
    print("A = ")
    print(matrix, end=" ")
    print("\n")

    print("y^0 = ")
    print(y, end=" ")
    print("\n")

    prev_y = y

    array_of_y = []
    for i in range(iterations):
        current_y = multiply_matrix_vector(matrix, prev_y)
        print("iteration " + str(i + 1) + ": y^(" + str(i + 1) + ")= A * y^(" + str(i) + ") = ", end="")
        print(current_y)
        if i != iterations - 1:
            prev_y = current_y
            array_of_y.append(current_y)
    print("\n")

    print("eigenvector y^(" + str(iterations) + "): ")
    print(current_y)

    new_matrix = np.zeros((iterations, iterations))
    for i in range(matrix[0].size):
        current_array = array_of_y[i - 1]
        for j in range(matrix[0].size):
            if i != matrix[0].size - 1:
                new_matrix[i][j] = current_array[j]
            else:
                new_matrix[i][j] = y[j]
    new_matrix = new_matrix.transpose()
    print("new matrix:")
    print(new_matrix)
    print("array of y:")
    print(array_of_y)

    # reversing the signs in y
    modified_y = np.zeros((iterations, 1))
    for i in range(current_y.size):
        modified_y[i] = -current_y[i]

    print("modified y:")
    print(modified_y)

    solutions = np.linalg.solve(new_matrix, modified_y)
    print("solutions/eigenvalues: ")
    print(solutions)

    proper_solutions = np.append(1, solutions)
    polynomial = np.poly1d(np.squeeze(proper_solutions))
    print("polynomial: ")
    print(polynomial)

    print("polynomial solutions:")
    poly_solutions = np.roots(polynomial)
    print(poly_solutions)

    for i in range(poly_solutions.size):
        c1 = (1, -poly_solutions[i])
        print("iteration " + str(i + 1) + " for lambda: " + str(np.poly1d(c1)))
        print("---------------")
        divided, division_remainder = polydiv(polynomial, c1)
        print(divided)


if __name__ == '__main__':
    # 3x3 example /67 Curs 3
    A = np.array([[-1, 2, 2],
                  [2, 2, 2],
                  [-3, -6, -6]])

    B = np.array([0, 1, 1])
    krylov(A, B)
