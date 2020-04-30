'''
    1.文字对象TextMobject对象的基本使用
    2.几种常用文字动画(Write， FadeIn, FadeOut)
    3.组定义vGroup的使用
'''

# 一次性导入 manimlib 的众多依赖包
from manimlib.imports import *
class Hello_Manim(Scene):
    def construct(self):
        helloworld = TextMobject("Hello World", color = RED)
        helloworld2 = TextMobject("GoodBye World", color = YELLOW)
        # self.play(Write(helloworld))
        # self.play(FadeIn(helloworld))
        # self.play(FadeOut(helloworld))
        # self.play(Transform(helloworld, helloworld2))

        rectangle = Rectangle(color = BLUE)
        # 包裹
        rectangle.surround(helloworld)
        group1 = VGroup(helloworld, rectangle)
        # 
        self.play(FadeIn(rectangle))
        # group1放大2.5倍
        self.play(ApplyMethod(group1.scale, 2.5))
        self.wait(1)