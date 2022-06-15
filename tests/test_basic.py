import turning_function

import copy

square = [[0,0], [1,0], [1,1], [0, 1]]

def test_non_zero():

	b = copy.deepcopy(square)
	b[0][0] = -1

	m = turning_function.metric(square, b)

	# print('m: ', m)

	assert abs(m - 0.6144398026382778) < .00000001

def test_rotation_invariance1():

	b = copy.deepcopy(square)

	b = [b.pop()] + b

	m = turning_function.metric(square, b)

	assert m == 0

def test_rotation_invariance2():

	b = copy.deepcopy(square)

	b = [b.pop()] + b
	b = [b.pop()] + b

	m = turning_function.metric(square, b)

	assert m == 0

def test_scale_invariance1():

	b = copy.deepcopy(square)

	scale = 2

	b = [(x*scale,y*scale) for x, y in b]

	# b = [b.pop()] + b
	# b = [b.pop()] + b

	m = turning_function.metric(square, b)

	assert m == 0

def test_translation_invariance1():

	b = copy.deepcopy(square)

	tx = 2.12351
	ty = 3.14159

	b = [(x+tx,y+ty) for x, y in b]

	# b = [b.pop()] + b
	# b = [b.pop()] + b

	m = turning_function.metric(square, b)

	assert m == 0
