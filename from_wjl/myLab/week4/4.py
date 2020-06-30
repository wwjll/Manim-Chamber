from manimlib.imports import *

# 绘制题目图形
def plot_commom_part():
    # 扇形的边
    arc = Arc(start_angle=math.radians(60), angle=math.radians(-60), radius=2)
    start_point = arc.get_start()
    end_point = arc.get_end()
    sector_side_oa = Line(ORIGIN, start_point)
    sector_side_ob = Line(ORIGIN, end_point)
    side_oc = sector_side_oa.copy().rotate(-10 * DEGREES, axis=OUT, about_point=ORIGIN)
    end_point_oc = side_oc.get_end()
    height_cd = Line(np.array([end_point_oc[0], 0, 0]), np.array([end_point_oc[0], end_point_oc[1], 0]))
    sector_side_group = VGroup(arc, sector_side_oa, sector_side_ob, side_oc, height_cd)
    # OABCD
    sector_labels_group = VGroup(
        TexMobject("O").scale(0.5).shift(LEFT * 0.1 + DOWN * 0.1),
        TexMobject("A").scale(0.5).shift(arc.get_start() + UP * 0.14),
        TexMobject("B").scale(0.5).shift(arc.get_end() + RIGHT * 0.1 + 0.1 * DOWN),
        TexMobject("C").shift(side_oc.get_end() + RIGHT * 0.12 + UP * 0.12).scale(0.5),
        TexMobject("D").shift(1.28 * RIGHT + DOWN * 0.12).scale(0.5)
    )
    return sector_side_group,sector_labels_group

class Scene1(Scene):
    def construct(self):
        question1 = TextMobject("圆心角为60$^{\\circ}$的扇形$OAB$, $C$是$\\stackrel\\frown{AB}$上一点")
        question2 = TextMobject("$CD\\bot OB$于$D$, 求$S\\triangle OCD\\max$?")
        question1.to_corner(UL)
        question2.next_to(question1, DOWN)
        question2.align_to(question1, LEFT)
        text_group1 = VGroup(question1, question2)
        self.play(Write(text_group1))
        self.wait()
        sector_side_group,sector_labels_group = plot_commom_part()
        self.play(ShowCreation(sector_side_group))
        self.wait()
        self.play(Write(sector_labels_group))
        self.wait()
        self.play(FadeOut(text_group1))
        self.wait()
        self.play(FadeOut(sector_labels_group))
        self.wait()
        self.play(FadeOut(sector_side_group))
        self.wait()


class Scene1_2(Scene):
    def construct(self):
        sector_side_group,sector_labels_group = plot_commom_part()
        sector_side_group.move_to(5 * LEFT + 2 * UP)
        sector_labels_group.move_to(5 * LEFT + 2 * UP)
        self.add(sector_side_group,sector_labels_group)
        
        side_ob = sector_side_group[2]
        center_point = side_ob.get_center()

        side_oc = sector_side_group[3]
        side_cd = sector_side_group[4]
        side_od = Line(side_oc.get_start(), side_cd.get_start())
        tri_ocd_group = VGroup(side_oc.copy(), side_od.copy(), side_cd.copy())
        self.play(
            Rotating(
                tri_ocd_group,
                radians=-50 * DEGREES,
                run_time=2,
                axis=OUT,
                about_point=side_oc.get_start()
            )
        )
        self.wait()
        label_e  = TextMobject('E')
        label_e.scale(0.5)
        position_e = tri_ocd_group[1].get_end()
        label_e.next_to(position_e, DOWN)
        label_e.shift(0.1 * UP)
        self.play(ShowCreation(label_e))
        self.wait()
        circle_center = Dot(
            center_point
        )
        circle_center_label = TextMobject("F")
        circle_center_label.scale(0.5)
        circle_center_label.next_to(position_e, UP, 0.6)
        circle_center_group = VGroup(circle_center_label, circle_center)
        self.play(FadeIn(circle_center_group))
        self.wait()
        # 
        circle = Circle(
            radius = 1,
            color = WHITE
        )
        circle.move_to(center_point)
        self.play(Write(circle))
        self.wait()
        # 
        self.play(FadeOut(tri_ocd_group))
        self.remove(tri_ocd_group)
        self.wait()
        # 
        moving_e_point = Dot(side_ob.get_start())
        moving_e_point.rotate(10 * DEGREES, about_point=center_point)
        label_e.next_to(moving_e_point, DL)
        line_fe = Line(center_point, moving_e_point.get_center())
        line_oe = Line(side_ob.get_start(), moving_e_point.get_center())
        line_be = Line(side_ob.get_end(), moving_e_point.get_center())
        label_e.add_updater(lambda l: l.next_to(moving_e_point, DOWN))
        line_fe.add_updater(lambda l: l.put_start_and_end_on(center_point, moving_e_point.get_center()))
        line_oe.add_updater(lambda l: l.put_start_and_end_on(side_ob.get_start(), moving_e_point.get_center()))
        line_be.add_updater(lambda l: l.put_start_and_end_on(side_ob.get_end(), moving_e_point.get_center()))
        moving_group = VGroup(line_fe, line_oe, line_be)
        moving_group.set_color(BLUE)
        self.play(ShowCreation(moving_group))
        self.wait()
        # 
        self.play(
            Rotating(
                moving_e_point,
                radians=80 * DEGREES,
                run_time=2,
                axis=OUT,
                about_point=center_point
            )
        )
        self.wait()
         

