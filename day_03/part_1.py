import os
from collections import defaultdict

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()

lines = data.splitlines()


def solve(binary_nums: list[str]) -> int:
    bit_counts: dict[int, int] = defaultdict(int)
    for b_num in binary_nums:
        for pos, bit_str in enumerate(b_num[::-1]):
            bit_counts[pos] += int(bit_str)

    gamma = epsilon = 0
    for pos, count in bit_counts.items():
        if count > len(binary_nums) / 2:
            gamma += 2 ** pos
        else:
            epsilon += 2 ** pos

    return gamma * epsilon


assert (
    solve(
        [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
    )
    == 198
)

print(solve(lines))  # 841526
