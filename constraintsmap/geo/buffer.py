from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from enum import Enum
import fiona
from shapely.geometry import shape, CAP_STYLE
from constraintsmap.constraint.constraints import Constraint, Operation
from .raster import to_raster_array


class BufferEnd(Enum):
    ROUND = 1
    FLAT = 2
    SQUARE = 3


cap_style = {
    BufferEnd.ROUND: CAP_STYLE.round,
    BufferEnd.FLAT: CAP_STYLE.flat,
    BufferEnd.SQUARE: CAP_STYLE.square
}

''' Buffer constraint example json
{
    "id":"",
    "name": "",
    "sort_order": 1,
    "image": "",
    "weight": 1,
    "operation": "Add",
    "operation_props": {}
}'''


class BufferConstraint(Constraint):
    ''' Create a buffered constraint around a vector '''

    @classmethod
    def init_create_geometry(shp_file, buffer_size, buffer_end=BufferEnd.ROUND):
        ''' convert the shape file to a geometry object '''
        input_shp = fiona.open(shp_file)
        shp = input_shp.next()
        shp_geo = shape(shp['geometry'])
        buffer_geo = shp_geo.buffer(buffer_size, cap_style=cap_style[buffer_end.lower()])
        return buffer_geo

    def __init__(self, shp_file, buffer_size, buffer_end=BufferEnd.ROUND, weight=1, sort_order=0):
        self.constraint_op = Operation()
        self.weight = weight
        self.sort_order = sort_order
        geometry = BufferConstraint.init_create_geometry(shp_file, buffer_size, buffer_end)
        raster = to_raster_array(geometry)
        raster[raster > 0] = weight
        self.img_array = raster
        super(BufferConstraint, self).__init__()
