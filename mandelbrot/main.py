import pygame as pg
import numpy as np
import numba
from utils.colors import generate_colorset
from fractal import Fractal


size = width, height = 3840, 2160


def main():
    fractal_generator = Fractal(height=height, width=width)
    pg.init()
    window = pg.display.set_mode(size, pg.SCALED)
    clock = pg.time.Clock()
    x1, x2, y1, y2 = -2, 1, -1, 1
    fractal = np.full((width, height, 3), (0, 0, 0), dtype=np.uint8)
    colors = generate_colorset()
    in_dragging = False
    max_iter = 3
    while True:
        clock.tick()
        for event in pg.event.get():
            if (
                event.type == pg.QUIT
                or event.type == pg.KEYDOWN
                and event.key == pg.K_ESCAPE
            ):
                quit()
            if event.type == pg.MOUSEBUTTONDOWN and not in_dragging:
                if pg.mouse.get_pressed()[0]:
                    mx, my = pg.mouse.get_pos()
                    in_dragging = True
            if in_dragging and event.type != pg.MOUSEBUTTONUP:
                mx2, my2 = pg.mouse.get_pos()
                dx, dy = fractal_generator.pixel_to_fractal(
                    x1, x2, y1, y2, mx2 - mx, my2 - my
                )
                x1 -= dx
                x2 -= dx
                y1 -= dy
                y2 -= dy
                mx, my = mx2, my2
            if in_dragging and event.type == pg.MOUSEBUTTONUP:
                in_dragging = False
            if event.type == pg.MOUSEWHEEL:
                dx, dy = fractal_generator.pixel_to_fractal(
                    x1, x2, y1, y2, width / 5, height / 5
                )
                if event.y == -1:
                    x1 -= dx
                    x2 += dx
                    y1 -= dy
                    y2 += dy
                elif event.y == 1:
                    x1 += dx
                    x2 -= dx
                    y1 += dy
                    y2 -= dy
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                max_iter /= 2
            if event.type == pg.KEYUP and event.key == pg.K_UP:
                max_iter *= 2
            if pg.key.get_pressed()[pg.K_s]:
                pg.image.save(window, "screenshot.jpg")
        fractal = fractal_generator.draw_mandelbrot_fractal(
            fractal, x1, x2, y1, y2, colors, max_iter
        )

        pg.surfarray.blit_array(window, fractal)
        pg.display.flip()
        pg.display.set_caption(f"FPS={clock.get_fps():.1f}")


if __name__ == "__main__":
    main()
