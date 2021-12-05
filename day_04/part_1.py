import os
import pprint
from collections import defaultdict

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


class Cell:
    def __init__(self, n_str: str):
        self.number = int(n_str)
        self.selected = False

    def __repr__(self) -> str:
        return f"{self.number:2d} ({'×' if self.selected else ' '})"


class Board:
    def __init__(self, cells: dict[int, dict[int, Cell]]):
        self.cells = cells

        numbers = defaultdict(set)
        for row, row_items in cells.items():
            for col, cell in row_items.items():
                numbers[cell.number].add((row, col))
        self.numbers = numbers

    def mark_number(self, number: int) -> bool:
        marked = False
        for row, col in self.numbers[number]:
            if not (cell := self.cells[row][col]).selected:
                cell.selected = True
                marked = True
        return marked

    def check_bingo(self) -> bool:
        if any(all(self.cells[r][c].selected for r in range(5)) for c in range(5)):
            return True
        if any(all(self.cells[r][c].selected for c in range(5)) for r in range(5)):
            return True
        return False

    def calculate_score(self, number: int) -> int:
        return (
            sum(
                cell.number
                for row in self.cells.values()
                for cell in row.values()
                if not cell.selected
            )
            * number
        )

    def __repr__(self) -> str:
        return pprint.pformat(self.cells)


def parse_data(data: str) -> tuple[list[int], list[Board]]:
    lines = data.splitlines()

    numbers = [int(n) for n in lines[0].split(",")]

    boards = [
        Board(
            {
                row: {
                    col: Cell(lines[board + row][3 * col : 3 * col + 2])  # noqa: E203
                    for col in range(5)
                }
                for row in range(5)
            }
        )
        for board in range(2, len(lines), 6)
    ]

    return numbers, boards


def solve(data: str) -> int:
    numbers, boards = parse_data(data)

    for number in numbers:
        for board in boards:
            if board.mark_number(number) and board.check_bingo():
                return board.calculate_score(number)

    return -1


example_data = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

assert solve(example_data) == 4512

print(solve(data))  # 58838
