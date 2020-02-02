from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from constraintsmap.constraint.operation import Operation
import numpy as np
from numpy.linalg import multi_dot


def test_can_add():
    op = Operation()
    first = np.array([[1, 1, 1, 1], [1, 1, 1, 1]])
    second = np.array([[1, 1, 1, 1], [1, 1, 1, 1]])
    result = op.execute(first, second)
    assert np.all([result[0], [2, 2, 2, 2]])


def test_weighted_sum():
    first = np.array([[1, 1, 1, 1], [1, 1, 1, 1]])
    weight = 4
    result = first * weight
    assert np.all([result[0], [4, 4, 4, 4]])


def test_weighted_sums():
    first = np.array([[1, 1, 1, 1], [1, 1, 1, 1]])
    second = np.array([[1, 1, 1, 1], [1, 1, 1, 1]])
    weights = [4, 5]
    weighted_sum = [a * weights[i] for i, a in enumerate([first, second])]
    result = Operation().execute(weighted_sum[0], weighted_sum[1])
    assert np.all([result[0], [4, 4, 4, 4]])
    assert np.all([result[1], [5, 5, 5, 5]])    
