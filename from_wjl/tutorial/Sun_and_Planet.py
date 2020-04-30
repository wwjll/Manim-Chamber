'''
    1. 3D场景类ThreeDScene
    2. 摄像机位置set_camera_orientation,参数俯仰角,方位角,距离,gamma
    3. 向量类Vector
'''
from manimlib.imports import *
class Sun_and_Planet(ThreeDScene):
    def construct(self):
        r = 7
        sun = Sphere(radius=1.6)
        planet = Sphere(radius=0.4)
        orbit = Circle(radius=r)
        planet.shift(UP * r)
        system = VGroup(orbit, sun, planet)
        system.shift(DOWN * 2. + LEFT + 1.2)
        # 指向圆心的矢量 -（7 - 1.6 - 0.4）
        F_vector = Vector(np.array([0,  -5, 0]), color=YELLOW)
        F_vector.next_to(planet, DOWN * 0.6)
        F_formula = TextMobject('$\\vec{F}=G m_1 m_2 \\frac{(\\vec{r_1} -\\vec{r_2})}{r^3}$', color=RED)
        F_formula.rotate_about_origin(PI/2)
        F_formula.next_to(F_vector, LEFT * 0.4)
        self.set_camera_orientation(phi=65 * PI/180, theta=PI/3)

        self.play(ShowCreation(orbit))
        self.play(FadeIn(sun), FadeIn(planet))
        self.wait(1)
        self.play(ShowCreation(F_vector))
        self.play(Write(F_formula))
        self.wait(1)
