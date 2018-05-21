from PIL import Image


def getBitmapSize(array):
    """Returns the width and height of the bitmap iamge in a tuple"""
    x = len(array[0])
    y = len(array)
    return (x, y)


def saveNewBitmap(array, filename):
    """Saves a new bitmap image file. Debug use only."""
