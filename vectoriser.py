from PIL import Image
import math
import helper as hp


def getRgbArray(file):
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


def RgbArrayToGreyscale(array, mode="greyscale"):
    """Converts a RGB or RGBA array to greyscale\n
    RGB mode returns pixels as RGB tuples\n
    greyscale mode returns pixels as int"""
    dimensions = hp.getDimensions(array)
    grey_array = []
    for h in range(dimensions[0]):
        row = []
        for w in range(dimensions[1]):
            greyscale = hp.RgbToGreyscale(array[h][w])
            if mode == "RGB":
                grey_rgb = hp.greyscaleToRgb(greyscale)
                row.append(grey_rgb)
            elif mode == "greyscale":
                row.append(greyscale)
            else:
                raise ValueError
        grey_array.append(row)
    return grey_array


def applyKernel(array, grey_filter):
    """Apply kernel filter to greyscale array"""
    new_array = []
    if len(grey_filter[0]) % 2 == 0 or len(grey_filter) % 2 == 0:
        raise ValueError
    dimensions = hp.getDimensions(array)
    for h in range(dimensions[0]):
        new_row = []
        for w in range(dimensions[1]):
            diameter = len(grey_filter)
            surroudings = hp.getSurroundingPixels(array, (h, w), diameter)
            applied = hp.applyKernelToLocal(surroudings, grey_filter)
            average = hp.getSum(applied)/len(applied)**2
            average = int(round(average))
            new_row.append(average)
        new_array.append(new_row)
    return new_array


def pythagorean(array1, array2):
    """Returns an array that contains the pythagorean value for each element"""
    dimensions = hp.getDimensions(array1)
    new_array = []
    for h in range(dimensions[0]):
        new_row = []
        for w in range(dimensions[1]):
            value1 = array1[h][w]
            value2 = array2[h][w]
            new_value = (value1**2+value2**2)**0.5
            new_value = int(round(new_value))
            new_row.append(new_value)
        new_array.append(new_row)
    return new_array


def getBinary(array, threshold, invert=False):
    dimensiosns = hp.getDimensions(array)
    binary = []
    for h in range(dimensiosns[0]):
        row = []
        for w in range(dimensiosns[1]):
            if array[h][w] > threshold:
                if invert:
                    row.append(0)
                else:
                    row.append(1)
            else:
                if invert:
                    row.append(1)
                else:
                    row.append(0)
        binary.append(row)
    return binary
