import os
from collections import defaultdict

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    edges = defaultdict(set)
    for line in data.splitlines():
        x, y = line.split("-")
        if x != "end" and y != "start":
            edges[x].add(y)
        if x != "start" and y != "end":
            edges[y].add(x)

    total_paths = 0
    remaining_paths: set[tuple[str, ...]] = {("start",)}
    while remaining_paths:
        current_path = remaining_paths.pop()
        node = current_path[-1]

        if node == "end":
            total_paths += 1
            continue

        smalls = [prev_node for prev_node in current_path if prev_node.islower()]
        small_visited_twice = len(smalls) > len(set(smalls))

        remaining_paths.update(
            (*current_path, next_node)
            for next_node in edges[node]
            if not (
                small_visited_twice
                and next_node.islower()
                and next_node in current_path
            )
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

assert solve(example_data) == 36

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

assert solve(example_data) == 103

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

assert solve(example_data) == 3509

print(solve(data))  # 131228
