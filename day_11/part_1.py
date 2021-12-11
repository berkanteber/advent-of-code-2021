import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    energy_levels = {}
    for r, line in enumerate(data.splitlines()):
        for c, energy in enumerate(line):
            energy_levels[r, c] = int(energy)

    total_flashes = 0
    for _ in range(100):
        for octopus in energy_levels:
            energy_levels[octopus] += 1

        flashed = set()
        to_flash = {
            octopus
            for octopus, energy_level in energy_levels.items()
            if energy_level == 10
        }
        while to_flash:
            octopus = to_flash.pop()
            energy_levels[octopus] = 0
            flashed.add(octopus)

            r, c = octopus
            neighbors = (
                *((r + 1, c - 1), (r + 1, c), (r + 1, c + 1)),
                *((r - 1, c - 1), (r - 1, c), (r - 1, c + 1)),
                *((r, c - 1), (r, c + 1)),
            )
            for neighbor in neighbors:
                n_r, n_c = neighbor
                if not (0 <= n_r < 10 and 0 <= n_c < 10):
                    continue

                if neighbor in flashed or neighbor in to_flash:
                    continue

                energy_levels[neighbor] += 1
                if energy_levels[neighbor] == 10:
                    to_flash.add(neighbor)

        total_flashes += len(flashed)

    return total_flashes


example_data = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

assert solve(example_data) == 1656

print(solve(data))  # 1637
