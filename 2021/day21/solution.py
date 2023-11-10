import itertools
from functools import lru_cache
from pathlib import Path

from aoc_utils import read_input

INPUT_FILE = Path(__file__).parent / "input"


@lru_cache(maxsize=None)
def play(pos1, pos2, score1, score2):
    num_wins1 = num_wins2 = 0
    for d1, d2, d3 in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        next_pos1 = (pos1 + d1 + d2 + d3) % 10
        next_score1 = score1 + next_pos1 + 1
        if next_score1 >= 21:
            num_wins1 += 1
        else:
            future_wins2, future_wins1 = play(
                pos2, next_pos1, score2, next_score1
            )  # it's P2 turn to play
            num_wins1 += future_wins1
            num_wins2 += future_wins2
    return num_wins1, num_wins2


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.p1_start = int(self.input[0].split(" ")[-1]) - 1
        self.p2_start = int(self.input[1].split(" ")[-1]) - 1

    def solve_part_1(self):
        scores = [0, 0]
        num_rolls = 0
        pos = [self.p1_start, self.p2_start]
        while True:
            player = num_rolls % 2
            num_rolls += 1
            pos[player] = (pos[player] + 3 * (num_rolls * 3 - 1)) % 10
            scores[player] += pos[player] + 1
            if any(x >= 1000 for x in scores):
                break
        answer = min(scores) * num_rolls * 3
        print(answer)
        return answer

    def solve_part_2(self):
        answer = max(play(pos1=self.p1_start, pos2=self.p2_start, score1=0, score2=0))
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
