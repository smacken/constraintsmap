import glob
import imageio
import json
import jsons
import numpy as np
from functools import partial
from dataclasses import dataclass


class Operation:
    # Add
    name=''
    execute_op = partial(np.add)
    def execute(img_array, constraint_array):
        return execute_op(constraint_array, img_array)

class SubtractOperation(Operation):
    execute_op = partial(np.subtract)

class MinOperation:
    # Floor
    min=0
    execute_op = partial(np.clip, min=min)

class RoundOperation:
    execute_op = partial(np.around, decimals=2)

class Constraint:
    name=''
    sort_order=0
    image=''
    weight=1
    operation=None
    operationProps={}

    def __init__(super, img_array):
        pass

class MultiConstraint(Constraint):
    # like a single constraint but for a directory/path
    name=''
    sort_order=0
    path=''
    weight=1
    operation=None

    def execute():
        for image_path in glob.glob("/home/adam/*.png"):
            im = imageio.imread('my_image.png')
            operation.execute(im)


@dataclass
class ConstraintsConfig:
    save_location: str
    output_location: str
    scale: bool = False
    scale_min: int = 0
    scale_max: int = 100
    round: bool = False


def read_constraints(constraint_json):
    constraints = json.loads(constraint_json)
    con = [Constraint(**c) for c in constraints['constraints']]
    return con


def read_layers():
    constraints = read_constraints()
    weighted_sum = sorted([(c.weight, c.sort_order) for c in constraints],
        key=lambda x: x[1])
    con_arrays = sorted([(c.image, c.sort_order) for c in constraints],
        key=lambda x: x[1])
    # np.dot(a,weights) but with multiple
    return numpy.linalg.multi_dot(con_arrays, weighted_sum)


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