class Scene1_3(Scene):
    # 讲解文字
    def construct(self):
        text1 = TextMobject("OA = OB","$\\quad \\angle {AOB}$ = 60°")
        text2 = TextMobject("旋转得","$ \\Delta {OBE} $")
        text3 = TextMobject("$\\because \\angle {ODC}  = \\angle {OEB} = 90°$")
        text4 = TextMobject("$\\therefore E $ 在以 $ OB $ 为直径的$ \\odot F $上")
        text5 = TextMobject("连接EF，当EF 等于半径（r）时")
        text6 = TextMobject("$S\\triangle OCD\\max = r^2$")
        text1.shift(3 * UP + RIGHT)
        text2.next_to(text1, DOWN)
        text3.next_to(text2, DOWN)
        text4.next_to(text3, DOWN)
        text5.next_to(text4, DOWN)
        text6.next_to(text5, DOWN)
        # text_group = VGroup(text1, text2, text3, text4, text5)
        self.play(Write(text1))
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(Write(text3))
        self.wait()
        self.play(Write(text4))
        self.wait()
        self.play(Write(text5))
        self.wait()
        self.play(Write(text6))
        self.wait()



class Scene2(Scene):
    def construct(self):
        position_o = ORIGIN
        total_scale = 0.5
        min = 0.25
        max = 1.5
        position_a_min = np.array([0, np.sqrt(3) * min , 0])
        position_a_max = np.array([0, np.sqrt(3) * max, 0])
        position_b_min = np.array([-min, 0, 0])
        position_b_max = np.array([-max, 0, 0])
        position_c_min = np.array([min, 0, 0])
        position_c_max = np.array([max, 0, 0])
        # 求出两圆交点 P 并使 P 随动
        def intersect(dot_p):
            length_ab = 2 * w.get_value()
            length_pb = 4 * total_scale
            length_pa = 3 * total_scale
            radian_pba = np.arccos((pow(length_pb, 2) + pow(length_ab, 2) - pow(length_pa, 2))/(2*length_pb*length_ab))
            # angle_pba = np.arccos((25 + pow(length_ab, 2))/24)
            radian_abo = np.pi / 3
            p_x = -w.get_value() - length_pb * np.cos(np.pi - radian_pba - radian_abo)
            p_y = length_pb * np.sin(np.pi - radian_pba - radian_abo)
            dot_p.move_to(np.array([p_x, p_y, 0]))
        #  
        def paralle(short_pc):
            # 尝试求 w 值使得 P, P', C 三点共线,涉及到浮点数运算，没有求出准确值
            short_pc.put_start_and_end_on(dot_p_clone.get_center(), dot_c.get_center())
            # vect1 = line_pp.get_end() - line_pp.get_start()
            # vect2 = short_pc.get_end() - short_pc.get_start()
            # print(vect2[0] / vect1[0], vect2[1] / vect1[1])
            # if(vect1[0] == 0 or vect1[1] == 0):
            #     return
            #     if(vect2[0] / vect1[0] == vect2[1] / vect1[1]):
            #         print("w",w.get_value())
            #         return
        w = ValueTracker(min)
        ab = Line(position_a_min, position_b_min)
        bc = Line(position_b_min, position_c_min)
        ac = Line(position_a_min, position_c_min)
        circle_a = Circle(radius = 3 * total_scale)
        circle_b  = Circle(radius = 4 * total_scale)
        circle_a.move_to(ab.get_start())
        circle_a.move_to(ab.get_end())
        ab.add_updater(lambda l: l.put_start_and_end_on(np.array([0, np.sqrt(3) * w.get_value(), 0]), np.array([-w.get_value(), 0, 0])))
        bc.add_updater(lambda l: l.put_start_and_end_on(np.array([-w.get_value(), 0, 0]), np.array([w.get_value(), 0, 0])))
        ac.add_updater(lambda l: l.put_start_and_end_on(np.array([0, np.sqrt(3) * w.get_value(), 0]), np.array([w.get_value(), 0, 0])))
        circle_a.add_updater(lambda ca: ca.move_to(ab.get_start()))
        circle_b.add_updater(lambda cb: cb.move_to(ab.get_end()))
        # 先随意指定了 P 点的位置，因为添加了 updater, 创建后会立即更新位置
        dot_p = Dot(ORIGIN)
        dot_p_clone = Dot(ORIGIN).rotate( -60 * DEGREES, about_point=ab.get_end())
        label_p = TextMobject('P')
        label_p.scale(0.5)
        label_p.add_updater(lambda l: l.move_to(dot_p.get_center() + 0.5 * DOWN))
        dot_p.add_updater(intersect)
        dot_p_clone.add_updater(lambda l: l.move_to(dot_p.copy().rotate(-60 * DEGREES, about_point=ab.get_end()).get_center()))
        line_pp = Line(dot_p, dot_p_clone)
        line_pp.add_updater(lambda l: l.put_start_and_end_on(dot_p.get_center(), dot_p_clone.get_center()))
        # 
        dot_c = Dot(position_c_min)
        dot_c.add_updater(lambda d: d.move_to(ac.get_end()))
        # 旋转后的P和C连线
        line_short_pc = Line(dot_p_clone, dot_c)
        line_short_pc.add_updater(paralle)
        max_group = VGroup(circle_a, circle_b, ab, bc, ac, dot_p, label_p, dot_p_clone, dot_c, line_pp, line_short_pc)
        # 
        self.play(ShowCreation(max_group))
        self.wait(2)
        self.play(w.set_value, max, run_time=4)
        self.wait()
