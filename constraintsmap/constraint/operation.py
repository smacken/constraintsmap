import numpy as np
from functools import partial


class Operation:
    # Add
    def __init__(self):
        self.name = 'add'
        self.execute_op = partial(np.add)

    def execute(self, img_array, constraint_array):
        return self.execute_op(constraint_array, img_array)


class SubtractOperation(Operation):
    def __init__(self):
        self.name = 'subtract'
        self.execute_op = partial(np.subtract)
        super(SubtractOperation, self).__init__()


class MinOperation(Operation):
    # Floor
    def __init__(self, min=0):
        self.min = min
        self.execute_op = partial(np.clip, min=min)
        super(MinOperation, self).__init__()


class MaxOperation(Operation):
    # ceiling
    def __init__(self, max=0):
        self.max = max
        self.execute_op = partial(np.clip, max=max)
        super(MaxOperation, self).__init__()


class RoundOperation(Operation):
    def __init__(self):
        self.execute_op = partial(np.around, decimals=2)
        super(RoundOperation, self).__init__()
