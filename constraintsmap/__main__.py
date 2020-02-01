from constraintsmap.common.config import read_config, write_output, read_layers

config = read_config()
img_array = read_layers()
if config.output_location:
    write_output(img_array, config.output_location)