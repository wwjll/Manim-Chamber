'''
    # latex语法使用
    1.manim 里有 TextMobject 和 TexMobject两种对象
    2.表示一个公式内: $$
    3.注意转义使用r"string"或、\\str来防止转义
    4.空格 \quad, 省略号 \dots
'''
from manimlib.imports import *
class Latex(Scene):
    def construct(self):
        # Making Objects
        equal = TextMobject("=", color=RED)
        
        eq_left01 = TextMobject(r"$1^3+2^3+3^3+\quad\dots\quad+n^3$", color=GREEN)
        eq_right01 = TextMobject("$(1+2+3+\\quad\\dots\\quad+n)^2$", color=YELLOW)
        
        eq_left02 = TextMobject(r"$\Sigma_{i=1}^{n} i^{3}$", color=GREEN)
        eq_right02 = TextMobject(r"$(\Sigma_{i=1}^{n} i)^{2}$", color=YELLOW)
        equation02 = VGroup(equal, eq_left02, eq_right02)
        
        # Position
        eq_left01.next_to(equal, LEFT)
        eq_right01.next_to(equal, RIGHT)
        eq_left02.next_to(equal, LEFT)
        eq_right02.next_to(equal, RIGHT)

        # Animation
        self.play(FadeIn(eq_left01), FadeIn(equal), FadeIn(eq_right01))
        self.wait(1)
        self.play(ReplacementTransform(eq_left01, eq_left02))
        self.play(ReplacementTransform(eq_right01, eq_right02))
        self.wait(1)
        self.play(ApplyMethod(equation02.scale, 2.4))
        self.wait(1)


