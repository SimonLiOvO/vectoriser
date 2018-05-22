from PIL import Image
import math


def getPixelArray(file):
    """Converts an image to a list containing pixel information"""
    array = []
    with Image.open(file) as img:
        for y in range(img.height):
            row = []
            for x in range(img.width):
                pixel = img.getpixel((x, y))
                row.append(pixel)
            array.append(row)
    return array


def RGBtoGreyScale(rgb):
    """Converts a RGB tuple to greyscale value"""
    greyscale = 0.2989*rgb[0]+0.5870*rgb[1]+0.1140*rgb[2]
    greyscale = int(round(greyscale))
    return greyscale


def greyscaleToRGB(greyscale):
    """Converts a greyscale int to a RGB tuple"""
    rgb = (greyscale, greyscale, greyscale)
    return rgb


def getDimensions(array):
    """Returns the width and height of the bitmap iamge in a tuple"""
    x = len(array[0])
    y = len(array)
    return (x, y)


def getGreyscaleArray(array, mode="greyscale"):
    """Converts a RGB or RGBA array to greyscale\n
    RGB mode returns pixels as RGB tuples\n
    greyscale mode returns pixels as int"""
    dimensions = getDimensions(array)
    grey_array = []
    for h in range(dimensions[1]):
        row = []
        for w in range(dimensions[0]):
            greyscale = RGBtoGreyScale(array[h][w])
            if mode == "RGB":
                grey_rgb = greyscaleToRGB(greyscale)
                row.append(grey_rgb)
            elif mode == "greyscale":
                row.append(greyscale)
            else:
                raise ValueError
        grey_array.append(row)
    return grey_array
