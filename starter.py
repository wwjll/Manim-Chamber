
import os
f = open('run_manim.bat', 'w')

py_file_name = 'from_wjl/tutorial/6a_plots_2D.py'
classname = '6a_plots_2D'
# p:autoplay after creation  l|m for the quality of the creation 
pl = ' ' + '-pl'
pm = ' ' + '-pm'
run_script = 'python -m manim' + ' ' + py_file_name + ' ' + classname  + pl  
f.write(run_script)
f.close()

os.system('run_manim.bat')