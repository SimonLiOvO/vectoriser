import helper as hp
from matplotlib import path

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


def getNextCorner(tuple, binary):
    """Returns a list that contains possible next steps of the path."""
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
    return points


def findEdge(tuple, binary, path=[]):
    path = path
    if len(path) == 0:
        return findEdge(tuple, binary, path=[(tuple)])
    if len(path) > 1 and path[0] == path[-1]:
        return path
    else:
        next_points = getNextCorner(tuple, binary)
        for point in next_points:
            if point in path:
                previous_index = path.index(point)-1
                if previous_index > -1:
                    if path[previous_index] == tuple:
                        next_points.remove(point)
            next_point = next_points[0]
        path.append(next_point)
        return findEdge(next_point, binary, path=path)


def invert(edge_path, binary):
    """Invert pixels included in the path"""
    p = path.Path(edge_path)
    dimensions = hp.getDimensions(binary)
    for h in range(dimensions[0]):
        for w in range(dimensions[1]):
            if p.contains_points([(h+0.5, w+0.5)])[0]:
                binary[h][w] = 1 - binary[h][w]
    return binary


def decompose(binary):
    binary = binary
    dimensions = hp.getDimensions(binary)
    paths = []
    for h in range(dimensions[0]+1):
        for w in range(dimensions[1]+1):
            if getNextCorner((h, w), binary):
                edge_path = findEdge((h, w), binary)
                paths.append(edge_path)
                p = path.Path(edge_path)
                for h in range(dimensions[0]):
                    for w in range(dimensions[1]):
                        if p.contains_points([(h+0.5, w+0.5)])[0]:
                            binary[h][w] = 1 - binary[h][w]
    return paths


if __name__ == "__main__":
    a = decompose(question)
    for path in a:
        print(path)
