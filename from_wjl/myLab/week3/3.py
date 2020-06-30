from manimlib.imports import *
# 变量使用下划线命名

class Scene1(Scene):
    def construct(self):
        # grid = NumberPlane(
        #     axis_config = {
        #         "stroke_color": BLACK
        #     }
        # )
        # self.add(grid)
        scale_text = 0.6
        question = TextMobject("如图，在三角形$\\Delta A B C$中，B = $\\frac{\pi }{4} $，BC 边上的高为 $\\frac{1}{3} BC$，求 $\\sin A$。")
        question.scale(0.8)
        question.shift(3 * UP)
        
        point_a = np.array([-5, 2, 0])
        point_b = np.array([-6, 1, 0])
        point_c = np.array([-3, 1, 0])
        point_h = np.array([-5, 1, 0])
        triangle = Polygon(point_a, point_b, point_c)
        triangle.set_stroke(color=WHITE, width=2)
        self.add(triangle)

        labelA = TextMobject("A")
        labelA.move_to(point_a, aligned_edge=DOWN)
        labelB = TextMobject("B")
        labelB.move_to(point_b, aligned_edge=RIGHT)
        labelC = TextMobject("C")
        labelC.move_to(point_c, aligned_edge=LEFT)
        labelH = TextMobject("H")
        labelH.move_to(point_h, aligned_edge=UP)
        labelA.scale(0.5)
        labelB.scale(0.5)
        labelC.scale(0.5)
        labelH.scale(0.5)
        self.add(labelA, labelB, labelC, labelH)
        
        h_line = DashedLine(
            start=point_a, 
            end=point_h, 
            color=WHITE
        )
        self.add(h_line)

        arc1 = Arc(
            arc_center = point_b,
            radius = 0.3,
            stroke_width = 2,
            start_angle = 0 * DEGREES,
            angle = 45 * DEGREES,
            color = WHITE
        )
        angle_b = TextMobject("45°")
        angle_b.next_to(arc1, RIGHT, aligned_edge=RIGHT)
        angle_b.scale(0.5)
        self.add(arc1)
        self.add(angle_b)


        self.play(Write(question))
        self.wait()

        stepText1 = TextMobject('由','$\\angle {BAH}=45°  \\quad AH = \\frac {1}{3} BC  \\quad HC = \\frac{2}{3}BC$ ')
        stepText2 = TextMobject('$\\therefore AB = \\frac{ \\sqrt{2} }{3}BC \\quad AC = \\frac{ \\sqrt{5} }{3}BC$')  
        stepText4 = TextMobject('由余弦定理','$cosA = \\sqrt{\\frac{AB^2 + AC^2 - BC^2}{2*AB*AC}}$')
        stepText5 = TextMobject('$= \\sqrt{\\frac{(\\frac{\\sqrt{2}}{3}BC)^2 + (\\frac{\\sqrt{5}}{3}BC)^2 - BC^2}{2*\\frac{\\sqrt{2}}{3}BC * \\frac{\\sqrt{5}}{3}BC }}$')
        stepText6 = TextMobject('$= \\sqrt{\\frac{(\\frac{4}{9})^2 + (\\frac{5}{9})^2 - 1}{2*\\frac{2}{9} * \\frac{5}{9} }}$')
        stepText7 = TextMobject('$=-\\frac{\\sqrt{10}}{10}$')
        
        stepText1.scale(scale_text)
        stepText2.scale(scale_text)
        stepText4.scale(scale_text)
        stepText5.scale(scale_text)
        stepText6.scale(scale_text)
        stepText7.scale(scale_text)
        stepText1.move_to(LEFT * 3 + 0.2 * UP)
        stepText2.next_to(stepText1, DOWN)
        stepText2.align_to(stepText1, LEFT)
        stepText4.next_to(stepText2, DOWN)
        stepText4.align_to(stepText2, LEFT)
        stepText5.next_to(stepText4, DOWN)
        stepText5.align_to(stepText4, LEFT)
        stepText6.next_to(stepText5, RIGHT)
        stepText7.next_to(stepText6, RIGHT)
        
        scene_text_group = VGroup(stepText1,stepText2,stepText4,stepText5,stepText6,stepText7)

        self.play(Write(stepText1))
        self.wait()
        self.play(Write(stepText2))
        self.wait()
        # 求得AB
        line_ab = Line(
            start = point_a,
            end = point_b,
            color = YELLOW,
            stroke_width = 2
        )
        label_ab = TextMobject("AB = $\\frac{\\sqrt{2}}{3}BC$")
        label_ab.scale(0.5)
        label_ab.set_color(RED)
        label_ab.move_to(line_ab.get_center() + 0.5 * LEFT + 0.3 * UP)
        self.play(ShowCreation(line_ab))
        self.wait()
        self.play(ShowCreation(label_ab))
        self.wait()
        # 求得AC
        line_ac = Line(
            start = point_a,
            end = point_c,
            color = YELLOW,
            stroke_width = 2
        )
        label_ac = TextMobject("AC = $\\frac{\\sqrt{5}}{3}BC$")
        label_ac.scale(0.5)
        label_ac.set_color(RED)
        label_ac.move_to(line_ac.get_center() + 0.5 * RIGHT + 0.3 * UP)
        self.play(ShowCreation(line_ac))
        self.wait()
        self.play(ShowCreation(label_ac))
        self.wait()

        self.play(Write(stepText4))
        self.wait()

        self.play(Write(stepText5))
        self.wait()

        self.play(Write(stepText6))
        self.wait()

        self.play(Write(stepText7))
        self.wait()

        self.play(FadeOut(scene_text_group))
        self.wait()
        self.remove(scene_text_group)

        result_text = TextMobject('在','$\\Delta A B C中，0° < \\angle A < 180°$')
        result_text2 = TextMobject('$\\therefore sinA = \\sqrt{1 - cos^2 A} = \\frac{3 \\sqrt{10}}{10}$')
        result_text.move_to(LEFT * 4 + 0.2 * UP)
        result_text.scale(scale_text)
        result_text2.scale(scale_text)
        result_text2.next_to(result_text[0], DOWN)
        result_text2.align_to(result_text[0], LEFT)
        self.play(Write(result_text))
        self.wait()
        self.play(Write(result_text2))
        self.wait()