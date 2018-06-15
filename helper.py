"""This file stores functions that are not meant be directly called by users."""


def getDimensions(array):
    """Returns the width and height of the bitmap iamge in a tuple (height, width)"""
    h = len(array)
    w = len(array[0])
    return (h, w)


def RgbToGreyscale(rgb):
    """Converts a RGB tuple to greyscale value"""
    try:
        # Different weight for different colour wave length
        greyscale = 0.2989*rgb[0]+0.5870*rgb[1]+0.1140*rgb[2]
    except TypeError:
        # Some iamge compression stores greyscale when there is no colour
        greyscale = rgb
    greyscale = int(round(greyscale))
    return greyscale


def greyscaleToRgb(greyscale):
    """Converts a greyscale int to a RGB tuple"""
    rgb = (greyscale, greyscale, greyscale)
    return rgb


def applyKernelToLocal(local_array, grey_filter):
    """Apply the filter to a section of a local section"""
    # Multiple the respective kernel value and average everything out
    output = []
    for y in range(len(grey_filter)):
        output_row = []
        for x in range(len(grey_filter)):
            new_value = local_array[y][x] * grey_filter[y][x]
            output_row.append(new_value)
        output.append(output_row)
    return output


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
                # fill in centre value if out of bound
                value = centre_value
            else:
                try:
                    value = array[h][w]
                except IndexError:
                    # fill in centre value if out of bound
                    value = centre_value
            row.append(value)
        surroudings.append(row)
    return surroudings


def getAreaThreshold(binary, percentage=0, abs=None):
    """
    Calulate the threshold given the precentage of the binary size\n
    If you want a 2% threshold, precentage parameter should be 0.02\n
    You can also abs parameter to specify the absolute threshold
    """
    if abs:
        area = abs
    else:
        dimensiosn = getDimensions(binary)
        area = dimensiosn[0]*dimensiosn[1]*percentage
    return area


def getSum(list):
    """Returns the sum of 2D array"""
    total = 0
    for row in list:
        total += sum(row)
    return total