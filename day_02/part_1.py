import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()

lines = data.splitlines()


def solve(commands: list[str]) -> int:
    depth = fwd = 0
    for command in commands:
        cmd, n_str = command.split()
        n = int(n_str)
        if cmd == "forward":
            fwd += n
        elif cmd == "down":
            depth += n
        elif cmd == "up":
            depth -= n
    return depth * fwd


assert (
    solve(
        [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2",
        ]
    )
    == 150
)

print(solve(lines))  # 1484118
