# Vectoriser
This is my own implementation of Potrace bitmap tracing algorithm.

## Potrace
Potrace algorithm takes a binary imgae (image with only #fff and #000) as input and outputs a vector image.

[Algorithm Paper](http://potrace.sourceforge.net/potrace.pdf)

## Required Packages
- Svgwrite
- Matplotlib
- Shapely ([Windows Installation](https://pypi.org/project/Shapely/#files))

## How to use Vectoriser
 - Get greyscale array using ``` i.RgbArrayToGreyscale(rgb) ```
 - Get binary array using ``` i.getBinary(greyscale, threshold, invert=True/False) ```
 (Turn on invert if you are using the inclued edge detection function, or you are feeding image with a white fg and black bg)
 - Get closed paths using ``` p.decompose(binary) ```
 - (Optional) Apply noise reduction using ```p.reduceByArea(paths, size_threshold)```
 (You can use ``` hp.getAreaThreshold(paths, ratio) ``` to compute the size in terms of path_size/image_size ratio)
 - Get striaght lines in a closed path using ```p.getStraightLines(path)```
 - Construct the SVG path data value using  ``` p.svgConstructor(straight_line) ```
 - Use svgwrite.<span></span>py to output the vector image

## Diagonal Bug
Because of a design flaw in my implementation, the program cannot exit a loop that has a diagonal open for the tracing to enter. The workaround is ```path.diagonalCompensate()```, but it only deals with half of the possible scenarios. Therefore, you will still encounter this bug.

## Troubleshooting
    IndexError: list index out of range at w = len(array[0])
The program was probably trying to trace an blank image. Use ```debug.saveBitmap()``` to preview the binary image.

## Other Known Issues
- Produces a 1x1 triangle path when it shuold produce a 1x1 rectangle path