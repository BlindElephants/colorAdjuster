from typing import List
import colorsys


def rgb_to_hsv(rgb):
    r, g, b = rgb
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    return [h * 360.0, s, v]  # Will return HSV values with maximum values of (360.0, 1.0, 1.0)


def hsv_to_rgb(hsv):
    h, s, v = hsv
    h /= 360.0
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return [round(r * 255.0), round(g * 255.0), round(b * 255.0)]  # Will return RGB values in the range 0-255