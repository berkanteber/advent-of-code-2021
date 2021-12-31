import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    player1_str, player2_str = data.splitlines()

    positions = {1: int(player1_str.split()[-1]), 2: int(player2_str.split()[-1])}
    scores = {1: 0, 2: 0}

    dice_turn = 0
    while scores[1] < 1000 and scores[2] < 1000:
        dice_total = 0
        for _ in range(3):
            dice_total += dice_turn % 100 + 1
            dice_turn += 1

        turn = 1 if (dice_turn // 3) % 2 == 1 else 2
        positions[turn] = (positions[turn] + dice_total - 1) % 10 + 1
        scores[turn] += positions[turn]

    lower_score = min(scores.values())

    return dice_turn * lower_score


example_data = """\
Player 1 starting position: 4
Player 2 starting position: 8
"""

assert solve(example_data) == 739785

print(solve(data))  # 798147
