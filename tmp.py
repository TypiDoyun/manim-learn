from manim import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()

        self.play(Create(square))
        self.wait(1)
        self.play(Transform(square, circle))
        self.wait(1)

class TwoDToThreeD(ThreeDScene):
    def construct(self):
        config.frame_rate = 60

        # 2차원 그래프를 정의
        axes = ThreeDAxes(
            x_range = ( -2 * TAU, 2 * TAU, PI / 2 ),
            y_range = ( -2 * TAU, 2 * TAU, 1 ),
            z_range = ( -2 * TAU, 2 * TAU, PI / 2 )
        )
        graph = axes.plot(
            lambda t: 2,
            color = BLUE
        )

        self.play(Write(axes))
        self.play(Create(graph))
        self.wait(1)

        phi = 0 * DEGREES
        theta = 90 * DEGREES


        self.move_camera(
            phi = phi,
            theta = theta,
            run_time = 3
        )
        self.wait()

class SinWave(Scene):
    def construct(self):

        x_labels = [
            "-\\frac{3\\pi}{2}", #  -3pi/2
            "-\\pi", #              -pi
            "-\\frac{\\pi}{2}", #   -pi/2
            "0", #                   Blank
            "\\frac{\\pi}{2}", #     pi/2
            "\\pi",#                 pi
            "\\frac{3\\pi}{2}" #     3pi/2
        ]
        axes = Axes(
            x_range = (-3*PI/2, 3*PI/2, PI/2),
            y_range = (-1.5, 1.5, 0.5),
            x_length = 10,
            axis_config={"include_tip": False}
        )
        axes.center()

        x_tex_lables = VGroup(*[
            MathTex(t).next_to(axes.x_axis.n2p(x),DOWN) if x >= 0 else
            MathTex(t).next_to(axes.x_axis.n2p(x),DOWN).shift(LEFT*0.2)
            for t,x in zip(x_labels, np.arange(-3*PI/2, 3*PI/2+PI/2, PI/2)) if t != "0"
        ])
        self.add(axes,x_tex_lables)
        self.wait()

def sin(t: float):
    return 4 * np.sin(t * PI / 4)

def cos(t: float):
    return 4 * np.cos(t * PI / 4)

class Wave(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = ( -10, 10, 1 ),
            y_range = ( -10, 10, 1 ),
            x_length = self.camera.frame_width,
            y_length = self.camera.frame_height
        )

        sin_wave = plane.plot(
            lambda t: -sin(t)
        )
        label = MathTex("f(x) = -\\sin(x)").to_corner(UL)

        self.add(
            get_grid_lines(plane), 
            plane,
            sin_wave,
            label
        )

