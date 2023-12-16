import math
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"

maxs = {"red": 12, "green": 13, "blue": 14}


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.games = {}
        for idx, line in enumerate(self.input):
            _, draws = line.strip().split(":")
            self.games[idx + 1] = []
            for draw in draws.split(";"):
                draw_d = {}
                for cube_draw in draw.split(", "):
                    num, color = cube_draw.split()
                    draw_d[color] = int(num)
                self.games[idx + 1].append(draw_d)

    def solve_part_1(self):
        answer = 0
        for game_id, game in self.games.items():
            valid = not any(
                val > maxs[color] for draw in game for color, val in draw.items()
            )
            if valid:
                answer += game_id
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for game in self.games.values():
            min_cubes = [max([draw.get(color, 0) for draw in game]) for color in maxs]
            answer += math.prod(min_cubes)

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
