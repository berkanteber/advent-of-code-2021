import os
from statistics import median_low

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    closing = {"<": ">", "{": "}", "[": "]", "(": ")"}
    points = {">": 4, "}": 3, "]": 2, ")": 1}

    totals = []
    for line in data.splitlines():
        stack = []
        for char in line:
            if char in "<{[(":
                stack.append(char)
            elif char == closing[stack.pop()]:
                continue
            else:
                break
        else:
            total = 0
            while stack:
                total = total * 5 + points[closing[stack.pop()]]
            totals.append(total)

    return median_low(totals)


example_data = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

assert solve(example_data) == 288957

print(solve(data))  # 1870887234
