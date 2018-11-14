import edge_detection as ed
import path as p
import helper as hp
import image as i
import debug

if __name__ == '__main__':
    rgb = i.getRgbArray(r"bitmap/wsg.png")
    greyscale = i.RgbArrayToGreyscale(rgb)
    # Uncomment the below line to enable edge detection
    # greyscale = ed.getEdges(greyscale)

    # The binary image needs to have black foreground and white bground
    # Use invert=True when needed
    binary = i.getBinary(greyscale, 75)

    # Uncomment below code to output an binary image
    # debug.saveBitmap(binary, "bitmap/binary_preview.png", binary=True)

    paths = p.decompose(binary)

    # Noise Reduction by removing paths with area smaller than the specified threshold
    paths = p.reduceByArea(paths, hp.getAreaThreshold(paths, 0))

    output = []
    for path in paths:
        straight_line = p.getStraightLines(path)
        output.append(p.svgConstructor(straight_line))

    with open('output.txt', 'w') as f:
        f.write(str(output))
    # Use svgwrite.py to produce the .svg vector file
