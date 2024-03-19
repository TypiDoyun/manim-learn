from manim import *

class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()

        self.play(Create(square))
        self.wait(1)
        self.play(Transform(square, circle))
        self.wait(1)

class TwoDToThreeD(Scene):
    def construct(self):
        # 2차원 그래프를 정의
        axes = ThreeDAxes(
            x_range = ( -2 * TAU, 2 * TAU, PI / 2 ),
            y_range = ( -5, 5, 1 ),
            z_range = ( -2 * TAU, 2 * TAU, PI / 2 )
            
        )
        graph = ParametricFunction(
            lambda t: [ t, np.sin(t), 0 ],
            t_range = [ -TAU, TAU ],
            color = BLUE
        )

        axes.plot(lambda t: [t, np.sin(t), 0], t_min=-TAU, t_max=TAU, color=BLUE)
        graph = ParametricFunction(lambda t: [t, np.sin(t), 0], t_min=-TAU, t_max=TAU, color=BLUE)

        # 애니메이션 실행
        self.add(axes)
        self.play(Create(graph))
        self.wait()

class SinWave(Scene):
    def construct(self):
        # Axes 설정
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI],  # x축 범위 및 눈금 설정
            y_range=[-1.5, 1.5, 1],      # y축 범위 및 눈금 설정
            axis_config={"color": BLUE},  # x, y축의 색상 설정
            x_axis_config={"numbers_to_include": [-2*PI, -PI, 0, PI, 2*PI]},  # x축 눈금 설정
            y_axis_config={"numbers_to_include": [-1.5, -1, 0, 1, 1.5]},  # y축 눈금 설정
        )

        x_labels = axes.get_x_axis_label(
            "OMG",
            [ 1, 2, 5, 2 ]
        )

        graph = axes.plot(lambda x: np.sin(x), color=GREEN)


        self.play(Write(x_labels))
        # 애니메이션 실행
        self.play(Write(axes))
        self.play(Create(graph))
        self.wait()