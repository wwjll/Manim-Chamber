from manimlib.imports import *

class Curve_3D_test(SpecialThreeDScene):
    # CONFIG = {
    #     "default_angled_camera_position" : {
    #         "phi" : 65 * DEGREES,
    #         "theta" : -60 * DEGREES,
    #         "distance" : 50,
    #         "gamma" : 0
    #     },
    # }

    def contruct(self):
        # self.set_camera_to_default_position()
        # r = 2
        # w = 4
        # circle = ParametricFunction(lambda t: r * complex_to_R3(np.exp(1j * w * t)),
        #                             t_min=0, t_max=TAU * 1.5, color=RED, stroke_width=8)
        # spiral_line = ParametricFunction(lambda t: r * complex_to_R3(np.exp(1j * w * t) + OUT * t),
        #                             t_min=0, t_max=TAU * 1.5, color=PINK, stroke_width=8)
        # circle.shift(IN * 2.5)
        # spiral_line.shift(IN * 2.5)

        # self.add(circle, spiral_line)
        # self.wait()
        # self.play(TransformFromCopy(circle, spiral_line, rate_func=there_and_back), run_time=4)
        # self.wait(2)


        self.set_camera_to_default_position()
        axes = self.get_axes()
        surface = ParametricSurface(lambda u,v: np.array([u, v, np.sin(u**2 + v**2)]),
                                        u_min = -4 , u_max=4, v_min=-4, v_max=4, resolution=(120,120))
        self.add(axes, surface)
        self.wait(5)
