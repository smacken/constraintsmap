import rasterio
from rasterio.features import rasterize
from rasterio.transform import IDENTITY
import numpy as np


def to_raster(geometry, rows, cols, out_file='test.tif'):
    ''' vector geometry to raster '''
    with rasterio.Env():
        result = rasterize([geometry], out_shape=(rows, cols))
        with rasterio.open(
                "test.tif",
                'w',
                driver='GTiff',
                width=cols,
                height=rows,
                count=1,
                dtype=np.uint8,
                nodata=0,
                transform=IDENTITY,
                crs={'init': "EPSG:4326"}) as out:
            out.write(result.astype(np.uint8), indexes=1)


def to_raster_array(geometry, rows, cols):
    with rasterio.Env():
        result = rasterize([geometry], out_shape=(rows, cols))
        return result.astype(np.uint8)
