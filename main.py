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
    unsharpen = v.AddGreyscales(greyscale, delta)
    return unsharpen


def save(greyscale, file):
    greyscale = v.GreyscaleArrayToRgb(greyscale)
    debug.saveBitmap(greyscale, file)


if __name__ == '__main__':
    image = getGreyscale("bitmap/quincy.png")
    sharpen_image = getUnsharpening(image)
    save(sharpen_image, "bitmap/sharpen_quincy.png")
