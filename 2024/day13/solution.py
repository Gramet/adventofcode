from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"

A_COST = 3
B_COST = 1


def compute_cost(num_a, num_b):
    return A_COST * num_a + B_COST * num_b


class Solution:
    def __init__(self):
        self.input = read_input_parts(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        for machine in self.input:
            x_a, y_a = parse_ints(machine.splitlines()[0])
            x_b, y_b = parse_ints(machine.splitlines()[1])
            x_p, y_p = parse_ints(machine.splitlines()[2])
            num_b = (y_p * x_a - y_a * x_p) / (x_a * y_b - x_b * y_a)
            num_a = (x_p - num_b * x_b) / x_a
            if num_a.is_integer() and num_b.is_integer():
                cost = compute_cost(num_a, num_b)
                answer += int(cost)

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        delta = 10000000000000
        for machine in self.input:
            x_a, y_a = parse_ints(machine.splitlines()[0])
            x_b, y_b = parse_ints(machine.splitlines()[1])
            x_p, y_p = parse_ints(machine.splitlines()[2])
            x_p += delta
            y_p += delta

            num_b = (y_p * x_a - y_a * x_p) / (x_a * y_b - x_b * y_a)
            num_a = (x_p - num_b * x_b) / x_a
            if num_a.is_integer() and num_b.is_integer():
                cost = compute_cost(round(num_a), round(num_b))
                answer += int(cost)

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
