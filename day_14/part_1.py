import os
from collections import Counter
from collections import defaultdict
from itertools import pairwise

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    template, rules = data.split("\n\n")

    rule_map = defaultdict(lambda: "")
    for rule in rules.splitlines():
        pair, char = rule.split(" -> ")
        rule_map[pair] = char

    polymer = template
    for _ in range(10):
        polymer_lst = []
        for first, second in pairwise(polymer):
            polymer_lst.append(first)
            if char := rule_map[first + second]:
                polymer_lst.append(char)
        polymer = "".join(polymer_lst) + polymer[-1]

    (_, most), *_, (_, least) = Counter(polymer).most_common()

    return most - least


example_data = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

assert solve(example_data) == 1588

print(solve(data))  # 2937
