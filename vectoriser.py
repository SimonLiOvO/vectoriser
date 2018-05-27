from PIL import Image
import math
import numpy


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
    """Returns the width and height of the bitmap iamge in a tuple (height, width)"""
    w = len(array[0])
    h = len(array)
    return (h, w)


def getGreyscaleArray(array, mode="greyscale"):
    """Converts a RGB or RGBA array to greyscale\n
    RGB mode returns pixels as RGB tuples\n
    greyscale mode returns pixels as int"""
    dimensions = getDimensions(array)
    grey_array = []
    for h in range(dimensions[0]):
        row = []
        for w in range(dimensions[1]):
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


def getRGBArray(array):
    """Converts a greyscale array to RGB array"""
    dimensions = getDimensions(array)
    for h in range(dimensions[0]):
        for w in range(dimensions[1]):
            array[h][w] = greyscaleToRGB(array[h][w])
    return array


def getSurroundingPixels(array, centre, diameter):
    """Returns a list containing the surrdouing pixels"""
    centre_y = centre[0]
    centre_x = centre[1]
    centre_value = array[centre_y][centre_x]
    radius = int((diameter-1)/2)
    surroudings = []
    for h in range(centre_y - radius, centre_y + radius + 1):
        row = []
        for w in range(centre_x - radius, centre_x + radius + 1):
            if h < 0 or w < 0:
                value = centre_value
            else:
                try:
                    value = array[h][w]
                except IndexError:
                    value = centre_value
            row.append(value)
        surroudings.append(row)
    return surroudings


def applyKernelToLocal(local_array, grey_filter):
    """Apply the filter to a section of a local section"""
    output = []
    for y in range(len(grey_filter)):
        output_row = []
        for x in range(len(grey_filter)):
            # TODO: Fix index error for rectangular images
            new_value = local_array[y][x] * grey_filter[y][x]
            output_row.append(new_value)
        output.append(output_row)
    return output


def applyKernel(array, grey_filter):
    """Apply filter to greyscale array"""
    new_array = []
    if len(grey_filter[0]) % 2 == 0 or len(grey_filter) % 2 == 0:
        raise ValueError
    dimensions = getDimensions(array)
    for h in range(dimensions[0]):
        new_row = []
        for w in range(dimensions[1]):
            diameter = len(grey_filter)
            surroudings = getSurroundingPixels(array, (h, w), diameter)
            applied = applyKernelToLocal(surroudings, grey_filter)
            average = numpy.sum(applied)/len(applied)**2
            average = int(round(average))
            new_row.append(average)
        new_array.append(new_row)
    return new_array
