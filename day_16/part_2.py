import copy
import os
from dataclasses import dataclass
from functools import reduce
from operator import mul

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


@dataclass
class Literal:
    value: int
    length: int


@dataclass
class Operator:
    operator_type: str
    operand_length: (int | None) = None
    operand_count: (int | None) = None
    prefix_length: (int | None) = None

    def convert_to_literal(self, *, operands: list[Literal]) -> Literal:
        values = [operand.value for operand in operands]

        op_type = self.operator_type
        if op_type == "sum":
            value = sum(values)
        elif op_type == "mul":
            value = reduce(mul, values)
        elif op_type == "min":
            value = min(values)
        elif op_type == "max":
            value = max(values)
        elif op_type == "gt":
            value = 1 if values[0] > values[1] else 0
        elif op_type == "lt":
            value = 1 if values[0] < values[1] else 0
        elif op_type == "eq":
            value = 1 if values[0] == values[1] else 0
        else:
            raise AssertionError

        assert self.prefix_length is not None
        length = self.prefix_length + sum(operand.length for operand in operands)

        return Literal(value, length)


def solve(data: str) -> int:
    binary_str = bin(int(data, 16))[2:].rjust(len(data.strip()) * 4, "0")

    values: list[Literal | Operator] = []
    packet = binary_str
    while True:
        type_id = int(packet[3:6], 2)
        if type_id != 4:
            op_map = {0: "sum", 1: "mul", 2: "min", 3: "max", 5: "gt", 6: "lt", 7: "eq"}
            operator = Operator(op_map[type_id])

            length_type_id = int(packet[6], 2)
            if length_type_id == 0:
                operator.prefix_length = 22
                operator.operand_length = int(packet[7:22], 2)
            else:
                operator.prefix_length = 18
                operator.operand_count = int(packet[7:18], 2)

            values.append(operator)

            next_idx = {0: 22, 1: 18}[length_type_id]
            packet = packet[next_idx:]
        else:
            keep_reading_idx = 6
            while packet[keep_reading_idx] == "1":
                keep_reading_idx += 5
            end_idx = keep_reading_idx + 4

            value_bits = packet[6 : end_idx + 1]
            value_bits = "".join([ch for i, ch in enumerate(value_bits) if i % 5])

            literal = Literal(int(value_bits, 2), end_idx + 1)
            values.append(literal)

            if len(packet) - end_idx > 11:
                packet = packet[end_idx + 1 :]
            else:
                break

    while len(values) != 1:
        reduced_values: list[Literal | Operator] = []
        idx = 0
        while idx < len(values):
            literal_or_operator = values[idx]

            if isinstance(literal_or_operator, Literal):
                literal = literal_or_operator
                reduced_values.append(literal)
                idx += 1
                continue

            operator = literal_or_operator
            operands: list[Literal] = []

            if operator.operand_count:
                possible_operands = values[idx + 1 : idx + operator.operand_count + 1]
                if all(isinstance(operand, Literal) for operand in possible_operands):
                    operands = possible_operands  # type: ignore[assignment]

            elif operator.operand_length:
                possible_operands = []
                operand_length = 0
                operand_idx = idx + 1
                while operand_length < operator.operand_length:
                    if operand_idx >= len(values):
                        break

                    operand = values[operand_idx]
                    if not isinstance(operand, Literal):
                        break

                    operand_length += operand.length
                    possible_operands.append(operand)

                    operand_idx += 1

                if operand_length == operator.operand_length:
                    operands = possible_operands  # type: ignore[assignment]

            if operands:
                literal = operator.convert_to_literal(operands=operands)
                reduced_values.append(literal)
                idx += len(operands)
            else:
                reduced_values.append(operator)

            idx += 1

        values = copy.copy(reduced_values)

    remaining: Literal = values[0]  # type: ignore[assignment]
    value = remaining.value

    return value


assert solve("C200B40A82") == 3
assert solve("04005AC33890") == 54
assert solve("880086C3E88112") == 7
assert solve("CE00C43D881120") == 9
assert solve("D8005AC2A8F0") == 1
assert solve("F600BC2D8F") == 0
assert solve("9C005AC2F8F0") == 0
assert solve("9C0141080250320F1802104A08") == 1

print(solve(data))  # 660797830937