class Sin(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range = ( -20, 20, 1 ),
            y_range = ( -20, 20, 1 ),
            z_range = ( -20, 0, 20 ),
            x_length = self.camera.frame_width * 2,
            y_length = self.camera.frame_height * 2,
            z_length = self.camera.frame_height,
            tips = False
        )

        axes.axis_config = {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "include_tip": False,
        }

        simple_cosine_wave = axes.plot(
            lambda t: cos(t),
            x_range = ( axes.x_range[0] / 2, axes.x_range[1] / 2 )
        )

        sine_wave = axes.plot(
            lambda t: (sin(t) + sin(2 * t) + sin(3 * t)) / 3,
            x_range = ( axes.x_range[0] / 2, axes.x_range[1] / 2 )
        )

        sine_wave_original = sine_wave.copy()

        sine_wave.color = BLUE

        sine1 = axes.plot(
            lambda t: sin(t) / 3,
            x_range = ( axes.x_range[0] / 2, axes.x_range[1] / 2 )
        )
        sine1.color = BLUE_C

        sine2 = axes.plot(
            lambda t: sin(2 * t) / 3,
            x_range = ( axes.x_range[0] / 2, axes.x_range[1] / 2 )
        )
        sine2.color = BLUE_D

        sine3 = axes.plot(
            lambda t: sin(3 * t) / 3,
            x_range = ( axes.x_range[0] / 2, axes.x_range[1] / 2 )
        )
        sine3.color = BLUE_E

        sine1.move_to(OUT * -2)
        sine2.move_to(OUT * -4)
        sine3.move_to(OUT * -6)

        self.play(Write(axes), run_time = 1)
        label = MathTex("f(x) = \\cos(x)").to_corner(UL)
        unknown_label = MathTex("f(x) = ?").to_corner(UL)

        self.play(
            Write(label),
            Create(simple_cosine_wave)
        )
        self.wait()
        self.play(
            Unwrite(label),
            Uncreate(simple_cosine_wave)
        )
        self.wait()
        self.play(Create(sine_wave), Write(unknown_label), run_time = 3)
        self.wait()
        self.move_camera(
            phi = -35 * DEGREES,
            theta = -90 * DEGREES,
            gamma = 0 * DEGREES,
            run_time = 2
        )
        sines = VGroup(sine1, sine2, sine3)
        self.play(
            Unwrite(unknown_label),
            ReplacementTransform(sine_wave, sines)
        )
        self.wait(1)
        self.play(
            sine1.animate.move_to(OUT * 0),
            sine2.animate.move_to(OUT * 0),
            sine3.animate.move_to(OUT * 0)
        )
        self.move_camera(
            phi = 0 * DEGREES,
            theta = -90 * DEGREES,
            gamma = 0 * DEGREES,
            run_time = 2
        )

        dotList = []

        for x in range(-19, 20, 1):
            print(x, sin(x) / 3, axes.p2c((x, sin(x) / 3, 0)))
            dot1 = Dot(
                point = axes.c2p(x, sin(x) / 3, 0),
                radius = 0.05,
                color = WHITE
            )
            dot2 = Dot(
                point = axes.c2p(x, sin(2 * x) / 3, 0),
                radius = 0.05,
                color = WHITE
            )
            dot3 = Dot(
                point = axes.c2p(x, sin(3 * x) / 3, 0),
                radius = 0.05,
                color = WHITE
            )

            dotList.append(VGroup(dot1, dot2, dot3))
        
        dots = VGroup(*dotList)
        self.play(Write(dots), run_time = 5)
        self.wait()

        targets = []

        for group in dots:
            y = 0

            for dot in group:
                y += dot.get_y()

            dot = Dot(
                point = (group[0].get_x(), y, 0),
                radius = 0.05,
                color = BLUE
            )

            targets.append(dot)

        self.play(*[
            ReplacementTransform(
                dots[i],
                target
            ) for i, target in enumerate(targets)
            ],
            Uncreate(sine1),
            Uncreate(sine2),
            Uncreate(sine3),
            run_time = 2
        )

        sine_wave_original.color = BLUE

        self.play(Write(sine_wave_original), run_time = 3)
        self.wait()

class Break(Scene):
    def construct(self):
        axes = Axes(
            x_range = ( -20, 20, 1 ),
            y_range = ( -20, 20, 1 ),
            x_length = self.camera.frame_width * 2,
            y_length = self.camera.frame_height * 2,
            tips = False
        )

        axes.axis_config = {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "include_tip": False,
        }

        pure_sin = axes.plot(
            lambda t: sin(t),
            x_range = ( axes.x_range[0] / 2, axes.x_range[1] / 2 )
        )
        pure_sin_label = MathTex("f(x) = \\sin(x)").to_corner(UL)
        pure_sin.color = BLUE
        pure_negative_sin = axes.plot(
            lambda t: -sin(t),
            x_range = ( axes.x_range[0] / 2, axes.x_range[1] / 2 )
        )
        pure_negative_sin_label = MathTex("f(x) = -\\sin(x)").to_corner(DR)
        pure_negative_sin.color = BLUE_E

        sum = axes.plot(
            lambda t: 0,
            x_range = ( axes.x_range[0] / 2, axes.x_range[1] / 2 )
        )
        sum.stroke_width = 2

        self.play(Write(axes), run_time = 1)
        self.play(Create(pure_sin), Write(pure_sin_label))
        self.wait()
        self.play(Create(pure_negative_sin), Write(pure_negative_sin_label))
        self.wait()

        self.play(ReplacementTransform(VGroup(pure_sin, pure_negative_sin), sum))
        self.wait()