import os
from itertools import product

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    player1_str, player2_str = data.splitlines()
    initial_positions = (int(player1_str.split()[-1]), int(player2_str.split()[-1]))

    total_score = 0
    universes = {total_score: {(initial_positions, (0, 0), 1): 1}}
    wins = {1: 0, 2: 0}

    current_score = 0
    while universes:
        while current_score not in universes:
            current_score += 1

        state, count = universes[current_score].popitem()

        for dice_rolls in product((1, 2, 3), repeat=3):
            (position1, position2), (score1, score2), turn = state

            if turn == 1:
                position1 = (position1 + sum(dice_rolls) - 1) % 10 + 1
                score1 += position1
                if score1 >= 21:
                    wins[1] += count
                    continue
            else:
                position2 = (position2 + sum(dice_rolls) - 1) % 10 + 1
                score2 += position2
                if score2 >= 21:
                    wins[2] += count
                    continue

            total_score = score1 + score2
            if total_score not in universes:
                universes[total_score] = {}

            new_state = ((position1, position2), (score1, score2), 3 - turn)

            if new_state not in universes[total_score]:
                universes[total_score][new_state] = 0

            universes[total_score][new_state] += count

        if not universes[current_score]:
            universes.pop(current_score)

    return max(wins.values())


example_data = """\
Player 1 starting position: 4
Player 2 starting position: 8
"""

assert solve(example_data) == 444356092776315

print(solve(data))  # 809953813657517
