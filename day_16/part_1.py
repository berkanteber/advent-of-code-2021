import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(input_path) as f:
    data = f.read()


def solve(data: str) -> int:
    binary_str = bin(int(data, 16))[2:].rjust(len(data.strip()) * 4, "0")

    version_totals = 0
    packet = binary_str
    while True:
        version = int(packet[0:3], 2)
        version_totals += version

        type_id = int(packet[3:6], 2)
        if type_id != 4:
            length_type_id = int(packet[6], 2)
            next_idx = {0: 22, 1: 18}[length_type_id]
            packet = packet[next_idx:]
        else:
            keep_reading_idx = 6
            while packet[keep_reading_idx] == "1":
                keep_reading_idx += 5

            end_idx = keep_reading_idx + 4

            if len(packet) - end_idx > 11:
                packet = packet[end_idx + 1 :]
            else:
                break

    return version_totals


assert solve("8A004A801A8002F478") == 16
assert solve("620080001611562C8802118E34") == 12
assert solve("C0015000016115A2E0802F182340") == 23
assert solve("A0016C880162017C3686B18A3D4780") == 31

print(solve(data))  # 947
