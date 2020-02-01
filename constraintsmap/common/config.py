import imageio
import json
import jsons
import numpy as np
from dataclasses import dataclass
from typing import Optional, Union

from constraintsmap.geo.buffer import BufferConstraint
from constraintsmap.constraint.constraints import Constraint, MultiConstraint


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
        constraints = [jsons.load(c, Union[Constraint, BufferConstraint, MultiConstraint]) for c in c_json['constraints']]
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
