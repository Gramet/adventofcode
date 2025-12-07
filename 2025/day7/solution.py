from collections import defaultdict
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = ascii_image_to_map(self.input, {".": 0, "^": 1, "S": 2})

    def solve_part_1(self):
        start = [k for k, v in self.map.items() if v == 2][0]
        beam_pos = set([start])
        splits = set()
        for _ in range(len(self.input)):
            new_beam_pos = set()
            for point in beam_pos:
                next_pos = point + Point2D(1, 0)
                if self.map.get(next_pos, 0) == 1:
                    new_beam_pos.add(next_pos + Point2D(0, 1))
                    new_beam_pos.add(next_pos + Point2D(0, -1))
                    splits.add(next_pos)
                else:
                    new_beam_pos.add(next_pos)
            print(beam_pos)
            beam_pos = new_beam_pos

        answer = len(splits)
        print(answer)
        return answer

    def solve_part_2(self):
        start = [k for k, v in self.map.items() if v == 2][0]
        beam_pos = defaultdict(int)
        beam_pos[start] = 1
        for _ in range(len(self.input)):
            new_beam_pos = defaultdict(int)
            for point in beam_pos:
                next_pos = point + Point2D(1, 0)
                if self.map.get(next_pos, 0) == 1:
                    new_beam_pos[next_pos + Point2D(0, 1)] += beam_pos[point]
                    new_beam_pos[next_pos + Point2D(0, -1)] += beam_pos[point]
                else:
                    new_beam_pos[next_pos] += beam_pos[point]
            beam_pos = new_beam_pos

        answer = sum(beam_pos.values())
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
