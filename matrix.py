from manim import *
from utils.grid import *

class MatrixScene(Scene): 
    def construct(self):
        direction = np.array([ 2, 1 ])
        vector = Matrix(
            [
                direction
            ],
            h_buff = 0.75
        )

        self.play(
            Write(vector),
            run_time = 2
        )

        self.wait(1)

        grid = NumberPlane(
            x_range = ( -5, 5 ),
            y_range = ( -5, 5 ),
            x_length = self.camera.frame_width,
            y_length = self.camera.frame_height,
        )
        dot = Dot(
            grid.c2p(direction[0], direction[1])
        )
        dot.set_opacity(0)
        dot_vector = Vector(
            grid.c2p(direction[0], direction[1])
        )
        rotated_dot_vector = dot_vector.copy()

        set_grid_lines(grid)

        self.play(
            Write(grid),
            run_time = 1
        )
        self.play(
            ReplacementTransform(vector, dot),
            Write(dot_vector),
            run_time = 1
        )
        self.remove(dot)

        self.wait(1)

        self.play(
            Rotate(
                VGroup(*[ rotated_dot_vector ]),
                PI / 2,
                about_point = grid.c2p(0, 0)
            ),
            run_time = 1
        )

        norm = np.linalg.norm(direction)
        from_1 = direction / norm * 0.4
        to_1 = get_rotate_matrix(90).dot(from_1) + from_1
        to_2 = get_rotate_matrix(180).dot(from_1) + to_1

        angle_symbol = VGroup(
            Line(
                grid.c2p(*from_1.tolist()),
                grid.c2p(*to_1.tolist())
            ),
            Line(
                grid.c2p(*to_1.tolist()),
                grid.c2p(*to_2.tolist())
            )
        )

        self.play(Create(angle_symbol))

        rotated_direction = get_rotate_matrix(90)


        
def get_rotate_matrix(degrees: float):
    radians = degrees * np.pi / 180
    cos = round(np.cos(radians), 12)
    sin = round(np.sin(radians), 12)
    return np.array([
        [ cos, -sin ],
        [ sin, cos ]
    ])