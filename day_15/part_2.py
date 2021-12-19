import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    risk_map = {
        (r, c): int(level_str)
        for r, row in enumerate(data.splitlines())
        for c, level_str in enumerate(row)
    }

    len_r = max(risk_map, key=lambda k: k[0])[0] + 1
    len_c = max(risk_map, key=lambda k: k[1])[1] + 1

    for i in range(4):
        for r in range(len_r):
            for c in range(len_c):
                prev = risk_map[r + i * len_r, c]
                risk_map[r + (i + 1) * len_r, c] = prev + 1 if prev < 9 else 1

    len_r *= 5
    max_r = len_r - 1

    for i in range(4):
        for r in range(len_r):
            for c in range(len_c):
                prev = risk_map[r, c + i * len_c]
                risk_map[r, c + (i + 1) * len_c] = prev + 1 if prev < 9 else 1

    len_c *= 5
    max_c = len_c - 1

    costs = {(r, c): 10 * max_r * max_c for r, c in risk_map}
    visited, unvisited = set(), set()

    unvisited.add((0, 0))
    costs[0, 0] = 0
    while unvisited:
        node = min(unvisited, key=lambda k: costs[k])
        unvisited.remove(node)
        visited.add(node)

        if node == (max_r, max_c):
            break

        r, c = node
        for next_node in ((r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)):
            if next_node not in costs:
                continue

            if next_node in visited:
                continue

            cost = costs[node] + risk_map[next_node]
            if cost < costs[next_node]:
                costs[next_node] = cost
                unvisited.add(next_node)

    return costs[max_r, max_c]


example_data = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

assert solve(example_data) == 315

print(solve(data))  # 2821
