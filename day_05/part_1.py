import os
from collections import defaultdict

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    lines = data.splitlines()

    field: dict[tuple[int, int], int] = defaultdict(int)
    for line in lines:
        start, _, end = line.partition(" -> ")
        s_x_str, s_y_str = start.split(",")
        e_x_str, e_y_str = end.split(",")
        s_x, s_y = int(s_x_str), int(s_y_str)
        e_x, e_y = int(e_x_str), int(e_y_str)

        if s_x != e_x and s_y != e_y:
            continue

        x_range = range(s_x, e_x + 1) if e_x >= s_x else range(e_x, s_x + 1)
        y_range = range(s_y, e_y + 1) if e_y >= s_y else range(e_y, s_y + 1)

        for x in x_range:
            for y in y_range:
                field[x, y] += 1

    return len([coord for coord, ctr in field.items() if ctr > 1])


example_data = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

assert solve(example_data) == 5

print(solve(data))  # 6005
