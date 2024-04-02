from manim import *
from utils.grid import *
from utils.transform import *

direction = np.array([ 4, 2 ])

class MatrixDotScene(Scene):
    def construct(self):
        transform_matrix = np.array([
            [ 2, 1 ],
            [ 0, 1 ]
        ])
        formula = VGroup(
            Matrix(
                transform_matrix,
                h_buff = 0.75
            ),
            MathTex(r"\cdot"),
            Matrix(
                [
                    [ int(direction[0] / 2) ],
                    [ int(direction[1] / 2) ]
                ],
                h_buff = 0.75
            )
        )

        result = Matrix(
            [
                [ 0 ],
                [ 0 ]
            ],
            v_buff = 0.75
        )

        result_formula = VGroup(
            MathTex(" = "),
            result
        )

        result_formula.arrange()

        formula[0].set_column_colors(RED, GREEN)
        formula[2].set_row_colors(RED, GREEN)
        formula.arrange()

        self.play(
            Write(formula),
            run_time = 2
        )

        self.play(
            formula.animate.move_to(LEFT * 4.75)
        )

        # new_value = 5
        # formula[0].get_entries()[0][0].set_value(new_value)
        # self.play(Transform(formula[0].get_entries()[0][0], Tex(str(new_value))))
        # self.wait(1)

        result_formula.move_to(formula[2].get_right() + RIGHT)

        self.play(
            Write(result_formula[0]),
            Write(result.get_brackets())
        )

        m1 = Matrix(
            [
                [ 0, 0 ],
            ],
            h_buff = 0.75
        )
        m2 = Matrix(
            [
                [ 0 ],
                [ 0 ]
            ],
            v_buff = 0.75
        )

        mul_formula = VGroup(
            m1,
            MathTex(r"\cdot"),
            m2
        )

        mul_formula[0].move_to(formula[0].get_bottom() + DOWN * 2)
        mul_formula[1].move_to(mul_formula[0].get_right() + RIGHT * 0.3)
        mul_formula[2].move_to(mul_formula[1].get_right() + RIGHT * 0.75)

        self.play(
            Write(mul_formula[0].get_brackets()),
            Write(mul_formula[1]),
            Write(mul_formula[2].get_brackets()),
        )

        result_tex = VGroup(
            MathTex(formula[0].get_rows()[0][0].copy().get_tex_string()),
            MathTex("\\times"),
            MathTex(formula[2].get_columns()[0][0].copy().get_tex_string()),
            MathTex("+"),
            MathTex(formula[0].get_rows()[0][1].copy().get_tex_string()),
            MathTex("\\times"),
            MathTex(formula[2].get_columns()[0][1].copy().get_tex_string()),
        )
        result_tex[0].set_color(RED)
        result_tex[2].set_color(RED)
        result_tex[4].set_color(GREEN)
        result_tex[6].set_color(GREEN)
        result_tex.arrange()
        result_matrix = MobjectMatrix(
            [
                [
                    result_tex
                ]
            ]
        )

        r1 = VGroup(
            MathTex(" = "),
            result_matrix
        )
        r1.arrange()
        r1.move_to(mul_formula[2].get_right() + RIGHT * 2.4)

        self.play(
            Write(r1[0]),
            Write(r1[1].get_brackets())
        )

        items = [ None, None ]

        for i in range(2):
            formula_row_1 = VGroup(
                formula[0].get_rows()[i][0].copy(),
                formula[0].get_rows()[i][1].copy(),
            )
            formula_column_1 = VGroup(
                formula[2].get_columns()[0][0].copy(),
                formula[2].get_columns()[0][1].copy(),
            )

            for j, tex in enumerate(formula_row_1):
                tex.move_to(mul_formula[0][0][j].get_center())
            
            for j, tex in enumerate(formula_column_1):
                tex.move_to(mul_formula[2][0][j].get_center())

            self.play(
                ReplacementTransform(
                    formula[0].get_rows()[i].copy(),
                    formula_row_1
                ),
                ReplacementTransform(
                    formula[2].get_columns()[0].copy(),
                    formula_column_1
                )
            )
            result_tex = VGroup(
                MathTex(formula_row_1[0].get_tex_string()),
                MathTex("\\times"),
                MathTex(formula_column_1[0].get_tex_string()),
                MathTex("+"),
                MathTex(formula_row_1[1].get_tex_string()),
                MathTex("\\times"),
                MathTex(formula_column_1[1].get_tex_string()),
            )
            result_tex[0].set_color(RED)
            result_tex[2].set_color(RED)
            result_tex[4].set_color(GREEN)
            result_tex[6].set_color(GREEN)
            result_tex.arrange()
            result_matrix = MobjectMatrix(
                [
                    [
                        result_tex
                    ]
                ]
            )

            r = VGroup(
                MathTex(" = "),
                result_matrix
            )
            r.arrange()
            r.move_to(mul_formula[2].get_right() + RIGHT * 2.4)
            self.play(
                ReplacementTransform(
                    formula_row_1[0],
                    result_matrix[0][0][0]
                ),
                ReplacementTransform(
                    formula_column_1[0],
                    result_matrix[0][0][2]
                ),
                run_time = 0.5
            )
            self.play(
                Write(result_matrix[0][0][1]),
                run_time = 0.5
            )
            self.play(
                Write(result_matrix[0][0][3]),
                run_time = 0.5
            )
            self.play(
                ReplacementTransform(
                    formula_row_1[1],
                    result_matrix[0][0][4]
                ),
                ReplacementTransform(
                    formula_column_1[1],
                    result_matrix[0][0][6]
                ),
                run_time = 0.5
            )
            self.play(
                Write(result_matrix[0][0][5]),
                run_time = 0.5
            )

            items[i] = MathTex(f"{int(formula_row_1[0].get_tex_string()) * int(formula_column_1[0].get_tex_string()) + int(formula_row_1[1].get_tex_string()) * int(formula_column_1[1].get_tex_string())}")
            items[i].set_color(RED if i == 0 else GREEN)
            items[i].move_to(result[0][i].get_center())

            self.play(
                ReplacementTransform(
                    result_matrix[0][0],
                    items[i]
                )
            )
            self.wait(1)

        self.wait(1)

        f = VGroup(
            formula,
            result_formula[0],
            result_formula[1].get_brackets(),
            items[0],
            items[1],
        )

        f_copy = f.copy()

        self.remove(*f)
        self.add(f_copy)

        f.shift(LEFT * 1.25 + UP * 3)
        f.scale(0.75)
        f.set_z_index(100)

        grid = NumberPlane(
            x_range = ( -32, 32 ),
            y_range = ( -32 * (1080 / 1920), 32 * (1080 / 1920) ),
            x_length = self.camera.frame_width * 2,
            y_length = self.camera.frame_height * 2,
        )

        second_grid = grid.copy()

        set_grid_lines(grid)
        set_grid_lines(
            second_grid,
            stroke_color = WHITE,
            second_stroke_color = WHITE,
            opacity = 0.35
        )
        
        self.play(
            Unwrite(m1.get_brackets()),
            Unwrite(mul_formula[1]),
            Unwrite(m2.get_brackets()),
            Unwrite(r1[0]),
            Unwrite(r1[1].get_brackets()),
            ReplacementTransform(
                f_copy,
                f
            ),
            Write(grid)
        )

        vector = Vector(
            grid.c2p(*direction)
        )

        transformed_vector = Vector(
            grid.c2p(*transform_matrix.dot(direction))
        )

        self.play(
            ReplacementTransform(
                f[0][2].copy(),
                vector
            )
        )
        self.play(
            ReplacementTransform(
                f[2].copy(),
                transformed_vector
            )
        )

        second_grid.set_z_index(0)

        self.play(
            FadeIn(second_grid),
            grid.animate.apply_matrix(transform_matrix),
            ReplacementTransform(
                f[0][0].copy(),
                transformed_vector
            ),
            ApplyMethod(
                vector.put_start_and_end_on,
                *get_transformed_vector(
                    grid,
                    vector,
                    transform_matrix
                )
            )
        )

        self.wait(1)
        


