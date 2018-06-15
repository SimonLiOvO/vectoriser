import image as i


def getGaussianBlur(greyscale):
    """Blurs the image"""
    blur_kernel = [[0.125, 0.25, 0.125], [0.25, 0.5, 0.25], [0.125, 0.25, 0.125]]
    blur = i.applyKernel(greyscale, blur_kernel)
    return blur


def getEdges(greyscale):
    """Returns the edges"""
    # Edges are white
    # Backgroun is black
    # When passing the edge greyscale to binary function, turn on the invert paramater
    sobel_x_kernel = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y_kernel = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    sobel_x = i.applyKernel(greyscale, sobel_x_kernel)
    sobel_y = i.applyKernel(greyscale, sobel_y_kernel)
    edges = i.pythagorean(sobel_x, sobel_y)
    return edges
