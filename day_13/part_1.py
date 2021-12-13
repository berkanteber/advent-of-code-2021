import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    coordinates, folds = data.split("\n\n")

    visibles = {
        tuple(int(coord_part) for coord_part in coordinate.split(","))
        for coordinate in coordinates.splitlines()
    }

    first_fold = folds.splitlines()[0].removeprefix("fold along ")

    axis, line_pos_str = first_fold.split("=")
    line_pos = int(line_pos_str)

    if axis == "x":
        to_remove = {(x, y) for x, y in visibles if x > line_pos}
        to_add = {(2 * line_pos - x, y) for x, y in to_remove}
    else:
        to_remove = {(x, y) for x, y in visibles if y > line_pos}
        to_add = {(x, 2 * line_pos - y) for x, y in to_remove}

    visibles -= to_remove
    visibles |= to_add

    return len(visibles)


example_data = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

assert solve(example_data) == 17

print(solve(data))  # 647
