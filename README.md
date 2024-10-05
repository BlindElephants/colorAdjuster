# colorAdjuster

Simple color palette adjuster to change multiple provided colors in the same way, using both RGB and HSV adjustments. 
Note that RGB adjustments always happen prior to any HSV adjustments.

Values are printed to stdout, allowing for piping to other programs or files as wished.

Run ```main.py``` with the following arguments:

- (required) list of RGB or Hex Colors, separated by colon (":"):
  - RGB: ```0,0,0:255,0,0:255,255,255```
  - Hex: ```#000000:#FF0000:#FFFFFF```
- Optional adjustment arguments:
  - ```-r <int>```: can be a positive or negative value to adjust red channel. Calculated values will wrap around 0-255, such that any negative number will wrap around to 255, and any value over 255 will wrap around to 0.
  - ```-g <int>```: same, for green channel
  - ```-b <int>```: same, for blue channel
  - ```--hue <float>```: value to adjust the hue wheel by. Hue is considered in the range of 0-360, and wraps around.
  - ```--sat <float>```: value to adjust the saturation by. Saturation is in the range 0-1, and does **NOT** wrap.
  - ```--val <float>```: value to adjust the value by. Value is in the range 0-1, and does **NOT** wrap.
  - ```--output_type <str>```: can be either ```hex``` or ```rgb```. By default, output value is in the same format as the input values. Use this if you want differently.