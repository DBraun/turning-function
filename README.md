# Turning Function

This module contains Python bindings to a C-implementation of ["An efficiently computable metric for comparing polygonal shapes"](http://www.cs.cornell.edu/~dph/papers/ACHKM-TPAMI-91.pdf) (Arkin et al., 1991).

## Installation

`pip install turning_function`

## Usage

Call `turning_function.distance(shape_a, shape_b, brute_force_updates=False)` where `shape_a`/`shape_b` are Nx2-shaped lists of points (not numpy arrays). This function will return four values: `distance, theta, ht_err, slope_err`. The error terms will be zero if `brute_force_updates` is `False`. Note that there is a maximum number of points (`turning_function.max_points`) a shape can hold.

```python
import turning_function
import random

def random_shape(num_points: int):

	return [(random.random(), random.random()) for _ in range(num_points)]

shape_a = random_shape(turning_function.max_points)
shape_b = random_shape(42)

distance, theta, ht_err, slope_err = turning_function.distance(shape_a, shape_b, brute_force_updates=False)
print('Distance: ', distance)

```

## License

The original source has this disclaimer:
> Implementation (c) Eugene K. Ressler 91, 92  This source may be freely distributed and used for non-commercial purposes, so long as this comment is attached to any code copied or derived from it.