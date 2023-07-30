import numba
from numpy import ndarray


@numba.jit(fastmath=True, parallel=True)
def _draw_mandelbrot_fractal(
    width,
    height,
    fractal: ndarray,
    x1: int,
    x2: int,
    y1: int,
    y2: int,
    colors: ndarray,
    max_iter: int,
):
    x_step = (x2 - x1) / width
    y_step = (y2 - y1) / height

    for x in numba.prange(width):
        for y in numba.prange(height):
            c = complex(x1 + x * x_step, y1 + y * y_step)
            z = 0
            for i in numba.prange(max_iter):
                z = z**2 + c
                if z.imag**2 + z.real**2 > 4:
                    break
            fractal[x][y] = colors[i]
    return fractal


class Fractal:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def pixel_to_fractal(self, x1: int, x2: int, y1: int, y2: int, px: int, py: int):
        return px * (x2 - x1) / self.width, py * (y2 - y1) / self.height

    def draw_mandelbrot_fractal(
        self,
        fractal: ndarray,
        x1: int,
        x2: int,
        y1: int,
        y2: int,
        colors: ndarray,
        max_iter: int,
    ):
        return _draw_mandelbrot_fractal(
            self.width, self.height, fractal, x1, x2, y1, y2, colors, max_iter
        )
