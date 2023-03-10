from pathlib import Path
from statistics import mean, median


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.crab_pos = [int(x) for x in self.input[0].strip("\n").split(",")]

    def solve_part_1(self):
        target_pos = round(median(self.crab_pos))
        answer = sum([abs(pos - target_pos) for pos in self.crab_pos])
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 999999999999
        for target_pos in range(min(self.crab_pos), max(self.crab_pos)):

            fuel = sum(
                [
                    int(abs(pos - target_pos) * (1 + abs(pos - target_pos)) / 2)
                    for pos in self.crab_pos
                ]
            )
            answer = min(fuel, answer)
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
