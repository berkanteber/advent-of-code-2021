import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    closing = {"<": ">", "{": "}", "[": "]", "(": ")"}
    points = {">": 25137, "}": 1197, "]": 57, ")": 3}

    total = 0
    for line in data.splitlines():
        stack = []
        for char in line:
            if char in "<{[(":
                stack.append(char)
            elif char == closing[stack.pop()]:
                continue
            else:
                total += points[char]
                break

    return total


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

assert solve(example_data) == 26397

print(solve(data))  # 315693
