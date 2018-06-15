from PIL import Image
import image as i
import helper as hp


def getColorMode(array):
    """Return the color mode of the image using pixel data"""
    if len(array[0][0]) == 3:
        return "RGB"
    if len(array[0][0]) == 4:
        return "RGBA"


def binaryToGreyscale(array):
    dimensiosns = hp.getDimensions(array)
    binary = []
    for h in range(dimensiosns[0]):
        row = []
        for w in range(dimensiosns[1]):
            if array[h][w] == 1:
                row.append(255)
            else:
                row.append(0)
        binary.append(row)
    return binary


def GreyscaleArrayToRgb(array):
    """Converts a greyscale array to RGB array"""
    dimensions = hp.getDimensions(array)
    for h in range(dimensions[0]):
        for w in range(dimensions[1]):
            array[h][w] = hp.greyscaleToRgb(array[h][w])
    return array


def saveBitmap(array, filename, binary=False):
    """Saves a new bitmap image file. Debug use only."""
    if binary:
        array = binaryToGreyscale(array)
    dimensions = hp.getDimensions(array)
    array = GreyscaleArrayToRgb(array)
    img = Image.new(getColorMode(array), (dimensions[1], dimensions[0]))
    for h in range(dimensions[0]):
        for w in range(dimensions[1]):
            img.putpixel((w, h), array[h][w])
    img.save(filename)
