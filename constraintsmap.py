import glob
import imageio
import json
import jsons
import numpy as np
import uuid
from functools import partial
from dataclasses import dataclass


class Operation:
    # Add
    def __init__(self):
        self.name = 'add'
        self.execute_op = partial(np.add)

    def execute(self, img_array, constraint_array):
        return self.execute_op(constraint_array, img_array)


class SubtractOperation(Operation):
    execute_op = partial(np.subtract)


class MinOperation(Operation):
    # Floor
    def __init__(self, min=0):
        self.min = min
        self.execute_op = partial(np.clip, min=min)


class MaxOperation(Operation):
    # ceiling
    def __init__(self, max=0):
        self.max = max
        self.execute_op = partial(np.clip, max=max)


class RoundOperation(Operation):
    def __init__(self):
        self.execute_op = partial(np.around, decimals=2)


class Constraint:
    constraint_op = None

    def __init__(self, name, img_array, operation, operation_props, sort_order=0, weight=1):
        self.id = str(uuid.uuid4())
        self.name = name
        self.img_array = img_array
        self.sort_order = sort_order
        self.weight = weight
        self.operation = operation
        self.operation_props = operation_props
        ops = {
            'add': Operation(),
            'subtract': SubtractOperation(),
            'round': RoundOperation(),
            'min': MinOperation(**operation_props)
        }
        self.constraint_op = ops[operation.lower()] if operation.lower() in ops else Operation()


class MultiConstraint(Constraint):
    # like a single constraint but for a directory/path

    def __init__(self, path):
        self.path = path

    def execute(self):
        for image_path in glob.glob("/home/adam/*.png"):
            im = imageio.imread('my_image.png')
            self.constraint_op.execute(im)


@dataclass
class ConstraintsConfig:
    save_location: str
    output_location: str
    scale: bool = False
    scale_min: int = 0
    scale_max: int = 100
    round: bool = False


def read_constraints(constraint_json):
    with open(constraint_json) as file:
        c_json = json.load(file, encoding='utf8')
        constraints = [jsons.load(c, Constraint) for c in c_json['constraints']]
        return constraints


def read_layers():
    constraints = read_constraints()
    weighted_sum = sorted([(c.weight, c.sort_order) for c in constraints],
        key=lambda x: x[1])
    con_arrays = sorted([(c.image, c.sort_order) for c in constraints],
        key=lambda x: x[1])
    # np.dot(a,weights) but with multiple
    return np.linalg.multi_dot(con_arrays, weighted_sum)


def write_output(img_array, output_path):
    imageio.imwrite(output_path, img_array)


def read_config(path='./config.json'):
    config = None
    with open(path) as file:
        try:
            dict_config = json.load(file, encoding='utf8')
            config = jsons.load(dict_config, ConstraintsConfig)
        except FileNotFoundError:
            print(path + " not found. ")
        except ValueError:
            print("parse error")
    return config


if __name__ == '__main__':
    config = read_config()
    img_array = read_layers()
    if config.output_location:
        write_output(img_array, config.output_location)
