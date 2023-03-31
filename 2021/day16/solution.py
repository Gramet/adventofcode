from pathlib import Path
from binascii import unhexlify
import numpy as np

hex_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def eval_packet(packet, packet_type):
    match packet_type:
        case 0:
            return sum(packet)
        case 1:
            return np.prod(packet)
        case 2:
            return min(packet)
        case 3:
            return max(packet)
        case 5:
            return int(packet[0] > packet[1])
        case 6:
            return int(packet[0] < packet[1])
        case 7:
            return int(packet[0] == packet[1])


def read_single_packet(string):
    packet = []
    tot_version = 0
    i = 0
    version = int(string[i : i + 3], 2)
    tot_version += version
    packet_type = int(string[i + 3 : i + 6], 2)
    if packet_type == 4:
        # Literal value
        i = i + 6
        val = ""
        num_bits = 0
        while True:
            next_five = string[i : i + 5]
            val += next_five[1:]
            i += 5
            num_bits += 5
            if next_five[0] == "0":
                break
        packet_val = int(val, 2)
        packet.append(packet_val)
    else:
        # Operator
        i = i + 6
        indicator = string[i]
        if indicator == "0":
            length = int(string[i + 1 : i + 16], 2)
            sum_version, subpackets = read_packet(string[i + 16 : i + 16 + length])
            i += 16 + length
            tot_version += sum_version
            packet.append(subpackets)
        else:
            num_subpackets = int(string[i + 1 : i + 12], 2)
            i += 12
            for _ in range(num_subpackets):
                sum_version, subpackets, packet_len = read_single_packet(string[i:])
                tot_version += sum_version
                packet.append(subpackets)
                i += packet_len
    return tot_version, packet, i


def read_single_packet_eval(string):
    tot_version = 0
    i = 0
    version = int(string[i : i + 3], 2)
    tot_version += version
    packet_type = int(string[i + 3 : i + 6], 2)
    if packet_type == 4:
        # Literal value
        i = i + 6
        val = ""
        num_bits = 0
        while True:
            next_five = string[i : i + 5]
            val += next_five[1:]
            i += 5
            num_bits += 5
            if next_five[0] == "0":
                break
        packet_val = int(val, 2)
        packet = packet_val
    else:
        # Operator
        i = i + 6
        indicator = string[i]
        if indicator == "0":
            length = int(string[i + 1 : i + 16], 2)
            sum_version, subpackets = read_packet_eval(string[i + 16 : i + 16 + length])
            i += 16 + length
            tot_version += sum_version
        else:
            num_subpackets = int(string[i + 1 : i + 12], 2)
            i += 12
            subpackets = []
            for _ in range(num_subpackets):
                sum_version, subpacket, packet_len = read_single_packet_eval(string[i:])
                subpackets.append(subpacket)
                tot_version += sum_version
                i += packet_len
        packet = eval_packet(subpackets, packet_type)
    return tot_version, packet, i


def read_packet(string):
    packets = []
    tot_version = 0
    i = 0
    while i < len(string):
        sum_version, packet, packet_len = read_single_packet(string[i:])
        tot_version += sum_version
        packets.append(packet)
        i += packet_len
        if all(x == "0" for x in string[i:]):
            break
    return tot_version, packets


def read_packet_eval(string):
    packets = []
    tot_version = 0
    i = 0
    while i < len(string):
        sum_version, packet, packet_len = read_single_packet_eval(string[i:])
        tot_version += sum_version
        packets.append(packet)
        i += packet_len
        if all(x == "0" for x in string[i:]):
            break
    return tot_version, packets


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()[0].strip("\n")
        self.bits = ""
        for char in self.input:
            self.bits += hex_map[char]
        print(self.bits)

    def solve_part_1(self):
        tot_version, packets = read_packet(self.bits)

        answer = tot_version

        print(packets)
        print(answer)
        return answer

    def solve_part_2(self):
        tot_version, packets = read_packet_eval(self.bits)

        answer = packets[0]

        print(answer)
        return answer

    def save_results(self):
        with open(Path(__file__).parent / "part1", "w") as opened_file:
            opened_file.write(str(self.solve_part_1()))

        with open(Path(__file__).parent / "part2", "w") as opened_file:
            opened_file.write(str(self.solve_part_2()))


if __name__ == "__main__":
    solution = Solution()
    solution.save_results()
