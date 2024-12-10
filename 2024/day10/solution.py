from functools import lru_cache
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = ascii_image_to_map(
            self.input, chr_map={str(x): x for x in range(10)} | {".": -1}
        )
        self.starting_points = [k for k, v in self.map.items() if v == 0]

    @lru_cache
    def compute_score(self, cur_pos):
        pos, height = cur_pos
        if height == 9:
            return 1
        else:
            score = 0
            for dir in deltas4_2d:
                next_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if next_pos in self.map and self.map[next_pos] == height + 1:
                    score += self.compute_score((next_pos, height + 1))
            return score

    def compute_score_single_path(self, cur_pos, start_pos):
        pos, height = cur_pos
        if height == 9:
            if cur_pos not in self.reached_from[start_pos[0]]:
                self.reached_from[start_pos[0]].append(cur_pos)
                return 1
            return 0
        else:
            score = 0
            for dir in deltas4_2d:
                next_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if next_pos in self.map and self.map[next_pos] == height + 1:
                    score += self.compute_score_single_path(
                        (next_pos, height + 1), start_pos
                    )

            return score

    def solve_part_1(self):
        answer = 0
        self.reached_from = {}
        for start in self.starting_points:
            self.reached_from[start] = []
            score = self.compute_score_single_path((start, 0), (start, 0))
            answer += score

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for start in self.starting_points:
            score = self.compute_score((start, 0))
            answer += score

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
