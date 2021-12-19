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

    max_r = max(risk_map, key=lambda k: k[0])[0]
    max_c = max(risk_map, key=lambda k: k[1])[1]

    costs = {(r, c): 10 * max_r * max_c for r, c in risk_map}
    unvisited = {(r, c) for r, c in risk_map}

    costs[0, 0] = 0
    while unvisited:
        node = min(unvisited, key=lambda k: costs[k])
        unvisited.remove(node)

        if node == (max_r, max_c):
            break

        r, c = node
        for next_node in ((r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)):
            if next_node not in unvisited:
                continue

            cost = costs[node] + risk_map[next_node]
            if cost < costs[next_node]:
                costs[next_node] = cost

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

assert solve(example_data) == 40

print(solve(data))  # 487
