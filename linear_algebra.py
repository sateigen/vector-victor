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
    return [sum(values) for values in zip(*args)]
