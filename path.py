import helper as hp
from matplotlib import path
from shapely.geometry import Polygon


def getCorner(tuple, binary):
    """Returns four pixels of the given corner from (0, 0) in clockwise order."""
    # Point is at the upper-left corner of the pixel with the same coordinate
    y = tuple[0]
    x = tuple[1]
    height, width = hp.getDimensions(binary)
    if y - height > 1 or x - width > 1:
        raise IndexError("Out of index")
    if y < 0 or x < 0:
        raise IndexError("Index must be postive")
    # Clockwise from 0, 0
    deltas = [(-1, -1), (-1, 0), (0, 0), (0, -1)]
    adjacent_pixels = []
    for delta in deltas:
        try:
            new_y = y+delta[0]
            new_x = x+delta[1]
            if new_y < 0 or new_x < 0:
                # Fill in white pixels for out of bound
                pixel = 1
            else:
                # Fill in white pixels for out of bound
                pixel = binary[new_y][new_x]
        except IndexError:
            pixel = 1
        adjacent_pixels.append(pixel)
    return adjacent_pixels


def diagonalCompensate(tuple, binary, invert):
    """Adds an extra pixel when four pixels are diagonal"""
    # This function is the workaround for the diagonal tracing problem
    # It only solve half of the possible diagonal scenarios
    pixels = getCorner(tuple, binary)
    if pixels == [1, 0, 1, 0]:
        if invert:
            binary[tuple[0]-1][tuple[1]] = 1
        else:
            binary[tuple[0]-1][tuple[1]-1] = 0
    if pixels == [0, 1, 0, 1]:
        if invert:
            binary[tuple[0]][tuple[1]] = 1
        else:
            binary[tuple[0]-1][tuple[1]] = 0
    return binary


def getNextCorner(tuple, binary, invert=False):
    """Returns a list that contains possible next steps of the path."""
    binary = diagonalCompensate(tuple, binary, invert=invert)
    pixels = getCorner(tuple, binary)
    points = []
    # append if there is a black pixel on the left and a white pixel on the right
    if pixels[0] == 0 and pixels[1] == 1:
        points.append((tuple[0] - 1, tuple[1]))
    if pixels[1] == 0 and pixels[2] == 1:
        points.append((tuple[0], tuple[1] + 1))
    if pixels[2] == 0 and pixels[3] == 1:
        points.append((tuple[0]+1, tuple[1]))
    if pixels[3] == 0 and pixels[0] == 1:
        points.append((tuple[0], tuple[1] - 1))
    return points, binary


def detectDeadend(possible_points, path):
    """Remove points that alrready exist from the possible point list"""
    # Removes point if already exists in the path
    # It is this function that raises error when diagonal bug occurs
    for point in possible_points:
        if point in path:
            previous_index = path.index(point)-1
            if previous_index > -1:
                possible_points.remove(point)
    return possible_points


def findEdge(tuple, binary):
    path = [(tuple), ]
    binary = binary
    # Keep finding edge until exit expression is satified
    while True:
        # If a closed path is form, exit the function
        if len(path) > 1 and path[0] == path[-1]:
            print("")
            return path
        else:
            print("Tracing at {} \r".format((path[-1])), end="")
            # Finds the pixels with normal diagonal setting (Adds extra black pixel)
            try:
                possible_points, binary = getNextCorner(path[-1], binary)
                next_point = detectDeadend(possible_points, path)[0]
            # Finds the pixels with invert setting if normal setting fails (Adds white pixel instead)
            except IndexError:
                try:
                    possible_points, binary = getNextCorner(path[-1], binary, invert=True)
                    next_point = detectDeadend(possible_points, path)[0]
                # If both methods fail, output the last 10 pixels for debugging and raise error
                except IndexError:
                    print("")
                    print("Last 10 points of the path: {}".format(path[-10:]))
                    raise IndexError("This error should only occur when processing diagonal pixels, refer to readme.md for more info.")
            # Append next point to path
            path.append(next_point)


