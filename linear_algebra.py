class ShapeError(Exception):
    pass


def shape(vector):
    if is_matrix(vector):
        return (len(vector), len(vector[0]))
    else:
        return (len(vector), )


def vector_add(vector1, vector2):
    if not compare_shapes(vector1, vector2):
        raise ShapeError
    else:
        return [sum(values) for values in zip(vector1, vector2)]


def vector_sub(vector1, vector2):
    if not compare_shapes(vector1, vector2):
        raise ShapeError
    else:
        return [item1 - item2 for item1, item2 in zip(vector1, vector2)]


def vector_sum(*args):
    if not compare_shapes(*args):
        raise ShapeError
    else:
        return [sum(values) for values in zip(*args)]


def compare_shapes(*args):
    return len(set([shape(item) for item in args])) == 1


def dot(vector1, vector2):
    if not compare_shapes(vector1, vector2):
        raise ShapeError
    else:
        return sum([value1 * value2 for value1, value2 in zip(vector1, vector2)])


def vector_multiply(vector, scalar):
    return [scalar * factor for factor in vector]


def vector_mean(*args):
    return [sum(value) / len(value) for value in zip(*args)]


def magnitude(vector):
    return sum([value ** 2 for value in vector]) ** (1/2)


def is_matrix(matrix):
    if type(matrix[0]) == list:
        return True
    else:
        return False


def matrix_row(matrix, row_number):
    return matrix[row_number]


def matrix_col(matrix, col_number):
    return [col[col_number] for col in matrix]


def matrix_add(matrix1, matrix2):
    if not compare_shapes(matrix1, matrix2):
        raise ShapeError
    else:
        return [vector_add(vector1, vector2) for vector1, vector2 in zip(matrix1, matrix2)]


def matrix_sub(matrix1, matrix2):
    if not compare_shapes(matrix1, matrix2):
        raise ShapeError
    else:
        return [vector_sub(vector1, vector2) for vector1, vector2 in zip(matrix1, matrix2)]


def matrix_scalar_multiply(matrix, scalar):
        return [vector_multiply(vector, scalar) for vector in matrix]
