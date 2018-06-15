import image as i
import debug


def getGaussianBlur(greyscale):
    blur_kernel = [[0.125, 0.25, 0.125], [0.25, 0.5, 0.25], [0.125, 0.25, 0.125]]
    blur = i.applyKernel(greyscale, blur_kernel)
    return blur


def getEdges(greyscale):
    sobel_x_kernel = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y_kernel = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    sobel_x = i.applyKernel(greyscale, sobel_x_kernel)
    sobel_y = i.applyKernel(greyscale, sobel_y_kernel)
    edges = i.pythagorean(sobel_x, sobel_y)
    return edges