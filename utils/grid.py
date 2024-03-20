from manim import *

def get_grid_lines(
        plane: NumberPlane,
        unit_count: int = 1,
        stroke_color: ManimColor = BLUE,
        stroke_width: float = 1,
        stroke_opacity: float = 1,
        second_stroke_color: ManimColor = BLUE,
        second_stroke_width: float = 1,
        second_stroke_opacity: float = 0.4
    ):
    index = round((plane.y_range[1] - plane.y_range[0]) / plane.y_range[2])
    y_grid = plane.background_lines[:index]
    x_grid = plane.background_lines[index:]

    x_grid_lines = []
    y_grid_lines = []

    for i, line in enumerate(y_grid):
        isPrimaryStroke = round(plane.p2c((0, y_grid[i].get_y(), 0))[1] / plane.y_range[2], 12) % (unit_count + 1) == 0

        if (isPrimaryStroke):
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
        y_grid_lines.append(line)
    
    for i, line in enumerate(x_grid):
        isPrimaryStroke = round(plane.p2c((x_grid[i].get_x(), 0, 0))[0] / plane.x_range[2], 12) % (unit_count + 1) == 0

        if (isPrimaryStroke):
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
        x_grid_lines.append(line)

    return VGroup(*(y_grid_lines + x_grid_lines))