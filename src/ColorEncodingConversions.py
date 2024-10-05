from typing import Union, Tuple, List

def hex_to_rgb(hex_value):
    if len(hex_value) != 6:
        return None
    rgb = [int(hex_value[0:2], 16), int(hex_value[2:4], 16), int(hex_value[4:6], 16)]
    return rgb

def rgb_to_hex(rgb):
    r_hex = hex(rgb[0])[2:4]
    g_hex = hex(rgb[1])[2:4]
    b_hex = hex(rgb[2])[2:4]

    if len(r_hex) == 1:
        r_hex = '0'+r_hex
    if len(g_hex) == 1:
        g_hex = '0'+g_hex
    if len(b_hex) == 1:
        b_hex = '0'+b_hex

    return (r_hex+g_hex+b_hex).upper()