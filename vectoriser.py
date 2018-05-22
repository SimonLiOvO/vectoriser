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
    HEX = hex(greyscale * 0x00010101)
    rgb = HEXtoRGB(HEX)
    return rgb


def HEXtoRGB(HEX):
    """Converts HEX color value to a RGB tuple"""
    rgb = tuple()
    hex_color = str(hex(HEX))
    rgb = (int(hex_color[2:4], 16), int(
        hex_color[4:6], 16), int(hex_color[6:8], 16))
    return rgb
