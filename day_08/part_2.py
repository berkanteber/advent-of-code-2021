import os
from itertools import permutations

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    possible_mappings = [
        dict(zip("abcdefg", permutation)) for permutation in permutations("ABCDEFG")
    ]

    output_total = 0
    for line in data.splitlines():
        signal_patterns_str, output_values_str = line.split(" | ")
        signal_patterns = signal_patterns_str.split()
        output_values = output_values_str.split()

        correct_signal_patterns = {
            "abcefg": 0,
            "cf": 1,
            "acdeg": 2,
            "acdfg": 3,
            "bcdf": 4,
            "abdfg": 5,
            "abdefg": 6,
            "acf": 7,
            "abcdefg": 8,
            "abcdfg": 9,
        }
        correct_signal_patterns_set = set(correct_signal_patterns.keys())

        for mapping in possible_mappings:
            replaced_signal_patterns_set = set()
            for signal_pattern in signal_patterns:
                for char in "abcdefg":
                    signal_pattern = signal_pattern.replace(char, mapping[char])
                signal_pattern = "".join(sorted(signal_pattern.lower()))
                replaced_signal_patterns_set.add(signal_pattern)

            if replaced_signal_patterns_set == correct_signal_patterns_set:
                break

        for i, output_value in enumerate(output_values):
            for char in "abcdefg":
                output_value = output_value.replace(char, mapping[char])
            output_value = "".join(sorted(output_value.lower()))

            output_total += correct_signal_patterns[output_value] * (10 ** (3 - i))

    return output_total


example_data = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

assert solve(example_data) == 61229

print(solve(data))  # 1046281
