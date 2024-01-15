from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

from aoc_utils import *
from numpy import poly

INPUT_FILE = Path(__file__).parent / "input"

ascii_delta = ord("a") - ord("A")


pairs = [low + up for low, up in zip(ascii_lowercase, ascii_uppercase)] + [
    up + low for low, up in zip(ascii_lowercase, ascii_uppercase)
]


def reduce_polymer(polymer):
    while True:
        cur = len(polymer)
        for pair in pairs:
            polymer = polymer.replace(pair, "")
        if len(polymer) == cur:
            return polymer


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)[0].strip()

    def solve_part_1(self):
        polymer = reduce_polymer(self.input)
        answer = len(polymer)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 9999999
        for letter in ascii_lowercase:
            polymer = self.input
            polymer = polymer.replace(letter, "").replace(letter.upper(), "")
            polymer = reduce_polymer(polymer)
            answer = min(answer, len(polymer))

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
