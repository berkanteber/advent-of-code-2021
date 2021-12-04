import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()

lines = data.splitlines()


def solve(binary_nums: list[str]) -> int:
    pos = 0
    o2_gen_lst = binary_nums
    while len(o2_gen_lst) > 1:
        bit_count = sum(int(b_num[pos]) for b_num in o2_gen_lst)
        keep = "1" if bit_count >= len(o2_gen_lst) / 2 else "0"
        o2_gen_lst = [b_num for b_num in o2_gen_lst if b_num[pos] == keep]
        pos += 1

    pos = 0
    co2_scrubber_lst = binary_nums
    while len(co2_scrubber_lst) > 1:
        bit_count = sum(int(b_num[pos]) for b_num in co2_scrubber_lst)
        keep = "1" if bit_count < len(co2_scrubber_lst) / 2 else "0"
        co2_scrubber_lst = [b_num for b_num in co2_scrubber_lst if b_num[pos] == keep]
        pos += 1

    return int(o2_gen_lst[0], 2) * int(co2_scrubber_lst[0], 2)


assert (
    solve(
        [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]
    )
    == 230
)

print(solve(lines))  # 4790390
