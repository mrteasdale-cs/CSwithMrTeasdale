import pygame as pg
import math
import colorsys

def run():
    pg.init()

    white = (255,255,255)
    black = (0,0,0)
    hue = 0

    WIDTH = 1920
    HEIGHT = 1080

    x_start, y_start = 0, 0

    x_sep = 10
    y_sep = 20

    rows = HEIGHT // y_sep
    columns = WIDTH // x_sep
    screen_size = rows * columns

    x_offset = columns / 2
    y_offset = rows / 2

    A, B = 0, 0

    theta_spacing = 10
    phi_spacing = 2

    chars = ".,-~:;=!*#$@"

    surface = pg.display.set_mode((WIDTH,HEIGHT))

    #Set font
    font = pg.font.SysFont("comicsansms", 17)
    #Set caption

    def hsv_to_rgb(h, s, v):
        return tuple(round(i*255) for i in colorsys.hsv_to_rgb(h, s, v))

    def text_display(letter, x_start, y_start):
        text = font.render(str(letter), True, hsv_to_rgb(hue, 1, 1))
        surface.blit(text, (x_start, y_start))

    run = True
    while run:
        surface.fill((black))

        z = [0] * screen_size
        b = [''] * screen_size

        for j in range(0, 628, theta_spacing):
            for i in range(0, 628, phi_spacing):
                c = math.sin(i)
                d = math.cos(j)
                e = math.sin(A)
                f = math.sin(j)
                g = math.cos(A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = math.cos(i)
                m = math.cos(B)
                n = math.sin(B)
                t = c * h * g - f * e
                x = int(x_offset + 30 * D * (l * h * m - t * n))
                y = int(y_offset + 15 * D * (l * h * n + t * m))
                o = int(x + columns * y)
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))

                if (rows > y and y > 0 and x > 0 and columns > x and D > z[o]):
                    z[o] = int(D)
                    b[o] = chars[N if N > 0 else 0]


        for k in range (len(b)):
            A += 0.00004
            B += 0.00002
            if k == 0 or k % columns:
                text_display(b[k], x_start, y_start)
                x_start += x_sep
            else:
                y_start += y_sep
                x_start = 0
                text_display(b[k], x_start, y_start)
                x_start += x_sep

        if y_start == rows * y_sep - y_sep:
            y_start = 0

        pg.display.update()
        hue += 0.005
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False

if __name__ == '__main__':
    run()