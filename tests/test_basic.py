import turning_function

import copy
import random

import pytest
from itertools import product

square = [[0,0], [1,0], [1,1], [0, 1]]

def random_shape(n: int):

    if n < 3 or n > turning_function.max_points:
        raise ValueError(f"The number of points is too large: {n}.")

    return [(random.random(), random.random()) for _ in range(n)]

def test_non_zero():

    b = copy.deepcopy(square)
    b[0][0] = -1

    m = turning_function.distance(square, b)

    # print('m: ', m)

    assert abs(m - 0.6144398026382778) < .00000001

@pytest.mark.parametrize("num_shifts", range(1,4))
def test_rotation_invariance1(num_shifts):

    b = copy.deepcopy(square)

    for _ in range(num_shifts):
        b = [b.pop()] + b

    m = turning_function.distance(square, b)

    assert m == 0

@pytest.mark.parametrize("scale", [0.5, 1., 2., 100000.])
def test_scale_invariance1(scale):

    b = copy.deepcopy(square)

    b = [(x*scale,y*scale) for x, y in b]

    # b = [b.pop()] + b
    # b = [b.pop()] + b

    m = turning_function.distance(square, b)

    assert m == 0

@pytest.mark.parametrize("tx,ty", product(range(-1,2),range(-1,2)))
def test_translation_invariance1(tx, ty):

    b = copy.deepcopy(square)

    b = [(x+tx,y+ty) for x, y in b]

    # b = [b.pop()] + b
    # b = [b.pop()] + b

    m = turning_function.distance(square, b)

    assert m == 0

def test_extra_point():

    a = [[0,0], [1,0], [1,1], [0, 1]]
    b = [[0,0], [0.1, 0.], [1,0], [1,1], [0, 1]]

    m = turning_function.distance(a, b)

    assert m == 0

@pytest.mark.parametrize("num_points", [3, 42, 1024])
def test_random1(num_points):

    shape_a = random_shape(num_points)

    distance = turning_function.distance(shape_a, shape_a)

    assert distance == 0