class BasisScene(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range = ( -32, 32 ),
            y_range = ( -32 * (1080 / 1920), 32 * (1080 / 1920) ),
            x_length = self.camera.frame_width * 2,
            y_length = self.camera.frame_height * 2,
        )

        second_grid = grid.copy()

        set_grid_lines(grid)
        set_grid_lines(
            second_grid,
            stroke_color = WHITE,
            second_stroke_color = WHITE,
            opacity = 0.35
        )

        x_basis_vector = Vector(
            grid.c2p(2, 0)
        )
        x_basis_vector.color = RED

        y_basis_vector = Vector(
            grid.c2p(0, 2)
        )
        y_basis_vector.color = GREEN

        self.add(grid)
        x_basis_vector2 = x_basis_vector.copy()
        self.add(
            x_basis_vector,
            y_basis_vector
        )

        vector = Vector(
            grid.c2p(*direction)
        )
        self.add(x_basis_vector2)

        self.play(
            ApplyMethod(
                x_basis_vector2.put_start_and_end_on,
                grid.c2p(0, 0),
                grid.c2p(4, 0)
            ),
            ApplyMethod(
                y_basis_vector.put_start_and_end_on,
                grid.c2p(4, 0),
                grid.c2p(4, 2)
            )
        )
        self.play(
            Unwrite(x_basis_vector),
            Write(vector)
        )

        self.wait(2)

        transform_matrix = [
            [ 2, 1 ],
            [ 0, 1 ]
        ]
        inverse_transform_matrix = [
            [ 1 / 2, -1 / 2 ],
            [ 0, 1 ]
        ]

        matrix = Matrix(
            transform_matrix,
            h_buff = 0.8
        )

        matrix_block = VGroup(
            matrix,
            SurroundingRectangle(
                matrix,
                color = BLACK,
                fill_opacity = 0.5,
                stroke_opacity = 0.5
            )
        )

        matrix.set_column_colors(RED, GREEN)

        surrounding_ellipse1 = Ellipse(
            matrix.get_columns()[0].get_width() * 3,
            matrix.get_columns()[0].get_height() * 1.2
        )
        surrounding_ellipse2 = surrounding_ellipse1.copy()

        matrix_block.shift(UL + UP)
        second_grid.set_z_index(-1)

        surrounding_ellipse1.move_to(matrix.get_columns()[0])
        surrounding_ellipse2.move_to(matrix.get_columns()[1])
        surrounding_ellipse2.set_stroke(GREEN)

        print(grid.c2p(1, 0))

        self.play(
            FadeIn(second_grid),
            Create(matrix_block[1]),
            Write(matrix),
            grid.animate.apply_matrix(transform_matrix),
            ApplyMethod(
                vector.put_start_and_end_on,
                *get_transformed_vector(grid, vector, transform_matrix)
            ),
            ApplyMethod(
                x_basis_vector2.put_start_and_end_on,
                *get_transformed_vector(grid, x_basis_vector2, transform_matrix)
            ),
            ApplyMethod(
                y_basis_vector.put_start_and_end_on,
                *get_transformed_vector(grid, y_basis_vector, transform_matrix)
            )
        )

        self.wait(4)

        print()

        self.play(
            FadeOut(second_grid),
            grid.animate.apply_matrix(inverse_transform_matrix),
            ApplyMethod(
                vector.put_start_and_end_on,
                *get_transformed_vector(
                    second_grid,
                    vector,
                    inverse_transform_matrix
                )
            ),
            ApplyMethod(
                x_basis_vector2.put_start_and_end_on,
                *get_transformed_vector(
                    second_grid,
                    x_basis_vector2,
                    inverse_transform_matrix
                )
            ),
            ApplyMethod(
                y_basis_vector.put_start_and_end_on,
                *get_transformed_vector(
                    second_grid,
                    y_basis_vector,
                    inverse_transform_matrix
                )
            )
        )

        self.wait(1)

        self.play(
            Create(surrounding_ellipse1),
            run_time = 0.5
        )

        self.wait()

        self.play(
            ReplacementTransform(
                matrix.get_columns()[0].copy(),
                x_basis_vector2
            )
        )

        self.play(
            FadeIn(second_grid),
            grid.animate.apply_matrix([
                [ 2, 0 ],
                [ 0, 1 ]
            ]),
            ApplyMethod(
                vector.put_start_and_end_on,
                *get_transformed_vector(
                    grid,
                    vector,
                    [
                        [ 2, 0 ],
                        [ 0, 1 ]
                    ]
                )
            ),
            ApplyMethod(
                x_basis_vector2.put_start_and_end_on,
                *get_transformed_vector(
                    grid,
                    x_basis_vector2,
                    [
                        [ 2, 0 ],
                        [ 0, 1 ]
                    ]
                )
            ),
            ApplyMethod(
                y_basis_vector.put_start_and_end_on,
                *get_transformed_vector(
                    grid,
                    y_basis_vector,
                    [
                        [ 2, 0 ],
                        [ 0, 1 ]
                    ]
                )
            )
        )

        self.wait(2)

        self.play(
            Transform(
                surrounding_ellipse1,
                surrounding_ellipse2
            ),
            run_time = 0.5
        )

        self.wait()

        self.play(
            ReplacementTransform(
                matrix.get_columns()[1].copy(),
                y_basis_vector
            )
        )

        self.play(
            grid.animate.apply_matrix([
                [ 1, 1 ],
                [ 0, 1 ]
            ]),
            ApplyMethod(
                vector.put_start_and_end_on,
                *get_transformed_vector(
                    second_grid,
                    vector,
                    [
                        [ 1, 1 ],
                        [ 0, 1 ]
                    ]
                )
            ),
            ApplyMethod(
                x_basis_vector2.put_start_and_end_on,
                *get_transformed_vector(
                    second_grid,
                    x_basis_vector2,
                    [
                        [ 1, 1 ],
                        [ 0, 1 ]
                    ]
                )
            ),
            ApplyMethod(
                y_basis_vector.put_start_and_end_on,
                *get_transformed_vector(
                    second_grid,
                    y_basis_vector,
                    [
                        [ 1, 1 ],
                        [ 0, 1 ]
                    ]
                )
            )
        )

