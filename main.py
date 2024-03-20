from manim import *
from utils.grid import *

class MyGrid(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range = ( -10, 10, 1 ),
            y_range = ( -10, 10, 1 ),
            x_length = self.camera.frame_width,
            y_length = self.camera.frame_height
        )

        get_grid_lines(
            plane,
            unit_count = -1
        )

        self.play(
            Write(plane),
            run_time = 1
        )
        self.wait()