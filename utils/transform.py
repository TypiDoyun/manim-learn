from manim import *

def get_transformed_vector(grid: NumberPlane, vector: Vector, matrix):
    matrix = np.array(matrix)

    return [
        grid.c2p(*matrix.dot(grid.p2c(vector.get_start())[:2].reshape(2, 1)).flatten().tolist()),
        grid.c2p(*matrix.dot(grid.p2c(vector.get_end())[:2].reshape(2, 1)).flatten().tolist())

    ]