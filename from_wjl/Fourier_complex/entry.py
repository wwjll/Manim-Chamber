from PIL import Image
import pylab
import numpy as np
from scipy.spatial import Delaunay
import heapq

path = r'D:\math\manim\from_wjl\Fourier_complex\\duck.png'
img = Image.open(path)
# matplotlib.pyplot.contour要求输入像素为单个字节，所以我们先转换成灰度像素
img = img.convert('L')
# 提取轮廓
fig, ax = pylab.subplots()
contours = ax.contour(img, origin='image', levels=[100])
# pylab.show()

raw_data = []
segs = np.array(contours.allsegs) / max(img.width, img.height)
reverse_idx = {}
for seg in segs:
    for poly in seg:
        # down sample 1: make points more discrete
        poly = (np.array(poly) * 1000).astype(int) / 1000
        poly = [tuple(p) for p in poly]

        # index points and deduplicate points shared cross polygons
        poly2 = []
        for p in poly:
            if p not in reverse_idx:
                reverse_idx[p] = len(reverse_idx)
                raw_data.append(np.array(p))
print(f'{len(raw_data)} points in raw data')

indices = np.random.choice(len(raw_data), int(len(raw_data) * 0.3), replace=False)
samples = np.array(raw_data)[indices]
print(f'randomly sampled {len(samples)} points')