import math
import numpy as np


def generate_colorset():
    colors = np.full((20000, 3), (0, 0, 0), dtype=np.uint8)
    for i in range(20000):
        r = int((math.cos(0.1 * i + 3) * 0.5 + 0.5) * 255)
        g = 0  # Set green component to 0 (black)
        b = int((math.cos(0.1 * i + 1) * 0.5 + 0.5) * 255)
        colors[i] = (r, g, b)
    return colors
