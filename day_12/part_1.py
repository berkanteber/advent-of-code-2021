import os
from collections import defaultdict

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    edges = defaultdict(set)
    for line in data.splitlines():
        x, y = line.split("-")
        edges[x].add(y)
        edges[y].add(x)

    total_paths = 0
    remaining_paths: set[tuple[str, ...]] = {("start",)}
    while remaining_paths:
        current_path = remaining_paths.pop()
        node = current_path[-1]

        if node == "end":
            total_paths += 1
            continue

        remaining_paths.update(
            (*current_path, next_node)
            for next_node in edges[node]
            if not (next_node.islower() and next_node in current_path)
        )

    return total_paths


example_data = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

assert solve(example_data) == 10

example_data = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

assert solve(example_data) == 19

example_data = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

assert solve(example_data) == 226

print(solve(data))  # 5228
