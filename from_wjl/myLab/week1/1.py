from manimlib.imports import *

class Plot1(GraphScene):
    CONFIG = {
        "y_max" : 100,
        "y_min" : 0,
        "x_max" : 10,
        "x_min" : 0,
        # x,y 轴分别的刻度
        "y_tick_frequency" : 10, 
        "x_tick_frequency" : 1, 
        "axes_color" : BLUE, 
        "y_label_direction": RIGHT,
        "x_label_direction": UP,
        # 设置图像原始位置
        "graph_origin": 3 * DOWN + 6 * LEFT,
    }
    # 定义本图像函数
    def func(self, x):
        return x**2

    def construct(self):
        self.setup_axes(animate=True)
        # 创建坐标轴和函数图像
        graph = self.get_graph(self.func,  
            color = GREEN,
            x_min = 4, 
            x_max = 10
        )
        # 默认label "f(x)" 的显示位置
        graph_label = self.get_graph_label(graph, x_val = 10, direction=UP/4)
        # 
        text1 = TextMobject("设函数f(x)的定义域为D")
        text1.scale(0.8)
        text1.next_to(self.coords_to_point(1, 80))
        # 第一幕
        self.play(
        	ShowCreation(graph),
            Write(graph_label),
            ShowCreation(text1),
            run_time = 2
        )
        self.wait()

        # 第二幕
        self.play(FadeOut(text1))
        self.wait()
        text2 = TextMobject("取区间I，且$I\subset D$")
        text2.scale(0.8)
        text2.next_to(self.coords_to_point(1, 80))
        # 画两条垂直 x 轴垂线
        v_dashed_line1 = DashedLine(start=self.coords_to_point(4, 0), 
            end=self.coords_to_point(4, 16), color=BLUE)
        v_dashed_line2 = DashedLine(start=self.coords_to_point(9, 0), 
            end=self.coords_to_point(9, 81), color=BLUE)
        VGroup2 = VGroup(v_dashed_line1, v_dashed_line2)
        # 截取图像范围
        graph2 = self.get_graph(func=self.func, x_min=4, x_max=9, color=RED)
        self.play(
            ShowCreation(text2),
            ShowCreation(graph2),
            ShowCreation(VGroup2),
            run_time = 2
        )

        # 第三幕
        self.play(
            FadeOut(text2),
            FadeOut(VGroup2),
        )
        self.wait()
        text3 = TextMobject("任取$x_1$和$x_2\subset I$,且$x_1<x_2$")
        text3.scale(0.8)
        text3.next_to(self.coords_to_point(1, 80))
        # 四条坐标轴垂线
        v_dashed_line3 = DashedLine(start=self.coords_to_point(5, 0), 
            end=self.coords_to_point(5, 25), color=BLUE)
        v_dashed_line4 = DashedLine(start=self.coords_to_point(8, 0), 
            end=self.coords_to_point(8, 64), color=BLUE)
        v_dashed_line5 = DashedLine(start=self.coords_to_point(0, 25), 
            end=self.coords_to_point(5, 25), color=BLUE)
        v_dashed_line6 = DashedLine(start=self.coords_to_point(0, 64), 
            end=self.coords_to_point(8, 64), color=BLUE)
        VGroup3 = VGroup(v_dashed_line3, v_dashed_line4, v_dashed_line5, v_dashed_line6)
        # 在函数图像上绘制两个点
        p1 = Dot()
        p2 = Dot()
        p1.move_to(self.coords_to_point(5, 25))
        p2.move_to(self.coords_to_point(8, 64))
        VGroup3_1 = VGroup(p1, p2)
        # 点坐标
        text4 = TextMobject("(x1, y1)")
        text5 = TextMobject("(x2, y2)")
        text4.scale(0.8)
        text5.scale(0.8)
        text4.next_to(self.coords_to_point(5, self.func(5)+7), direction=LEFT)
        text5.next_to(self.coords_to_point(8, self.func(8)+7), direction=LEFT)
        VGroup3_2 = VGroup(text4, text5)
        self.play(
            ShowCreation(text3),
            ShowCreation(VGroup3_1),
            ShowCreation(VGroup3),
            ShowCreation(VGroup3_2),
            run_time = 2
        )
        self.wait()

        # 第四幕
        self.play(
            FadeOut(text3),
        )
        self.wait()

class Plot2(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_tick_frequency": 1,
        "y_min": 0,
        "y_max": 100,
        "y_tick_frequency": 10,
        "graph_origin": 3 * DOWN + 6 * LEFT,
    }

    def func(self, x):
        return 100/x
    def construct(self):
        self.setup_axes(animate=True)
        # 创建坐标轴和函数图像
        graph = self.get_graph(self.func,  
            color = GREEN,
            x_min = 2, 
            x_max = 5
        )
        graph_label = self.get_graph_label(graph, x_val=1, direction=RIGHT)
        # 创建两个点
        d1 = Dot()
        d2 = Dot()
        d1.move_to(self.coords_to_point(2, 50-1), DOWN)
        d2.move_to(self.coords_to_point(5, 20-1), DOWN)
        # 创建两条虚线
        dash_line1 = DashedLine(start=self.coords_to_point(
            2, 0), end=self.coords_to_point(2, 50), color=BLUE)
        dash_line2 = DashedLine(start=self.coords_to_point(
            2, 0), end=self.coords_to_point(2, 50), color=BLUE)
        dash_line3 = DashedLine(start=self.coords_to_point(
            5, 0), end=self.coords_to_point(5, 20), color=BLUE)
        dash_line4 = DashedLine(start=self.coords_to_point(
            0, 20), end=self.coords_to_point(5, 20), color=BLUE)
        # 创建标注
        text1 = TextMobject("$(x_1,y_1)$")
        text2 = TextMobject("$(x_2,y_2)$")
        text1.scale(0.7)
        text2.scale(0.7)
        text1.next_to(self.coords_to_point(2, 50), direction=RIGHT)
        text2.next_to(self.coords_to_point(5, 24), direction=RIGHT)
        self.add(graph, graph_label, d1, d2, dash_line1,
                dash_line2, dash_line3, dash_line4, text1, text2)
        self.wait()

        # 标注
        text3 = TextMobject("同理，若$f(x_1)>f(x_2)$", "则$f(x)$在区间I上单调递减")
        text3.scale(0.8)
        text3[0].next_to(self.coords_to_point(5, 80))
        text3[1].next_to(self.coords_to_point(5, 80))
        self.wait(3)
        self.play(Write(text3[0]))
        self.wait(3)
        self.play(FadeOut(text3[0]))
        self.wait()
        self.play(Write(text3[1]))
        self.wait(4)

