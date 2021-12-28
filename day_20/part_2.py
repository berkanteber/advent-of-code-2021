import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    enhancement_algorithm, input_image_str = data.split("\n\n")

    input_image = set()
    for i, line in enumerate(input_image_str.splitlines()):
        for j, ch in enumerate(line):
            if ch == "#":
                input_image.add((i, j))

    step = 50
    buffer = 2 * step + 1
    max_i = i + buffer
    max_j = j + buffer
    min_ij = -buffer

    for _ in range(step):
        output_image = set()

        for i in range(min_ij - buffer, max_i + 1 + buffer):
            for j in range(min_ij - buffer, max_j + 1 + buffer):
                bits = ""
                neighbors = (
                    *((i - 1, j - 1), (i - 1, j), (i - 1, j + 1)),
                    *((i, j - 1), (i, j), (i, j + 1)),
                    *((i + 1, j - 1), (i + 1, j), (i + 1, j + 1)),
                )
                for (n_i, n_j) in neighbors:
                    bits += {False: "0", True: "1"}[(n_i, n_j) in input_image]

                if enhancement_algorithm[int(bits, 2)] == "#":
                    output_image.add((i, j))

        input_image = output_image

    output_image = {
        (i, j)
        for i, j in input_image
        if (i - min_ij >= step and j - min_ij >= step)
        and (max_i - i >= step and max_j - j >= step)
    }

    return len(output_image)


example_data = """\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""

assert solve(example_data) == 3351

print(solve(data))  # 15653
