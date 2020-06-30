'''
   2.get_corner(),获取角落位置，eg:get_corner(UP + LEFT)
   3.to_edge,相对边缘的位置
'''
from manimlib.imports import *

class Quote(Scene):
    def construct(self):
        quote = TextMobject("为什么我喜欢数学？")
        quote.set_color(RED)
        quote.to_edge(LEFT)
        quote2 = TextMobject("因为用Manim制作动画很好玩")
        quote2.set_color(BLUE)
        author = TextMobject("-鲁迅", color = PINK)
        
        author.next_to(quote.get_corner(DOWN + RIGHT), DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote, quote2), 
            ApplyMethod(author.move_to, quote2.get_corner(DOWN + RIGHT) + DOWN + 2 * LEFT))
        self.play(ApplyMethod(author.scale, 1.6))
        author.match_color(quote2)
        self.play(FadeOut(quote), FadeOut(author))
        self.wait()
