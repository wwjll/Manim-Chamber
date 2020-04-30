from manimlib.imports import *

class ThreedSurface(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -2,
        "u_max": 2,
        "v_min": -2,
        "v_max": 2,
        "checkerboard_colors": [BLUE_D]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)

    def func(self, x, y):
        return np.array([x,y,x**2 - y**2])


class Test(ThreeDScene):

    def construct(self):
        self.set_camera_orientation(0.6, -0.7853981, 86.6)

        surface = ThreedSurface()
        self.play(ShowCreation(surface))

        d = Dot(np.array([0,0,0]), color = YELLOW)
        self.play(ShowCreation(d))


        self.wait()
        self.move_camera(0.8*np.pi/2, -0.45*np.pi)
        self.begin_ambient_camera_rotation()
        self.wait(9)