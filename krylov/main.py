import numpy as np
from fractions import Fraction


def inv(matrix):
    return np.linalg.inv(matrix)


def multiply_matrix_vector(matrix, vector):
    return matrix.dot(vector)


def direct_power_method(matrix, y, iterations):
    print("A = ")
    print(matrix, end=" ")
    print("\n")

    print("y^0 = ")
    print(y, end=" ")
    print("\n")

    prev_y = y

    for i in range(iterations):
        current_y = multiply_matrix_vector(matrix, prev_y)
        print("iteration " + str(i + 1) + ": y^(" + str(i + 1) + ")= A * y^(" + str(i) + ") = ", end="")
        print(current_y)
        if i != iterations - 1:
            prev_y = current_y
    print("\n")

    lambda_array = []
    for line in range(current_y.size):
        # print(current_y[line])
        lmb_1 = current_y[line] / prev_y[line]  # y(last iteration)/y(second to last iteration)
        lambda_array.append(round(lmb_1, 6))

    print("lambda array: ")
    print(lambda_array)
    print("\n")

    sum_of_lmb = 0
    for value in lambda_array:
        sum_of_lmb = sum_of_lmb + value

    eigenvalue = 1 * sum_of_lmb / current_y.size
    print("eigenvalue: " + str(round(eigenvalue, 6)))
    print("rounded eigenvalue: " + str(round(eigenvalue, 0)) + "\n")

    print("eigenvector y^(" + str(iterations) + "): ")
    print(current_y)


def inverse_power_method(matrix, y, iterations):
    matrix = inv(matrix)
    print("A = ")
    print_matrix_as_fraction(matrix)
    print("\n")

    print("y^0 = ")
    print(y, end=" ")
    print("\n")

    prev_y = y

    for i in range(iterations):
        current_y = multiply_matrix_vector(matrix, prev_y)
        # current_y = np.around(current_y, 10)

        print("iteration " + str(i + 1) + ": y^(" + str(i + 1) + ")= A * y^(" + str(i) + ") = ", end=" ")
        print_arr_as_fraction(current_y)
        if i != iterations - 1:
            prev_y = current_y
    print("\n")

    lambda_array = []
    for line in range(current_y.size):
        # print(current_y[line])
        lmb_1 = current_y[line] / prev_y[line]  # y(last iteration)/y(second to last iteration)
        lambda_array.append(round(lmb_1, 6))

    print("lambda array: ")
    print(lambda_array)
    print("\n")

    sum_of_lmb = 0
    for value in lambda_array:
        sum_of_lmb = sum_of_lmb + value

    eigenvalue = 1 * sum_of_lmb / current_y.size
    print("eigenvalue: " + str(round(eigenvalue, 6)))
    print("rounded eigenvalue: " + str(round(eigenvalue, 0)) + "\n")

    print("eigenvector y^(" + str(iterations) + "): ")
    print(current_y)

    # print("as fractions: ")
    # for line in matrix:
    #     for elem in line:
    #         print("normal elem: " + str(elem))
    #         elem = Fraction(elem).limit_denominator()  # turn numbers into fractions
    #         print(elem)


def print_matrix_as_fraction(matrix):
    # matrix_size = len(matrix[0])
    new_matrix = []
    for line in matrix:
        array_line = []
        for elem in line:
            elem = Fraction(elem).limit_denominator()  # turn numbers into fractions
            # print(elem)
            array_line.append(str(elem))
        new_matrix.append(array_line)
    print(new_matrix)


def print_arr_as_fraction(arr):
    matrix_size = arr.size
    new_matrix = []
    for elem in range(arr.size):
        new_matrix.append(str(Fraction(arr[elem]).limit_denominator()))

    print(new_matrix)
    # print(multiply_matrix_vector(new_matrix,['q1', 'q2', 'q3']))


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
        # print("current array: ")
        # print(current_array)
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
    print("solutions: ")
    print(solutions)


if __name__ == '__main__':
    # 3x3 example /67 Curs 3
    A = np.array([[-1, 2, 2],
                  [2, 2, 2],
                  [-3, -6, -6]])

    B = np.array([0, 1, 1])
    krylov(A, B)
