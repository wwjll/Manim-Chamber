'''
'''
from manimlib.imports import *
class Simple_Vector(Scene):
    def construct(self):
        plane = NumberPlane ( color = RED )
        plane.add( plane.get_axis_labels( ) )
        self.add( plane )
        points = [ x * RIGHT + y * UP
                    for x in np.arange( -5 , 5 , 1 )
                    for y in np.arange( -3 , 3,  1)
                ]
        vec_field = []
        for point in points:
            field = 0.5 * RIGHT + 0.5 * UP
            result = Vector( field, color=YELLOW ).shift( point )
            vec_field.append( result )

        draw_field = VGroup( *vec_field )
        self.play( ShowCreation( draw_field ) , run_time = 4)
        self.wait( 2 )


class Numberplane ( Axes ) :
    CONFIG = {
        "axis_config": {
            "stroke_color":WHITE,
            "stroke_width":2,
            "include_ticks":False,
            "include_tip":False,
            "line_to_number_buff":SMALL_BUFF,
            "label_direction":DR,
            "number_scale_val":0.5,
        },
        "y_axis_config": {
            "label_direction":DR,
        },
        "backgroud_line_style": {
            "stroke_color":BLUE_D,
            "stroke_width":2,
            "stroke_opacity":1,
        },
        # Defaults to a faded version of line_config
        "faded_line_style": None,
        "x_line_frequency": 1,
        "y_line_frequency": 1,
        "faded_line_ratio": 1,
        "make smooth after applying functions" : True,   
    }

