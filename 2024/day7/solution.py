from pathlib import Path

from aoc_utils import *
import itertools

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        ops = ["*", "+"]
        for line in self.input:
            ints = parse_ints(line)
            target = ints[0]
            ints = ints[1:]
            operators = itertools.product(ops, repeat=len(ints) - 1)
            for op_list in operators:
                res = ints[0]
                for op, num in zip(op_list, ints[1:]):
                    match op:
                        case "+":
                            res += num
                        case "*":
                            res *= num
                        case _:
                            raise ValueError

                if res == target:
                    answer += res
                    break
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        ops = ["*", "+", "|"]
        for line in self.input:
            ints = parse_ints(line)
            target = ints[0]
            ints = ints[1:]
            operators = itertools.product(ops, repeat=len(ints) - 1)
            for op_list in operators:
                res = ints[0]
                for op, num in zip(op_list, ints[1:]):
                    match op:
                        case "+":
                            res += num
                        case "*":
                            res *= num
                        case "|":
                            res = int(str(res) + str(num))
                        case _:
                            raise ValueError

                if res == target:
                    answer += res
                    break
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
