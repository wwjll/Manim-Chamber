# '''
#     一开始定义的CONFIG字典实际上确定了构造函数中成员变量的值，这是由于GraphScene和Scene都继承自父类Container，而Container的构造函数会使用CONFIG中的键和值进行构造
#     （详细内容可查看其源代码的manim\manimlib\container中的container.py及manim\utils\config_ops.py中的digest_config方法）。
#     你可以不用深究其含义，简单理解为这个字典对一些场景的属性和我们希望用到的一些参数进行了初始化配置，之后可以使用self.XXX来调用就ok了；
# '''

from manimlib.imports import *
class Circular(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN,
        "function_color" : RED,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(-10, 12, 2)
    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        func_graph2 = self.get_graph(self.func_to_graph2)
        # 在 2pi 的位置获取cos与横轴的高线
        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
        # label 与绘制曲线的位置
        graph_lab = self.get_graph_label(func_graph, label = r"\cos(x)")
        graph_lab2 = self.get_graph_label(func_graph2, label = r"\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject(r"x = 2 \pi")
        # 在 2pi 的位置 cos的输入值
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT+UP)

        self.play(ShowCreation(func_graph), ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab),
                    ShowCreation(graph_lab2), ShowCreation(two_pi))

    def func_to_graph(self, x):
        return np.cos(x)

    def func_to_graph2(self, x):
        return np.sin(x)
