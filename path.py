import helper as hp
from matplotlib import path
from shapely.geometry import Polygon


question = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

nine = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
]


def getCorner(tuple, binary):
    """Returns four pixels of the given corner from (0, 0) in clockwise order."""
    y = tuple[0]
    x = tuple[1]
    height, width = hp.getDimensions(binary)
    if y - height > 1 or x - width > 1:
        raise IndexError("Out of index")
    if y < 0 or x < 0:
        raise IndexError("Index must be postive")
    deltas = [(-1, -1), (-1, 0), (0, 0), (0, -1)]
    adjacent_pixels = []
    for delta in deltas:
        try:
            new_y = y+delta[0]
            new_x = x+delta[1]
            if new_y < 0 or new_x < 0:
                pixel = 1
            else:
                pixel = binary[new_y][new_x]
        except IndexError:
            pixel = 1
        adjacent_pixels.append(pixel)
    return adjacent_pixels


def diagonalCompensate(tuple, binary, invert):
    """Adds an extra pixel when four pixels are diagonal"""
    pixels = getCorner(tuple, binary)
    if pixels == [1, 0, 1, 0]:
        if invert:
            binary[tuple[0]-1][tuple[1]] = 1
        else:
            binary[tuple[0]][tuple[1]] = 0
    if pixels == [0, 1, 0, 1]:
        if invert:
            binary[tuple[0]-1][tuple[1]-1] = 1
        else:
            binary[tuple[0]][tuple[1]-1] = 0
    return binary


def getNextCorner(tuple, binary, invert=False):
    """Returns a list that contains possible next steps of the path."""
    binary = diagonalCompensate(tuple, binary, invert=invert)
    pixels = getCorner(tuple, binary)
    points = []
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
    for point in possible_points:
        if point in path:
            previous_index = path.index(point)-1
            if previous_index > -1:
                possible_points.remove(point)
    return possible_points


def findEdge(tuple, binary):
    path = [(tuple), ]
    binary = binary
    while True:
        if len(path) > 1 and path[0] == path[-1]:
            return path
        else:
            print("finding edge", path[-1])
            try:
                possible_points, binary = getNextCorner(path[-1], binary)
                next_point = detectDeadend(possible_points, path)[0]
            except IndexError:
                try:
                    possible_points, binary = getNextCorner(path[-1], binary, invert=True)
                    next_point = detectDeadend(possible_points, path)[0]
                except IndexError:
                    raise IndexError("This error should only occur when processing diagonal pixels, refer to readme.md for more info.")
            path.append(next_point)


def decompose(binary):
    """Decompose the binary image into a bunch of closed paths"""
    binary = binary
    dimensions = hp.getDimensions(binary)
    paths = []
    for h in range(dimensions[0]+1):
        for w in range(dimensions[1]+1):
            print(h, w)
            if getNextCorner((h, w), binary)[0]:
                edge_path = findEdge((h, w), binary)
                paths.append(edge_path)
                p = path.Path(edge_path)
                for h in range(dimensions[0]):
                    for w in range(dimensions[1]):
                        if p.contains_points([(h+0.5, w+0.5)])[0]:
                            binary[h][w] = 1 - binary[h][w]
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
        if len(lines) > 1:
            if lines[0][0] == lines[-1][-1]:
                return lines
        stop_line = False
        straight_line = []
        if len(straight_line) == 0:
            straight_line.append(closed_path[0])
        for i in range(1, len(closed_path)):
            for s_point in straight_line:
                if checkStraightLineDistance(straight_line[0], closed_path[i], s_point):
                    stop_line = True
                    break
            if stop_line:
                lines.append(straight_line)
                closed_path = closed_path[i:]
                break
            else:
                straight_line.append(closed_path[i])
        if stop_line:
            continue
        else:
            lines.append(straight_line)
            closed_path = closed_path[i:]


def svgConstructor(polygon):
    """returns a svg path setting"""
    string = ""
    string += "M{},{}".format(polygon[0][0][1], polygon[0][0][0])
    for i in range(0, len(polygon)):
        string += " L{},{}".format(polygon[i][-1][1], polygon[i][-1][0])
    string += " Z"
    return string


if __name__ == "__main__":
    paths = decompose(question)
    paths = reduceByArea(paths, hp.getAreaThreshold(paths, 0.02))
    for path in paths:
        straight_line = getStraightLines(path)
        print(svgConstructor(straight_line))
    # print(getCorner((17,38), twitter))