'''
    1.形状组合
    2.shift的使用,shift是相对坐标移动,move_to是绝对坐标移动
'''
from manimlib.imports import *
class Basic_Shapes(Scene):
    def construct(self):
        # 定义一些对象
        ring = Annulus(inner_radius = .4, outer_radius = 1, color = BLUE)
        square = Square(color = ORANGE, fill_color = ORANGE, fill_opacity = 0.5)
        rect = Rectangle(height = 3.2, width = 1.2, color = PINK, fill_color = PINK, fill_opacity = 0.5)

        line01 = Line(np.array([0, 3.6, 0]), np.array([0, 2, 0]), color = BLUE)
        line02 = Line(np.array([-1, 2, 0]), np.array([-1, -1, 0]), color = BLUE)
        line03 = Line(np.array([1, 2, 0]), np.array([1, 0.5, 0]), color = BLUE)

        # 位置, shift() 方法是相对当前位置的移动, 对应点方向向量如下
        # UP: (0,1,0)、DOWN: (0,-1,0)、LEFT: (-1,0,0)、RIGHT: (1,0,0)、IN: (0,0,-1)、OUT: (0,0,1)
        ring.shift(UP * 2) 
        square.shift(LEFT + DOWN * 2)
        rect.shift(RIGHT + DOWN * (3.2/2 - 0.5))

        # 展示
        self.add(line01)
        self.play(GrowFromCenter(ring))
        self.wait(0.5)
        self.play(FadeIn(line02), FadeIn(line03))
        self.wait(0.5)
        self.play(FadeInFromDown(square))
        self.play(FadeInFromDown(rect))
        self.wait()


