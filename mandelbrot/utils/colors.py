import math
import numpy as np


def generate_colorset():
    colors = np.full((20000, 3), (0, 0, 0), dtype=np.uint8)
    for i in range(20000):
        r = int((0.5 * math.sin(0.005 * i)) * 255)
        g = int((0.5 * math.sin(0.01 * i)) * 255)
        b = int((0.5 * math.sin(0.03 * i) + 0.1) * 255)
        colors[i] = (r, g, b)
    return colors
