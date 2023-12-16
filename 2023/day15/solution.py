from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


def hash(chr, val):
    chr_val = ord(chr)
    val = ((val + chr_val) * 17) % 256
    return val


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)[0].strip().split(",")

    def solve_part_1(self):
        answer = 0
        for inp in self.input:
            val = 0
            for chr in inp:
                val = hash(chr, val)
            answer += val

        print(answer)
        return answer

    def solve_part_2(self):
        boxes = {}
        for inp in self.input:
            box = 0
            for chr in inp:
                if chr == "-" or chr == "=":
                    break
                box = hash(chr, box)
            if box not in boxes:
                boxes[box] = []
            if "-" in inp:
                boxes[box] = [b for b in boxes[box] if not b[0] == inp.strip("-")]
            elif "=" in inp:
                lens = (inp.split("=")[0], int(inp.split("=")[1]))
                if any(b[0] == inp.split("=")[0] for b in boxes[box]):
                    boxes[box] = [
                        b if not b[0] == inp.split("=")[0] else lens for b in boxes[box]
                    ]
                else:
                    boxes[box].append(lens)
        answer = 0
        for box_num, box in boxes.items():
            for slot, lens in enumerate(box):
                answer += (box_num + 1) * (slot + 1) * lens[1]

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
