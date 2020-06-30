from manimlib.imports import *


class Sector1(Scene):

    def construct(self):
        texts = VGroup(TextMobject("圆心角为60$^{\\circ}$的扇形$OAB$, $C$是$\\stackrel\\frown{AB}$上一点"),
                       TextMobject("$CD\\bot OB$于$D$, 求$S\\triangle OCD\\max$")).arrange(DOWN).to_corner(UP)

        arc = Arc(start_angle=math.radians(60), angle=math.radians(-60), radius=2)
        start = arc.get_start()
        end = arc.get_end()
        line = Line(ORIGIN, start)
        line2 = Line(ORIGIN, end)
        line3 = line.copy().rotate_about_origin(math.radians(-10))
        end2 = line3.get_end()
        end3 = RIGHT * 1.28
        line4 = Line(UP * 1.5, ORIGIN).shift(end3)

        symbols = VGroup(
            TexMobject("O").scale(0.5).shift(LEFT * 0.1 + DOWN * 0.1),
            TexMobject("A").scale(0.5).shift(start + UP * 0.14),
            TexMobject("B").scale(0.5).shift(end + RIGHT * 0.1),
            TexMobject("C").shift(end2 + RIGHT * 0.12 + UP * 0.12).scale(0.5),
            TexMobject("D").shift(end3 + DOWN * 0.12).scale(0.5)
        )

        triangle = Group(line3, line4, Line(ORIGIN, end3))
        point = SmallDot().scale(0.8)
        pic = Group(Group(line, arc, line2), SmallDot().scale(0.8).shift(end2), triangle, point)
        full = Group(pic, symbols)
        Group(texts, full).arrange(DOWN).to_corner(UP)

        self.play(ShowCreation(pic))
        self.play(Write(symbols))
        self.play(Write(texts))
        self.wait(5)
        self.clear()
        full.scale(1.2).to_corner(LEFT + UP)
        self.add(full)

        texts = VGroup(TextMobject("注意到$OA=OB$, 又$\\angle$AOB=60$^{\\circ}$"), TextMobject("所以想到旋转(等边三角形题特性)"),
                       TextMobject("当然你也可以看到边相等想到旋转")).arrange(DOWN)

        Group(full, texts).arrange(RIGHT, False)
        self.play(Write(texts))
        triangle = triangle.copy()
        self.play(ApplyMethod(triangle.rotate_about_point, math.radians(-50), line3.get_start()))
        e = triangle.submobjects.__getitem__(1).get_end()
        self.play(ShowCreation(SmallDot(e)))
        self.play(Write(TexMobject("E").shift(e + DOWN * 0.16).scale(0.5)))

        texts2 = VGroup(TextMobject("旋转得$\\triangle OBE$"), TexMobject("\\because\\angle ODC=\\angle OEB=90^{\\circ}")).arrange(DOWN)
        texts3 = VGroup(TextMobject("或者连接$EF$"),
                        TextMobject("直角三角形斜边上的中线等于斜边的一半等于$r$"),
                        TextMobject("由圆的定义“到定点距离相等的点集“得上述")).arrange(DOWN)
        text = TextMobject("$\\therefore E$在以$OB$为直径的$\\odot F$上")
        text2 = TextMobject("$\\therefore EG$为半弦, 半弦最大为$r$, 即解")
        text3 = TextMobject("但是设$OD$为$x$, 勾股定理, 配方也行:(")
        Group(texts, texts2, text, texts3, text2).arrange(DOWN, False)
        self.play(Write(texts2))
        o = line2.get_center()
        self.play(ShowCreation(SmallDot(o)))
        self.play(Write(TexMobject("F").shift(o + DOWN * 0.16 + RIGHT * 0.1).scale(0.5)))
        self.play(ShowCreation(Circle(arc_center=line2.get_center(), color=WHITE).scale(1.2)))
        self.play(Write(text))
        self.play(ShowCreation(Line(e, o)))
        self.play(Write(texts3))
        g = e + UP * 1.185
        self.play(ShowCreation(Line(g, e)))
        self.play(ShowCreation(SmallDot(g)))
        self.play(Write(TexMobject("G").scale(0.5).shift(g + UP * 0.16)))
        self.play(Write(text2))
        self.wait(5)
        self.clear()
        self.play(Write(text3))
        self.wait(2)
