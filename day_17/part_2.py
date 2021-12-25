import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    x_str, y_str = data.removeprefix("target area: ").split(", ")
    x_start_str, x_end_str = x_str[2:].split("..")
    y_start_str, y_end_str = y_str[2:].split("..")
    x_start, x_end = int(x_start_str), int(x_end_str)
    y_start, y_end = int(y_start_str), int(y_end_str)

    velocities = set()
    for x in range(1, x_end + 1):
        for y in range(1000, y_start - 1, -1):
            vel_x, vel_y = x, y
            pos_x, pos_y = 0, 0
            while pos_x <= x_end and pos_y >= y_start:
                if x_start <= pos_x <= x_end and y_start <= pos_y <= y_end:
                    velocities.add((x, y))
                    break

                pos_x += vel_x
                pos_y += vel_y

                if vel_x != 0:
                    vel_x -= vel_x // abs(vel_x)
                vel_y -= 1

    return len(velocities)


assert solve("target area: x=20..30, y=-10..-5") == 112

print(solve(data))  # 4110
