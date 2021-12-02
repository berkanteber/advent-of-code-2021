import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()

numbers = [int(x) for x in data.splitlines()]


def solve(nums: list[int]) -> int:
    inc = 0
    for i in range(len(nums) - 1):
        prev, cur = nums[i], nums[i + 1]
        if cur > prev:
            inc += 1

    return inc


assert solve([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7

print(solve(numbers))  # 1226
