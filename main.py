from manim import *
from utils.grid import *

class Intro(Scene):
    def construct(self):
        text = Text("Domain Name")

        # 화면 중앙에 위치시키기
        text.move_to(ORIGIN)

        # 초기 텍스트 추가
        self.play(Write(text))
        self.wait(2)
        
        new_text = VGroup(
            Text("What is "),
            Text("Domain Name"),
            Text("?")
        )

        # 초기 텍스트 뒤에 위치시키기
        new_text[1].move_to(text)

        new_text[0].next_to(new_text[1], LEFT)
        new_text[2].next_to(new_text[1], RIGHT)

        x = new_text.get_center()[0]

        new_text[0].shift((-x, 0, 0))
        new_text[1].shift((-x, 0, 0))
        new_text[2].shift((-x, 0, 0))

        # 텍스트 애니메이션
        self.play(
            Write(new_text[0]),
            Write(new_text[2]),
            text.animate.shift((-x, 0, 0))
        )

        # 애니메이션 완료 후 대기
        self.wait()
