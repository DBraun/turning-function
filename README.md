# Turning Function

This module contains Python bindings to a C-implementation of ["An efficiently computable metric for comparing polygonal shapes"](http://www.cs.cornell.edu/~dph/papers/ACHKM-TPAMI-91.pdf) (Arkin et al., 1991).

## Installation

`pip install turning_function`

## Usage

```python
import turning_function
import random

def random_shape(num_points: int):

	return [(random.random(), random.random()) for _ in range(num_points)]

shape_a = random_shape(turning_function.max_points)
shape_b = random_shape(42)

distance = turning_function.distance(shape_a, shape_b)
print('Distance: ', distance)

```

## License

The original source has this disclaimer:
> Implementation (c) Eugene K. Ressler 91, 92  This source may be freely distributed and used for non-commercial purposes, so long as this comment is attached to any code copied or derived from it.