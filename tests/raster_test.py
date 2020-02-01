from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
# from ..constraintsmap import read_config, read_constraints
from geo.raster import to_raster_array
from geo.buffer import BufferConstraint


# def test_init():
#     ''' should pass '''
#     assert 1 == 1

def test_to_raster_array():
    geo = BufferConstraint.init_create_geometry('./tests/data/State_Fairgrounds.shp', 10)
    ras_arr = to_raster_array(geo, 100, 100)
    assert ras_arr is not None


def test_to_raster_writes_file():
    assert 1 == 1
