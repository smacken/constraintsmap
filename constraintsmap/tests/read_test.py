from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from constraintsmap.common.config import read_config, read_constraints


def test_init():
    ''' should pass '''
    assert 1 == 1


def test_read_config():
    config = read_config('./constraintsmap/tests/config.json')
    assert config != None
    assert config.save_location == '/tests/'


def test_read_constraints():
    constraints = read_constraints('./constraintsmap/tests/constraints.json')
    assert constraints != None
