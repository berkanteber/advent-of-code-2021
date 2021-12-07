import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    positions = [int(pos) for pos in data.split(",")]
    positions.sort()
    min_pos = positions[0]
    positions = [pos - min_pos for pos in positions]
    max_pos = positions[-1]

    cost = sum(pos * (pos + 1) // 2 for pos in positions)

    candidate_pos = 1
    while candidate_pos <= max_pos:
        new_cost = 0
        for pos in positions:
            dist = abs(pos - candidate_pos)
            new_cost += dist * (dist + 1) // 2

        if new_cost < cost:
            cost = new_cost
            candidate_pos += 1
        else:
            break

    return cost


assert solve("16,1,2,0,4,2,7,1,2,14") == 168

print(solve(data))  # 98231647
