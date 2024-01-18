from pathlib import Path
from collections import deque

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


def play(num_marbles, num_players):
    score = {p: 0 for p in range(num_players)}
    marbles = deque([0])
    for marble in range(1, num_marbles + 1):
        if marble % 23 != 0:
            marbles.rotate(-1)
            marbles.append(marble)
        else:
            marbles.rotate(7)
            score[marble % num_players] += marble + marbles.pop()
            marbles.rotate(-1)
    return max(score.values())


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.num_players, self.num_marbles = parse_ints(self.input[0])

    def solve_part_1(self):
        answer = play(self.num_marbles, self.num_players)

        print(answer)
        return answer

    def solve_part_2(self):
        answer = play(self.num_marbles * 100, self.num_players)

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