class Question(Scene):
    def construct(self):
        text1 = TextMobject("Q:怎么证明一个函数在某个区间的单调性？", height=8, width=8)
        text2 = TexMobject("Example:", "y", "=", "x", "+",
                           "\\ln{x}", ",", "x\\in \\left(0,+\\infty \\right)")
        text3 = TextMobject("证明：")
        text4 = TextMobject("在$(0,+\\infty \\right)$任取$x_1$和$x_2$,且$x_1<x_2$")
        text5 = TexMobject("y_1", "=", "x_1", "+", "\\ln", "{x_1}")
        text6 = TexMobject("y_2", "=", "x_2", "+", "\\ln", "{x_2}")
        text7 = TexMobject("y_1", "-", "y_2", "=",
                           "\\left( x_1-x_2 \\right)+ \\left( \\ln{x_1}-\\ln{x_2} \\right)"),
        text8 = TexMobject("=", "x_1", "-", "x_2", "+",
                           "\\ln{", "{x_1}", "\\over", "{x_2}","}")
        text9 = TexMobject("\\because  x_1<x_2")
        text10 = TexMobject("\\therefore ", "x_1-x_2<0",
                            ",", "\\frac{x_1}{x_2}<1")
        text11 = TextMobject("$\\therefore$","$\\ln{\\frac{x_1}{x_2}}$","<","0")
        text12 = TextMobject("$\\therefore$","$y_1 < y_2$")
        text13 = TextMobject("$\\therefore$", "y函数在$(0,+\infty)$上递增")
        text_group1_2 = VGroup(text1, text2)
        text_group1_2.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.5
        )
        text_group1_2.move_to(np.array([0, 1, 0]))
        self.play(Write(text1))
        self.wait(3)
        self.play(
            Transform(text1, text2)
        )
        transform_text = TexMobject("y", "=", "x", "+",
                                    "\\ln{x}", ",", "x\\in \\left(0,+\\infty \\right)")
        transform_text.move_to(np.array([-4, 3, 0]))
        self.wait(3)
        self.play(
            Transform(text1, transform_text)
        )
        self.wait(3)
        text3.move_to(transform_text.get_center()+1*DOWN+2.5*LEFT)
        self.play(Write(text3))
        self.wait(3)

        text4.move_to(np.array([-1, 2, 0]))
        self.play(FadeInFrom(text4, UP))
        self.wait(3)
        text5.move_to(np.array([-3.5, 1, 0]))
        self.play(Write(text5))
        self.wait(3)
        text6.move_to(np.array([-3.5, 0, 0]))
        # self.play(ReplacementTransform(text5.copy(), text6))
        self.play(
            Transform(text5[1].copy(),text6[1]),
            Transform(text5[3].copy(),text6[3]),
            Transform(text5[4].copy(),text6[4])
        )
        self.wait(1)
        self.play(
            Transform(text5[0].copy(),text6[0]),
            Transform(text5[2].copy(),text6[2]),
            Transform(text5[5].copy(),text6[5])
        )
        transform_text7 = TexMobject("y_1", "-", "y_2", "=",
                                     "\\left( x_1-x_2 \\right)+ \\left( \\ln{x_1}-\\ln{x_2} \\right)")
        transform_text7.move_to(np.array([-1.5, -1, 0]))
        self.wait(3)
        self.play(ReplacementTransform(text6.copy(), transform_text7))
        self.wait(3)

        text8.move_to(np.array([-1.8, -2, 0]))
        self.play(Write(text8))

        transform_text8 = TexMobject(
            "y_1-y_2=x_1-x_2+ln{{x_1}\\over{x_2}}")
        transform_text8.move_to(transform_text7.get_center()+2*LEFT)
        self.wait(3)
        self.play(
            FadeOut(transform_text7),
            ReplacementTransform(text8, transform_text8)
        )
        self.wait()
        text9.move_to(transform_text8.get_center()+1*DOWN+0.5*LEFT)
        self.play(Write(text9))
        text10.move_to(text9.get_center()+1*DOWN+1.4*RIGHT)
        self.wait()
        self.play(Write(text10))
        text11.move_to(text10.get_center()+1.5*LEFT)
        self.wait(3)
        self.play(ReplacementTransform(text10,text11))
        text12.move_to(text10.get_center())
        self.wait(3)
        self.play(ReplacementTransform(text11,text12))
        self.wait(3)
        text13.move_to(text12.get_center()+7*RIGHT)
        self.play(ReplacementTransform(text12.copy(),text13))