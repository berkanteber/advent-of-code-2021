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

        x_step = 1 if e_x > s_x else -1
        y_step = 1 if e_y > s_y else -1

        if s_x != e_x and s_y != e_y:
            if abs(s_x - e_x) != abs(s_y - e_y):
                continue
            for i in range(abs(s_x - e_x) + 1):
                field[s_x + i * x_step, s_y + i * y_step] += 1
        else:
            for x in range(s_x, e_x + x_step, x_step):
                for y in range(s_y, e_y + y_step, y_step):
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

assert solve(example_data) == 12

print(solve(data))  # 23864
