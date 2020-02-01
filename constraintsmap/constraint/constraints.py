import uuid
import glob
import imageio
from .operation import Operation, SubtractOperation, RoundOperation, MinOperation, MaxOperation


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
            'min': MinOperation(**operation_props),
            'max': MaxOperation(**operation_props)
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
