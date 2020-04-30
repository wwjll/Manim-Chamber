from manimlib.imports import *

class PieChart(Scene):
    CONFIG = {
            'start_per' : 0,
            'r' : 2,
            'gap' : TAU * 2 / 1000,
            'stroke' : 100,
            'legend_style' : 'Dot',
            'legend_loc' : RIGHT * 3.6 + UP * 0.1,
            'legend_scale' : 0.65
    }
    # 由给定参数绘制一个扇形区域
    def create_arc(self, percentage, arc_color):
        arc = Arc(radius = self.r, start_angle = self.start_per / 100 * TAU, \
            angle = percentage / 100 * TAU - self.gap, color=arc_color, stroke_width=self.stroke)
        self.start_per += percentage
        return arc

    # 
    def create_arcs(self, *args):
        arc_group = VGroup()
        for per, color, name in args:
            arc_group.add(self.create_arc(per, color))
        self.arcs = arc_group
        return self.arcs

    # 由给定参数生成文字标签
    def create_legend(self, arc_color, name):
        text_str = name
        text = TextMobject(text_str)

        if self.legend_style == 'Rect':
            color = Square(color = arc_color, fill_color = arc_color,
                fill_opacity = 1).scale(0.16)
            color.shift(self.legend_loc)
            text.next_to(color, RIGHT * 0.75)
            return VGroup(color, text)
        elif self.legend_style == 'Dot':
            color = Dot(color = arc_color).scale(2.5)
            color.shift(self.legend_loc)
            text.next_to(color, RIGHT)
            return VGroup(color, text)

    # 
    def create_legends(self, *args):
        legend_group = VGroup()
        i = 0
        length = len(args) - 1
        for (per, color, name) in args:
            legend_group.add(self.create_legend(color, name).shift(DOWN * 0.7 * (i - length / 2)))
            i += 1
        self.legends = legend_group.scale(self.legend_scale)
        return self.legends

    # 
    def create_title(self, title):
        self.title = TextMobject(title)
        title.shift(UP)
        return self.title

    # 
    def create_anim(self, title, *args):
        self.create_title(title)
        self.create_arcs(*args)
        self.create_legends(*args)

        self.play(ShowCreation(self.arcs))
        self.wait(0.5)
        self.play(ApplyMethod(self.arcs.shift, LEFT * 2.4))
        self.play(Write(self.title.shift(UP * 0.75)))

        i = 0
        per_group = VGroup()
        for (per, color, name) in args:
            text_str = name + '%.2f' % per + '\%'
            text = TextMobject(text_str)
            text.bg = SurroundingRectangle(text, color=color, fill_color=BLACK, fill_opacity=.64, stroke_width=2)
            text_group = VGroup(text.bg, text).scale(.6)
            text_group.move_to(self.arcs[i])

            per = TextMobject(('%.2f' % per + '\%'), color = BLUE).scale(self.legend_scale)
            per.next_to(self.legends[i], LEFT * 0.8)
            per_group.add(per)

            self.play(FadeIn(text_group))
            self.play(ReplacementTransform(text_group, self.legends[i]))
            self.play(Write(per))
            self.wait(0.5)
            i += 1

        self.play(ApplyMethod(self.arcs.shift, DOWN*0.75), ApplyMethod(self.legends.shift, DOWN*0.75),\
                ApplyMethod(per_group.shift, DOWN*0.75), ApplyMethod(self.title.shift, DOWN*0.75))

        self.wait(2)
        self.all = VGroup(self.title, self.arcs, self.legends, per_group)
        return self.all


