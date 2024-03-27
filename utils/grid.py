from manim import *

class NumberPlaneGrid():
    def __init__(self, x: VGroup, y: VGroup):
        self.x = x
        self.y = y

    x: VGroup
    y: VGroup

def get_grid_lines(
    plane: NumberPlane
) -> NumberPlaneGrid:
    index = round((plane.y_range[1] - plane.y_range[0]) / plane.y_range[2])
    y = plane.background_lines[:index]
    x = plane.background_lines[index:]

    return NumberPlaneGrid(
        x = x,
        y = y
    )
    

def set_grid_lines(
    plane: NumberPlane,
    unit_count: int = 1,
    stroke_color: ManimColor = BLUE_D,
    stroke_width: float = 1,
    stroke_opacity: float = 1,
    second_stroke_color: ManimColor = BLUE_D,
    second_stroke_width: float = 1,
    second_stroke_opacity: float = 0.5
) -> None:
    grid = get_grid_lines(plane)

    print(grid)

    x_grid_lines = []
    y_grid_lines = []

    def set_style(condition: bool):
        if (condition):
            line.set_style(
                stroke_color = stroke_color,
                stroke_width = stroke_width,
                stroke_opacity = stroke_opacity
            )
        else:
            line.set_style(
                stroke_color = second_stroke_color,
                stroke_width = second_stroke_width,
                stroke_opacity = second_stroke_opacity
            )

    for i, line in enumerate(grid.y):
        is_primary_stroke = round(plane.p2c((0, grid.y[i].get_y(), 0))[1] / plane.y_range[2], 12) % (unit_count + 1) == 0
        set_style(is_primary_stroke)       
        y_grid_lines.append(line)
    
    for i, line in enumerate(grid.x):
        is_primary_stroke = round(plane.p2c((grid.x[i].get_x(), 0, 0))[0] / plane.x_range[2], 12) % (unit_count + 1) == 0
        set_style(is_primary_stroke)
        x_grid_lines.append(line)

    return VGroup(*(y_grid_lines + x_grid_lines))