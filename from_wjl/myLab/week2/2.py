
from manimlib.imports import *

def funcA(x):
    return (np.log(np.sqrt(x ** 2 + 1) + x) -3*x) / (x ** 2 + 1)
def funcB(x):
    return (np.log(np.sqrt(x ** 2 + 1) -x) +3*x) / (x ** 2 + 1)
def funcC(x):
    return abs(np.log(np.sqrt(x ** 2 + 1) -x) +3*x) / (x ** 2 + 1)
def funcD(x):
    return -abs(np.log(np.sqrt(x ** 2 + 1) -x) +3*x) / (x ** 2 + 1)

class Scene1(GraphScene):
    CONFIG = {
        "y_max" : 2,
        "y_min" : -2,
        "x_max" : 5,
        "x_min" : -5,
        # x,y 轴分别的刻度
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 2, 
        "axes_color" : BLUE, 
        "y_label_direction": RIGHT,
        "x_label_direction": UP,
        "x_axis_width": 2.5,
        "y_axis_height": 1.5,
    }

    def plot(self, func, pos, letter):
        # 注意坐标轴设置要在 setup_axes 调用之前
        if (any(pos)):
            self.graph_origin=pos
        self.setup_axes(animate=True)
        graph = self.get_graph(func,  
            color = GREEN,
            x_min = -5, 
            x_max = 5
        )
        label = TexMobject(letter)
        label.next_to(self.x_axis, DOWN, 1)
        vline = self.get_vertical_line_to_graph(x=1, graph=graph, color=RED)
        self.add(vline)
        self.add(label)
        self.add(graph)
        self.wait()
        return graph, label, self.axes, vline
    def rotateFunc(self, func, pos):
        if (any(pos)):
            self.graph_origin=pos
        self.setup_axes(animate=True)
        rGraph = self.get_graph(func,  
            color = YELLOW,
            x_min = -5, 
            x_max = 5
        )
        self.add(rGraph)
        for i in range(10):
            rGraph.rotate(TAU / 20, axis=OUT, about_point=self.coords_to_point(0,0))
            self.wait()
        return rGraph, self.axes

    def construct(self):
        # 
        text = TextMobject("函数f(x)=","$\\frac{ln(\\sqrt{x^2+1} + x ) - 3x}{x^2 + 1}$", "的图像大致为？")
        text.shift(LEFT + 3*UP)
        self.play(Write(text))
        self.wait()
        fa,la,aa, vla = self.plot(funcA, 5 * LEFT, 'A')
        groupA = VGroup(fa,la,aa, vla)
        fb,lb,ab, vlb = self.plot(funcB, 2 * LEFT, 'B')
        groupB = VGroup(fb,lb,ab, vlb)
        fc,lc,ac, vlc = self.plot(funcC, RIGHT, 'C')
        groupC = VGroup(fc,lc,ac, vlc)
        fd,ld,ad, vld = self.plot(funcD, 4 * RIGHT, 'D')
        groupD = VGroup(fd,ld,ad, vld)
        
        text2 = TextMobject("f(-x)=","$\\frac{ln(\\sqrt{(x)^2+1} - x ) + 3x}{(x)^2 + 1}$","= f(-x) = -f(x)。")
        text2.shift(LEFT + 3 * UP)
        text3 = TextMobject("奇函数，图像关于原点旋转180°重合:")
        text3.next_to(text2[0], DOWN, aligned_edge=LEFT)
        vgroup = VGroup(text2, text3)
        self.play(ReplacementTransform(text, vgroup))
        self.wait()
        rGraphA, axesA = self.rotateFunc(funcA, 5 * LEFT)
        groupA_2 = VGroup(rGraphA, axesA)
        rGraphB, axesB = self.rotateFunc(funcB, 2 * LEFT)
        groupB_2 = VGroup(rGraphB, axesB)
        rGraphC, axesC = self.rotateFunc(funcC, RIGHT)
        groupC_2 = VGroup(rGraphC, axesC)
        rGraphD, axesD = self.rotateFunc(funcD, 4 * RIGHT)
        groupD_2 = VGroup(rGraphD, axesD)
        
        text4 = TextMobject("排除 C 和 D 选项")
        text4.shift(LEFT + 3 * UP)
        self.play(FadeOut(vgroup))
        self.wait()
        self.play(Write(text4))
        self.wait()
        self.play(FadeOut(groupC))
        self.play(FadeOut(groupC_2))
        self.wait()
        self.play(FadeOut(groupD))
        self.play(FadeOut(groupD_2))
        self.wait()
        
        text5 = TextMobject("f(1)=$\\frac{ln(\\sqrt{2} + 1)-3}{2}$")
        text5.shift(LEFT + 3 * UP)
        self.play(ReplacementTransform(text4, text5))
        self.wait()
        text6 = TextMobject("我们对这个式子做近似计算:")
        text6.shift(LEFT + 3 * UP)
        self.play(ReplacementTransform(text5, text6))
        self.wait()
        text7 = TextMobject("由 $ln(\\sqrt{2} + 1)$", "$\\approx \\log_{2.7}{2.4}$", "$<\\log_{2.7}{2.7}=1$")
        text7.shift(LEFT + 3 * UP)
        self.play(ReplacementTransform(text6, text7))
        self.wait()
        # 
        text8 = TextMobject("$\\therefore \\frac{ln(\\sqrt{2} + 1)-3}{2} < 0$", "即 f(1) < 0, 最后选择 A")
        text8.next_to(text7[0], DOWN, aligned_edge=LEFT)
        self.play(Write(text8))
        self.play(FadeOut(groupB))
        self.play(FadeOut(groupB_2))
        self.wait()
        # 
        self.remove(rGraphA, axesA)
        self.wait()
        


