from collections import Counter
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        count_2 = 0
        count_3 = 0
        for val in self.input:
            count = Counter(val)
            if 2 in count.values():
                count_2 += 1
            if 3 in count.values():
                count_3 += 1
        answer = count_3 * count_2
        print(answer)
        return answer

    def solve_part_2(self):
        for idx, val in enumerate(self.input):
            for val2 in self.input[idx:]:
                diff = 0
                for chr1, chr2 in zip(val, val2):
                    if chr1 != chr2:
                        diff += 1
                    if diff > 1:
                        break
                if diff == 1:
                    answer = "".join(
                        [chr for chr, chr2 in zip(val, val2) if chr == chr2]
                    )
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
