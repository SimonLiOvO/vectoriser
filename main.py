import vectoriser as v
import debug


def getGreyscale(file):
    rgb = v.getRgbArray(file)
    greyscale = v.RgbArrayToGreyscale(rgb)
    return greyscale


def getRadiusBlur(getGreyscale):
    blur_kernel = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    blur = v.applyKernel(getGreyscale, blur_kernel)
    return blur


def getEdges(greyscale):
    sobel_x_kernel = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y_kernel = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    sobel_x = v.applyKernel(greyscale, sobel_x_kernel)
    sobel_y = v.applyKernel(greyscale, sobel_y_kernel)
    edges = v.pythagorean(sobel_x, sobel_y)
    return edges


def save(greyscale, file):
    greyscale = v.GreyscaleArrayToRgb(greyscale)
    debug.saveBitmap(greyscale, file)


if __name__ == '__main__':
    image = getGreyscale("bitmap/twitter.png")
    image = getRadiusBlur(image)
    image = getRadiusBlur(image)
    save(getEdges(image), "bitmap/blur_edge_twitter.png")
