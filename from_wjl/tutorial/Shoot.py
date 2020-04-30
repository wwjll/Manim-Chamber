'''
    1.形状组合
    2.Mobject.next_to 方法
    3.补帧动画, ApplyMethod 
'''
from manimlib.imports import *

class Shoot(Scene):
    def construct(self):
        # 创建瞄准器
        circle01 = Circle(color = BLUE)
        circle02 = Circle(color = RED, fill_color = RED, fill_opacity = 1)
        circle02.scale(0.1)
        line01 = Line(np.array([-1, 0, 0]), np.array([1, 0, 0]), color = RED)
        line02 = Line(np.array([0, -1, 0]), np.array([0, 1, 0]), color = RED)
        aim_scope = VGroup(circle01, circle02, line01, line02)

        # 创建靶点
        target_list = []
        for i in range(3):
            for j in range(5):
                target_ij = Circle(color = YELLOW, fill_color = YELLOW, fill_opacity = 0.4)
                target_ij.scale(0.4)
                target_ij.shift(np.array([-4 + j * 2, -2 + i * 2, 0]))
                self.play(FadeIn(target_ij))
                target_list.append(target_ij)
        self.wait(1)

        # 射击动作
        def shoot_ij(i, j):
            target_ij = target_list[j + i]
            # 补帧动画准星移到目标位置
            self.play(ApplyMethod(aim_scope.next_to, target_ij, 0))
            self.play(ApplyMethod(target_ij.set_fill, GREY), ApplyMethod(target_ij.set_color, GREY))
            self.wait(0.5)
            ij = TextMobject("(%d, %d)" % (i, j), color = GREY)
            ij.next_to(target_ij, DOWN)
            self.play(Write(ij))
            self.wait(1)
            return 0
        
        self.add(aim_scope)
        self.play(ApplyMethod(aim_scope.shift, DOWN * 3 + LEFT * 6.1))
        shoot_ij(0 , 1)
        shoot_ij(0 , 2)
        shoot_ij(0 , 3)
