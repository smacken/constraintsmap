from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from main import Operation
import numpy as np


def test_can_add():
    op = Operation()
    first = np.array([[1, 1, 1, 1], [1, 1, 1, 1]])
    second = np.array([[1, 1, 1, 1], [1, 1, 1, 1]])
    result = op.execute(first, second)
    assert result[0] == [2, 2, 2, 2]


def test_weighted_sum():    
    first = np.array([[1, 1, 1, 1], [1, 1, 1, 1]])
    weight = 4
    weight_array = np.full(first.shape, weight)
    result = np.dot(first, weight_array)
    assert result[0] == [4, 4, 4, 4]
