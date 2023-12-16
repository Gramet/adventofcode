from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


def get_diffs(numbers):
    return [numbers[k + 1] - num for k, num in enumerate(numbers[:-1])]


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        for line in self.input:
            numbers = list(map(int, line.split()))
            next_nums = [numbers]
            while any(next_nums[-1]):
                next_nums.append(get_diffs(next_nums[-1]))
            answer += sum(x[-1] for x in next_nums)

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for line in self.input:
            numbers = list(map(int, line.split()))
            next_nums = [numbers]
            while any(next_nums[-1]):
                next_nums.append(get_diffs(next_nums[-1]))

            next_nums.reverse()
            next_nums[0].insert(0, 0)
            for idx, nums in enumerate(next_nums[1:]):
                nums.insert(0, nums[0] - next_nums[idx][0])
            answer += next_nums[-1][0]
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
