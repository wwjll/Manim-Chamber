'''
   1.创建动画 showCreation
'''
from manimlib.imports import *

class Simple_Anim(Scene):
    def construct(self):
        # Making Objects
        circle01 = Circle(color = RED, fill_color = RED, fill_opacity = 0.5)
        circle02 = Circle(color = RED, fill_color = RED, fill_opacity = 0.5)
        square01 = Square(color = RED, fill_color = RED, fill_opacity = 0.5)
        love = VGroup(circle01, circle02, square01)

        rect01 = Rectangle(width = 4, height = 0.8, color = RED, fill_color = RED, fill_opacity = 0.5)
        rect02 = Rectangle(width = 4, height = 0.8, color = RED, fill_color = RED, fill_opacity = 0.5)
        hate = VGroup(rect01, rect02)

        square02 = Square(color = RED, fill_color = BLACK, fill_opacity = 0.5)
        eye01 = Circle(color = RED, fill_color = BLACK, fill_opacity = 0.5)
        eye02 = Circle(color = RED, fill_color = BLACK, fill_opacity = 0.5)
        square02.scale(2)
        eye01.scale(0.45)
        eye02.scale(0.45)
        face = VGroup(square02, eye01, eye02)

        line01 = Line(np.array([-6, -2.4, 0]), np.array([6, 2.4, 0]), color = RED)
        line01.set_height(0.2)

        text01 = TextMobject("LOVE\nHATE\nFACE\n")
        text01.scale(1.8)

        all_group = VGroup(love, hate, face, line01, text01)

        # Position
        circle01.shift((UP + LEFT) * np.sqrt(2) / 2)
        circle02.shift((UP + RIGHT) * np.sqrt(2) / 2)
        square01.rotate(np.pi / 4)
        rect01.rotate(np.pi / 4)
        rect02.rotate(-np.pi / 4)

        eye01.shift(np.array([-0.72, 0.6, 0]))
        eye02.shift(np.array([0.72, 0.6, 0]))
        face.shift(RIGHT * 4)

        text01.shift(DOWN * 2.5)

        # Show Objects
        self.play(ShowCreation(circle01), ShowCreation(circle02), ShowCreation(square01))

        self.wait(1)
        self.play(ApplyMethod(love.shift, LEFT * 4))
        self.wait(1)

        self.play(ShowCreation(rect01), ShowCreation(rect02))
        self.wait(1)

        self.play(ShowCreation(square02))
        self.play(ShowCreation(eye01), ShowCreation(eye02))
        self.wait(1)

        self.play(ApplyMethod(love.set_opacity, 1), ApplyMethod(hate.set_opacity, 1), 
        ApplyMethod(face.set_opacity, 1))
        self.wait(1)
        self.play(ShowCreation(line01))
        self.wait(1)

        self.play(Transform(line01, text01))
        self.wait(1)
        self.play(ApplyMethod(all_group.shift, UP * 0.5))
        self.wait(1)




