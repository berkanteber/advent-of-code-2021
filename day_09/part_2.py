import os
from collections import Counter

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    heights = [[int(cell) for cell in row] for row in data.splitlines()]

    minimums = []
    for i, row in enumerate(heights):
        for j, cell in enumerate(row):
            if j > 0 and row[j - 1] <= cell:
                continue
            if j < len(row) - 1 and row[j + 1] <= cell:
                continue
            if i > 0 and heights[i - 1][j] <= cell:
                continue
            if i < len(heights) - 1 and heights[i + 1][j] <= cell:
                continue
            minimums.append((i, j))

    cell_to_basin = {cell: cell for cell in minimums}
    new_cells_added = True
    while new_cells_added:
        new_cells_added = False
        for i, row in enumerate(heights):
            for j, cell in enumerate(row):
                if cell == 9 or (i, j) in cell_to_basin:
                    continue

                for neighbor in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)):
                    if neighbor in cell_to_basin:
                        r, c = cell_to_basin[neighbor]
                        if heights[r][c] < cell:
                            cell_to_basin[i, j] = cell_to_basin[neighbor]
                            new_cells_added = True
                            break

    basin_sizes = Counter(cell_to_basin.values())

    (_, first), (_, second), (_, third) = basin_sizes.most_common(3)

    return first * second * third


example_data = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""

assert solve(example_data) == 1134

print(solve(data))  # 1148965
