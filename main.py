import edge_detection as ed
import path as p
import helper as hp
import image as i
import debug

if __name__ == '__main__':
    rgb = i.getRgbArray(r"bitmap/blank.png")
    greyscale = i.RgbArrayToGreyscale(rgb)
    # Uncomment the below line to enable edge detection
    # greyscale = ed.getEdges(greyscale)

    # The binary image needs to have black foreground and white bground
    # Use invert=True when needed
    binary = i.getBinary(greyscale, 255, invert=True)

    # Uncomment below code to output an binary image
    # debug.saveBitmap(binary, "bitmap/binary_preview.png", binary=True)

    paths = p.decompose(binary)

    # Noise Reduction by removing paths with area smaller than the specified threshold
    paths = p.reduceByArea(paths, hp.getAreaThreshold(paths, 0.02))

    print("SVG path data:")
    output = []
    for path in paths:
        straight_line = p.getStraightLines(path)
        output.append(p.svgConstructor(straight_line))
    print(output)
    # Use svgwrite.py to produce the .svg vector file