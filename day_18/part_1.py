import ast
import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    numbers = list(map(ast.literal_eval, data.splitlines()))
    numbers.reverse()

    while len(numbers) > 1:
        total = [numbers.pop(), numbers.pop()]
        total_str = str(total).replace(" ", "")

        while True:
            d5s = []
            last_d5_start = None
            depth = 0
            for i, ch in enumerate(total_str):
                if ch == "[":
                    depth += 1
                    if depth == 5:
                        last_d5_start = i
                elif ch == "]":
                    if depth == 5:
                        d5s.append((last_d5_start, i))
                        last_d5_start = None
                    depth -= 1

            exploded = False
            for d5_start, d5_end in d5s:
                d5 = ast.literal_eval(total_str[d5_start : d5_end + 1])
                if not isinstance(d5, list) or len(d5) != 2:
                    continue

                d5_first, d5_second = d5
                if not (isinstance(d5_first, int) and isinstance(d5_second, int)):
                    continue

                total_str_before = total_str[:d5_start]
                prev_idx_end = len(total_str_before) - 1
                while prev_idx_end >= 0:
                    if total_str_before[prev_idx_end] in "0123456789":
                        prev_idx_start = prev_idx_end
                        while total_str_before[prev_idx_start] in "0123456789":
                            prev_idx_start -= 1
                        prev_idx_start += 1

                        pre_prev = total_str_before[:prev_idx_start]
                        post_prev = total_str_before[prev_idx_end + 1 :]

                        prev_num = int(
                            total_str_before[prev_idx_start : prev_idx_end + 1]
                        )
                        total_str_before = (
                            pre_prev + str(prev_num + d5_first) + post_prev
                        )
                        break
                    prev_idx_end -= 1

                total_str_after = total_str[d5_end + 1 :]
                next_idx_start = 0
                while next_idx_start < len(total_str_after):
                    if total_str_after[next_idx_start] in "0123456789":
                        next_idx_end = next_idx_start
                        while total_str_after[next_idx_end] in "0123456789":
                            next_idx_end += 1
                        next_idx_end -= 1

                        pre_next = total_str_after[:next_idx_start]
                        post_next = total_str_after[next_idx_end + 1 :]

                        next_num = int(
                            total_str_after[next_idx_start : next_idx_end + 1]
                        )
                        total_str_after = (
                            pre_next + str(next_num + d5_second) + post_next
                        )
                        break
                    next_idx_start += 1

                total_str = total_str_before + "0" + total_str_after
                exploded = True
                break

            if exploded:
                continue

            splitted = False
            num_start = None
            for i, ch in enumerate(total_str):
                if ch in "0123456789" and num_start is None:
                    num_start = i
                elif (ch == "," or ch == "]") and num_start is not None:
                    if i - num_start > 1:
                        num = int(total_str[num_start:i])
                        splitted_lst = [num // 2, (num + 1) // 2]
                        splitted_str = str(splitted_lst).replace(" ", "")
                        total_str = total_str[:num_start] + splitted_str + total_str[i:]
                        splitted = True
                        break
                    else:
                        num_start = None

            if splitted:
                continue

            break

        numbers.append(ast.literal_eval(total_str))

    (number,) = numbers

    magnitude = 0
    stack: list[tuple[int, int | list]] = [(1, number)]  # type: ignore[type-arg]
    while stack:
        coefficient, item = stack.pop()
        if isinstance(item, int):
            magnitude += coefficient * item
            continue

        first, second, *_ = item
        stack.append((3 * coefficient, first))
        stack.append((2 * coefficient, second))

    return magnitude


example_data = """\
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""

assert solve(example_data) == 4140

print(solve(data))  # 4120
