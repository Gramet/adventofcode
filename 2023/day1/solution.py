from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"

chars_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        for line in self.input:
            for chr in line:
                val = 0
                if chr.isdigit():
                    val += 10 * int(chr)
                    break
            for chr in line[::-1]:
                if chr.isdigit():
                    val += int(chr)
                    break
            answer += val

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for line in self.input:
            for idx, chr in enumerate(line):
                val = 0
                if chr.isdigit():
                    val += 10 * int(chr)
                    break
                for key, chr_val in chars_dict.items():
                    if line[idx:].startswith(key):
                        val += 10 * chr_val
                        break
                if val:
                    break
            for idx, chr in enumerate(line[::-1]):
                found = False
                if chr.isdigit():
                    found = True
                    val += int(chr)
                    break
                for key, chr_val in chars_dict.items():
                    if line[-1 - idx :].startswith(key):
                        val += chr_val
                        found = True

                        break
                if found:
                    break

            answer += val

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
