import os

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
            minimums.append(cell)

    return sum(cell + 1 for cell in minimums)


example_data = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""

assert solve(example_data) == 15

print(solve(data))  # 417
