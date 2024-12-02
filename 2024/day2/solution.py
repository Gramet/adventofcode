from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


def is_safe(numbers) -> bool:
    if numbers != sorted(numbers) and numbers != sorted(numbers, reverse=True):
        return False
    numbers = sorted(numbers)
    if all(1 <= abs(num - numbers[i + 1]) <= 3 for i, num in enumerate(numbers[:-1])):
        return True
    return False


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        for line in self.input:
            numbers = list(map(int, line.split()))
            if is_safe(numbers):
                answer += 1

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for line in self.input:
            numbers = list(map(int, line.split()))
            for i, _ in enumerate(numbers):
                temp_numbers = numbers[:i] + numbers[i + 1 :]
                if is_safe(temp_numbers):
                    answer += 1
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
