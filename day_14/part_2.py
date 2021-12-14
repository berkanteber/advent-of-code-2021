import os
from collections import Counter
from itertools import pairwise

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    template, rules = data.split("\n\n")

    rule_map = {}
    for rule in rules.splitlines():
        pair_str, char = rule.split(" -> ")
        rule_map[pair_str[0], pair_str[1]] = char

    pair_counter = Counter(pairwise(template))
    for _ in range(40):
        diff: Counter[tuple[str, str]] = Counter()
        for pair, char in rule_map.items():
            pair_count = pair_counter[pair]

            diff[pair] += pair_count

            diff[pair[0], char] -= pair_count
            diff[char, pair[1]] -= pair_count

        pair_counter.subtract(diff)

    polymer_counter = Counter({template[-1]: 1})
    for (first, _), count in pair_counter.items():
        polymer_counter[first] += count

    (_, most), *_, (_, least) = polymer_counter.most_common()

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

assert solve(example_data) == 2188189693529

print(solve(data))  # 3390034818249
