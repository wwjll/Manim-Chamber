from manimlib.imports import *
import sys
sys.path.append(r'E:\math\manim\from_wjl\tutorial\PieChart')
from PieChart import PieChart
class ShowPieChart(PieChart):
    def construct(self):
        color_list = [
            '#B92B35','#B92B35','#B92B35','#B92B35','#B92B35','#B92B35','#B92B35','#B92B35',\
            '#B92B35','#B92B35','#B92B35','#B92B35','#B92B35','#B92B35','#B92B35','#B92B35',
        ]
        data_info = (15.36, color_list[0], 'GuangDong'), (8.35, color_list[1], 'GuangDong'), (7.43, color_list[2], 'GuangDong'),\
                    (5.69, color_list[3], 'GuangDong'),(5.55, color_list[4], 'GuangDong'),(4.53, color_list[5], 'GuangDong'),\
                    (4.39, color_list[6], 'GuangDong'),(4.15, color_list[7], 'GuangDong'),(3.66, color_list[8], 'GuangDong'),\
                    (3.50, color_list[9], 'GuangDong'),(37.40, color_list[-2], 'GuangDong')

        # title = 'B站各省用户占比统计'
        title = 'Bilibili'
        self.create_anim(title, *data_info)

        self.wait()
        