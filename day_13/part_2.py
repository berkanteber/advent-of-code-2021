import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> str:
    coordinates, folds = data.split("\n\n")

    visibles = {
        tuple(int(coord_part) for coord_part in coordinate.split(","))
        for coordinate in coordinates.splitlines()
    }

    for fold in folds.splitlines():
        axis, line_pos_str = fold.removeprefix("fold along ").split("=")
        line_pos = int(line_pos_str)

        if axis == "x":
            to_remove = {(x, y) for x, y in visibles if x > line_pos}
            to_add = {(2 * line_pos - x, y) for x, y in to_remove}
        else:
            to_remove = {(x, y) for x, y in visibles if y > line_pos}
            to_add = {(x, 2 * line_pos - y) for x, y in to_remove}

        visibles -= to_remove
        visibles |= to_add

    map_str = ""
    for j in range(max(y for _, y in visibles) + 1):
        for i in range(max(x for x, _ in visibles) + 1):
            map_str += "#" if (i, j) in visibles else "."
        map_str += "\n"

    return map_str


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

example_result = """\
#####
#...#
#...#
#...#
#####
"""

assert solve(example_data) == example_result

print(solve(data), end="")  # HEJHJRCJ

#  #..#.####...##.#..#...##.###...##....##
#  #..#.#.......#.#..#....#.#..#.#..#....#
#  ####.###.....#.####....#.#..#.#.......#
#  #..#.#.......#.#..#....#.###..#.......#
#  #..#.#....#..#.#..#.#..#.#.#..#..#.#..#
#  #..#.####..##..#..#..##..#..#..##...##.
