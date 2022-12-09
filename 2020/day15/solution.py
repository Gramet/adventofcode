from pathlib import Path
from collections import defaultdict


def count_nums(starts, end):
    d = defaultdict(lambda: t)
    lastnum = -1
    for t, num in enumerate(starts):
        d[lastnum], lastnum = t, int(num)
    for t in range(len(starts), end):
        d[lastnum], lastnum = t, t - d[lastnum]
    return lastnum


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.starts = [int(x) for x in self.input[0].split(",")]

    def solve_part_1(self):
        answer = count_nums(self.starts, 2020)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = count_nums(self.starts, 30000000)
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
