import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    internal_days = {day: 0 for day in range(9)}
    for day in data.split(","):
        internal_days[int(day)] += 1

    for _ in range(80):
        internal_days = {
            **{day: internal_days[day + 1] for day in {0, 1, 2, 3, 4, 5, 7}},
            6: internal_days[0] + internal_days[7],
            8: internal_days[0],
        }

    return sum(internal_days.values())


assert solve("3,4,3,1,2") == 5934

print(solve(data))  # 383160
