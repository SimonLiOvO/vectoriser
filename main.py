import vectoriser as v
import debug


def getGreyscale(file):
    rgb = v.getRgbArray(file)
    greyscale = v.RgbArrayToGreyscale(rgb)
    return greyscale


def getGaussianBlur(greyscale):
    blur_kernel = [[0.125, 0.25, 0.125], [0.25, 0.5, 0.25], [0.125, 0.25, 0.125]]
    blur = v.applyKernel(greyscale, blur_kernel)
    return blur


def getEdges(greyscale):
    sobel_x_kernel = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y_kernel = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    sobel_x = v.applyKernel(greyscale, sobel_x_kernel)
    sobel_y = v.applyKernel(greyscale, sobel_y_kernel)
    edges = v.pythagorean(sobel_x, sobel_y)
    return edges


def getUnsharpening(greyscale):
    blur = getGaussianBlur(greyscale)
    delta = v.getGreyscaleDelta(greyscale, blur)
    sharpen = getsharpMask(delta)
    unsharpen = v.AddGreyscales(greyscale, sharpen)
    return unsharpen


def getsharpMask(greyscale):
    unsharp_kernel = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    unsharp = v.applyKernel(greyscale, unsharp_kernel)
    return unsharp


def save(greyscale, file):
    greyscale = v.GreyscaleArrayToRgb(greyscale)
    debug.saveBitmap(greyscale, file)