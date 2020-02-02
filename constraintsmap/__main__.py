from constraintsmap.common.config import read_config, write_output, read_layers

if __name__ == '__main__':
    config = read_config()
    img_array = read_layers()
    if config.output_location:
        write_output(img_array, config.output_location)