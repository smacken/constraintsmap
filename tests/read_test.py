from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from main import read_config


def test_init():
    ''' should pass '''
    assert 1 == 1


def test_read_config():
    config = read_config('./tests/config.json')
    assert config != None
    assert config.save_location == '/tests/'