class MatrixScene(Scene): 
    def construct(self):
        vector = Matrix(
            [
                [ int(direction[0] / 2), int(direction[1] / 2) ]
            ],
            h_buff = 0.75
        )
        vector.set_column_colors(RED, GREEN)

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

        right_angle_length = 0.4

        right_angles = VGroup(
            RightAngle(
                dot_vector,
                rotated_dot_vector1,
                length = right_angle_length
            ),
            RightAngle(
                rotated_dot_vector1,
                rotated_dot_vector2,
                length = right_angle_length
            ),
            RightAngle(
                rotated_dot_vector2,
                rotated_dot_vector3,
                length = right_angle_length
            ),
            RightAngle(
                rotated_dot_vector3,
                dot_vector,
                length = right_angle_length
            ),
        )

        right_angles.set_color(BLUE)

        self.play(
            *[
                Write(right_angle)
                for right_angle in right_angles
            ],
            run_time = 1
        )


        self.wait(2)
        dot.set_x(0)
        dot.set_y(0)
        self.add(dot)

        dot_vector_clone = dot_vector.copy()

        self.play(
            ReplacementTransform(
                VGroup(
                    right_angles,
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

        self.play(
            Write(dot_vector_clone)
        )

        self.wait()

        transform_matrix = np.array([
            [ 2, 1 ],
            [ 0, 1 ]
        ])

        transformed_vector_end = transform_matrix.dot([
            [ grid.c2p(*direction)[0] ],
            [ grid.c2p(*direction)[1] ]
        ]).flatten().tolist()
        transformed_vector_end.append(0)

        self.play(
            grid.animate.apply_matrix(transform_matrix),
            ApplyMethod(
                dot_vector_clone.put_start_and_end_on,
                dot_vector_clone.start,
                transformed_vector_end
            )
        )

        
def get_rotate_matrix(degrees: float):
    radians = degrees * np.pi / 180
    cos = round(np.cos(radians), 12)
    sin = round(np.sin(radians), 12)
    return np.array([
        [ cos, -sin ],
        [ sin, cos ]
    ])