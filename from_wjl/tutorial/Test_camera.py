
from manimlib.imports import *

class Test_camera(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        yellow_cube = Cube(fill_color=YELLOW, stroke_width=2, stroke_color=WHITE)
        blue_sphere = Sphere(fill_color=BLUE, checkerboard_colors=None).shift(OUT * 2)
        green_cube = Cube(fill_color=GREEN).scale([2, 0.5, 0.5]).shift(RIGHT * 3.25)

        phi_0, theta_0 = 0, 0
        phi, theta = 60 * DEGREES, -120 * DEGREES

        self.set_camera_orientation(phi=phi_0, theta=theta_0)
        self.add(axes, yellow_cube, blue_sphere, green_cube)
        self.wait()
        dt = 1/15
        delta_phi, delta_theta = (phi - phi_0) / 30, (theta - theta_0) / 60
        for i in range(30):
            phi_0 += delta_phi
            self.set_camera_orientation(phi=phi_0, theta=theta_0)
            self.wait(dt)
        for i in range(60):
            theta_0 += delta_theta
            self.set_camera_orientation(phi=phi_0, theta=theta_0)
            self.wait(dt)
        self.wait(2)



    
