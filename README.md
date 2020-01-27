# Constraints Map

Take a series of layers/constraints and align to a given weighting to 
combine for an overall constrained output.
Busically munge together layers with weights for an output.
Each layer/constraint can have an operation applied e.g. min/max, +/-, multiple, gate

Constraints json

Each constraint layer can be input via a json file.

Geo

Allows constraints layers to be added in shape file format as vectors.
Constraint operators (e.g. Buffer) can be applied to points/lines/polygons before
being included in the constraints matrix.

Constraint-linking

Constraints can be included based upon the relationship with another constraint-layer.
For example: add a layer based upon the intersection of another constraint-layer.
Each constraint layer is given a unique id which can be linked when creating another.