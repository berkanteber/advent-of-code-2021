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
    length = len(positions)

    cost = sum(positions)
    candidate_pos = 1
    gte_index = 0
    while candidate_pos <= max_pos:
        while positions[gte_index] < candidate_pos:
            gte_index += 1

        new_cost = cost - (length - gte_index) + gte_index
        if new_cost < cost:
            cost = new_cost
            candidate_pos += 1
        else:
            break

    return cost


assert solve("16,1,2,0,4,2,7,1,2,14") == 37

print(solve(data))  # 348996
