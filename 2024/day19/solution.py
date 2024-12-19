from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.patterns, self.designs = read_input_parts(INPUT_FILE)
        self.patterns = self.patterns.strip("\n").split(", ")

    def solve_part_1(self):
        answer = 0
        for design in self.designs.splitlines():
            cur_design = set()
            cur_design.add(design)
            found = False
            while cur_design and not found:
                new_designs = set()
                for design in cur_design:
                    for pat in self.patterns:
                        if design == pat:
                            answer += 1
                            found = True
                            break
                        elif design.startswith(pat):
                            new_designs.add(design[len(pat) :])
                    if found:
                        break
                cur_design = new_designs

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for design in self.designs.splitlines():
            cur_design = dict()
            cur_design[design] = 1
            found = False
            while cur_design and not found:
                new_designs = defaultdict(int)
                for design, num in cur_design.items():
                    for pat in self.patterns:
                        if design == pat:
                            answer += num
                        elif design.startswith(pat):
                            new_designs[design[len(pat) :]] += num
                cur_design = new_designs

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
