import math
import colorsys
import time

hue = 0

WIDTH = 80
HEIGHT = 24

x_start, y_start = 0, 0

x_separator = 2
y_separator = 4

rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0

theta_spacing = 10
phi_spacing = 1

chars = ".,-~:;=!*#$@"

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def text_display(letter):
    print(letter, end="", flush=True)

run = True
while run:
    print("\033[2J", end="")  # Clear the terminal
    print("\033[H", end="")   # Move cursor to home position

    z = [0] * screen_size
    b = [' '] * screen_size

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
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if rows > y > 0 and columns > x > 0 and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_separator - y_separator:
        y_start = 0

    for i in range(len(b)):
        A += 0.00004
        B += 0.00002
        if i == 0 or i % columns:
            text_display(b[i])
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i])
            x_start += x_separator

    hue += 0.005
    time.sleep(0.03)  # Adjust the delay to control the speed of the animation