def invert(edge_path, binary):
    """Invert pixels inside the path"""
    # We invert the pixels in the path after it is completed
    # So that the patch of pixels will not be traced again
    # we can also trace the inner edge (if there is one) as well if it is inverted

    # Finds the area where the path locates
    min_y = min(edge_path, key = lambda t: t[0])[0]
    min_x = min(edge_path, key = lambda t: t[1])[1]
    max_y = max(edge_path, key = lambda t: t[0])[0]
    max_x = max(edge_path, key = lambda t: t[1])[1]
    # Creates a shapely path object
    p = path.Path(edge_path)
    for h in range(min_y, max_y+1):
        for w in range(min_x, max_x):
            print("Inverting at {} \r".format((h, w)), end="")
            # Uses shapely's contains_point func to check if a point is in the path
            if p.contains_points([(h+0.5, w+0.5)])[0]:
                # Invert the pixel if it is
                binary[h][w] = 1 - binary[h][w]
    print("")
    # Return the inverted binary array
    return binary


def decompose(binary):
    """Decompose the binary image into a bunch of closed paths"""
    binary = binary
    dimensions = hp.getDimensions(binary)
    paths = []
    for h in range(dimensions[0]+1):
        for w in range(dimensions[1]+1):
            print("Looking for edges at {} \r".format((h, w)), end="")
            if getNextCorner((h, w), binary)[0]:
                edge_path = findEdge((h, w), binary)
                paths.append(edge_path)
                binary = invert(edge_path, binary)
    return paths


def reduceByArea(paths, threshold):
    """Remove paths smaller than the threshold"""
    reduced = []
    for path in paths:
        polygon = Polygon(path)
        if polygon.area >= threshold:
            reduced.append(path)
    return reduced


def checkStraightLineDistance(line_starts, line_ends, point):
    """
    Return True if distance between the point and straight line is bigger
    than 1
    """
    # Equation: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line#Line_defined_by_an_equation
    y1, x1 = line_starts
    y2, x2 = line_ends
    y0, x0 = point
    numerator = abs((y2-y1)*x0 - (x2 - x1)*y0 + x2*y1 - y2*x1)
    denominator = ((y2 - y1)**2 + (x2 - x1)**2)**0.5
    if denominator == 0:
        return False
    distance = numerator/denominator
    if distance > 0.5:
        return True
    else:
        return False


def getStraightLines(closed_path):
    """Decompose a closed_path into stright lines"""
    closed_path = closed_path
    lines = []
    while True:
        # Exit expression
        if len(lines) > 1:
            if lines[0][0] == lines[-1][-1]:
                return lines
        stop_line = False
        straight_line = []
        # Adds the first pixel to the line
        if len(straight_line) == 0:
            straight_line.append(closed_path[0])
        # Loops through the closed_path
        for i in range(1, len(closed_path)):
            for s_point in straight_line:
                if checkStraightLineDistance(straight_line[0], closed_path[i], s_point):
                    # Uses a flag to pass the stop_line message out of the loop
                    stop_line = True
                    break
            if stop_line:
                lines.append(straight_line)
                # Chop the closed_path
                closed_path = closed_path[i:]
                break
            else:
                # Add new point to straight line
                straight_line.append(closed_path[i])
        if stop_line:
            # Start the process again
            continue
        else:
            lines.append(straight_line)
            closed_path = closed_path[i:]


def svgConstructor(polygon):
    """returns a svg path setting"""
    # M = "move to" (point)
    # L = "line to" (point tp point)
    # Z = "close the path" (point tp point)
    string = ""
    string += "M{},{}".format(polygon[0][0][1], polygon[0][0][0])
    for i in range(0, len(polygon)):
        string += " L{},{}".format(polygon[i][-1][1], polygon[i][-1][0])
    string += " Z"
    return string