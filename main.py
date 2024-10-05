import argparse
import src.ColorSpaceConversions as SpaceConversions
import re

from src.ColorEncodingConversions import hex_to_rgb, rgb_to_hex


def is_value_rgb_or_hex(color_value):
    if "," in color_value:
        return "rgb"
    elif re.search("[a-fA-F]", color_value):
        return 'hex'
    elif len(color_value) in [6, 7]:
        return 'hex'
    elif '#' in color_value:
        return 'hex'

def get_rgb_values(color_values_input):
    color_values_split = color_values_input.split(":")
    color_values_split = [cv.strip() for cv in color_values_split]
    color_values_split = [cv.replace("#", "") for cv in color_values_split]

    color_types = []
    for cv in color_values_split:
        color_types.append(is_value_rgb_or_hex(cv))
    unique_color_types = set(color_types)

    if len(unique_color_types) > 1:
        raise TypeError("Must only supply a single color type, either RGB or HEX")

    color_type = list(unique_color_types)[0]

    if color_type == "hex":
        color_values_split = [hex_to_rgb(cv) for cv in color_values_split]
    else:
        color_values_split = [cv.split(',') for cv in color_values_split]

        for cv_idx in range(len(color_values_split)):
            for chan_idx in range(len(color_values_split[cv_idx])):
                color_values_split[cv_idx][chan_idx] = int(color_values_split[cv_idx][chan_idx].strip())

    return color_type, color_values_split




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This program accepts RGB or HEX color values and will perform an operation on"
                                                 "those values to adjust them. Values may be added or subtracted to the R, G, B, "
                                                 "Hue, Saturation, or Value parameters of each color by passing a value with "
                                                 "the related argument. RGB values are in the range of 0-255 and will wrap. "
                                                 "Hue values are in the range 0-360, while Saturation and Value values are "
                                                 "in the range 0-1. You can pass multiple such arguments, but note that RGB adjustments will"
                                                 "always happen prior to HSV adjustments. By default, the output values will be in the same "
                                                 "encoding as the input.")
    parser.add_argument("color_values", type=str, help="If using RGB, each "
                                                       "value should have three parts, separate by commas. If using HEX "
                                                       "values, each should contain 6 characters 0-F. Providing more "
                                                       "than one such color, separated by semicolon (;), will be "
                                                       "interpreted as a list, with the directed operation being performed "
                                                       "on all values.")
    parser.add_argument("--output_type", type=str, default=None)

    parser.add_argument("-r", type=int)
    parser.add_argument("-g", type=int)
    parser.add_argument("-b", type=int)

    parser.add_argument("--hue", type=float)
    parser.add_argument("--sat", type=float)
    parser.add_argument("--val", type=float)

    args = parser.parse_args()

    color_type, rgb_values = get_rgb_values(args.color_values)


    for idx in range(len(rgb_values)):
        if args.r:
            rgb_values[idx][0] = (rgb_values[idx][0] + args.r) % 255
        if args.g:
            rgb_values[idx][1] = (rgb_values[idx][1] + args.g) % 255
        if args.b:
            rgb_values[idx][2] = (rgb_values[idx][2] + args.b) % 255

    if args.hue or args.sat or args.val:
        hsv_values = [SpaceConversions.rgb_to_hsv(cv) for cv in rgb_values]

        for idx in range(len(hsv_values)):
            if args.hue:
                hsv_values[idx][0] = (hsv_values[idx][0] + args.hue) % 360.0
            if args.sat:
                hsv_values[idx][1] = min(max((hsv_values[idx][1] + args.sat), 0.0), 1.0)
            if args.val:
                hsv_values[idx][2] = min(max((hsv_values[idx][2] + args.val), 0.0), 1.0)

        rgb_values = [SpaceConversions.hsv_to_rgb(cv) for cv in hsv_values]

    if color_type == 'hex' and args.output_type != 'rgb':
        hex_values = [rgb_to_hex(cv) for cv in rgb_values]
        hex_values = [f'#{cv}' for cv in hex_values]
        hex_values = ':'.join(hex_values)
        print(hex_values)
    else:  # color_type == 'rgb'
        out_rgb = []
        for cv in rgb_values:
            cv_str = [str(c) for c in cv]
            out_rgb.append(f'{",".join(cv_str)}')
        out_rgb = ':'.join(out_rgb)

        print(out_rgb)
