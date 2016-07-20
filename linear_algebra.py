class ShapeError(Exception):
    pass


def shape(vector):
    return(len(vector), )


def vector_add(vector1, vector2):
    if shape(vector1) != shape(vector2):
        raise ShapeError
    else:
        return [sum(values) for values in zip(vector1, vector2)]


def vector_sub(vector1, vector2):
    if shape(vector1) != shape(vector2):
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
    if shape(vector1) != shape(vector2):
        raise ShapeError
    else:
        return sum([value1 * value2 for value1, value2 in zip(vector1, vector2)])


def vector_multiply(vector, number):
    return [number * factor for factor in vector]
        #
        # def test_vector_multiply():
        #     """
        #     [a b]  *  Z     = [a*Z b*Z]
        #     Vector * Scalar = Vector
        #     """
        #     assert vector_multiply(v, 0.5) == [0.5, 1.5, 0]
        #     assert vector_multiply(m, 2) == [6, 8]
