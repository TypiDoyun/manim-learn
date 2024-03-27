from manim import *
from utils.grid import *

class MatrixScene(Scene): 
    def construct(self):
        direction = np.array([ 8, 4 ])
        vector = Matrix(
            [
                [ int(direction[0] / 2), int(direction[1] / 2) ]
            ],
            h_buff = 0.75
        )

        self.play(
            Write(vector),
            run_time = 2
        )

        self.wait(1)

        grid = NumberPlane(
            x_range = ( -32, 32 ),
            y_range = ( -32 * (1080 / 1920), 32 * (1080 / 1920) ),
            x_length = self.camera.frame_width * 2,
            y_length = self.camera.frame_height * 2,
        )
        dot = Dot(
            grid.c2p(*direction)
        )
        dot.set_opacity(0)
        dot_vector = Vector(
            grid.c2p(*direction)
        )
        dot_vector.set_z_index(1)
        dot_vector.stroke_width = 4
        rotated_dot_vector1 = dot_vector.copy()
        rotated_dot_vector2 = dot_vector.copy()
        rotated_dot_vector3 = dot_vector.copy()

        set_grid_lines(grid)

        self.play(
            Write(grid),
            run_time = 2
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
                VGroup(*[ rotated_dot_vector1 ]),
                PI / 2,
                about_point = grid.c2p(0, 0)
            ),
            Rotate(
                VGroup(*[ rotated_dot_vector2 ]),
                PI,
                about_point = grid.c2p(0, 0)
            ),
            Rotate(
                VGroup(*[ rotated_dot_vector3 ]),
                PI * 3 / 2,
                about_point = grid.c2p(0, 0)
            ),
            run_time = 1
        )

        norm = np.linalg.norm(direction)
        from_1 = direction / norm * 0.5
        to_1 = get_rotate_matrix(90).dot(from_1) + from_1
        to_2 = get_rotate_matrix(180).dot(from_1) + to_1
        
        line_1 = Line(
            grid.c2p(*from_1.tolist()),
            grid.c2p(*to_1.tolist())
        )
        line_2 = Line(
            grid.c2p(*to_1.tolist()),
            grid.c2p(*to_2.tolist())
        )

        line_1.stroke_width = line_2.stroke_width = 2
        line_1.stroke_color = line_2.stroke_color = BLUE

        angle_symbol = VGroup(
            line_1,
            line_2
        )
        angle_symbol.set_z_index(0)
        rotated_angle_symbol1 = angle_symbol.copy().rotate(
            PI / 2,
            about_point = grid.c2p(0, 0)
        )
        rotated_angle_symbol2 = angle_symbol.copy().rotate(
            PI,
            about_point = grid.c2p(0, 0)
        )
        rotated_angle_symbol3 = angle_symbol.copy().rotate(
            PI / 2 * 3,
            about_point = grid.c2p(0, 0)
        )

        self.play(
            Create(angle_symbol),
            Create(rotated_angle_symbol1),
            Create(rotated_angle_symbol2),
            Create(rotated_angle_symbol3),
            run_time = 0.5
        )

        self.wait()
        dot.set_x(0)
        dot.set_y(0)
        self.add(dot)

        self.play(
            ReplacementTransform(
                VGroup(
                    angle_symbol,
                    rotated_angle_symbol1,
                    rotated_angle_symbol2,
                    rotated_angle_symbol3,
                    dot_vector,
                    rotated_dot_vector1,
                    rotated_dot_vector2,
                    rotated_dot_vector3,
                ),
                dot
            ),
            run_time = 1
        )

        self.remove(dot)

        self.wait()

        self.play(
            grid.animate.apply_matrix([
                [ 2, 1 ],
                [ 0, 1 ]
            ])
        )


        
def get_rotate_matrix(degrees: float):
    radians = degrees * np.pi / 180
    cos = round(np.cos(radians), 12)
    sin = round(np.sin(radians), 12)
    return np.array([
        [ cos, -sin ],
        [ sin, cos ]
    ])