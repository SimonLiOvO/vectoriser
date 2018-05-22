from PIL import Image
import vectoriser as v


def getColorMode(array):
    """Return the color mode of the image using pixel data"""
    if len(array[0][0]) == 3:
        return "RGB"
    if len(array[0][0]) == 4:
        return "RGBA"


def saveBitmap(array, filename):
    """Saves a new bitmap image file. Debug use only."""
    dimensions = v.getDimensions(array)
    img = Image.new(getColorMode(array), dimensions)
    for w in range(dimensions[0]):
        for h in range(dimensions[1]):
            img.putpixel((w, h), array[h][w])
    img.save(filename)
