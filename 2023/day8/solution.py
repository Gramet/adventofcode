from math import lcm
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.dirs, self.maps = read_input_parts(INPUT_FILE)
        self.maps = self.maps.split("\n")[:-1]

        self.maps = [parse_words(line) for line in self.maps]
        self.maps = {start: (left, right) for (start, left, right) in self.maps}

    def solve_part_1(self):
        cur_pos = "AAA"
        steps = 0
        while cur_pos != "ZZZ":
            if self.dirs[steps % len(self.dirs)] == "L":
                cur_pos = self.maps[cur_pos][0]
            else:
                cur_pos = self.maps[cur_pos][1]
            steps += 1
        answer = steps
        print(answer)
        return answer

    def solve_part_2(self):
        cur_pos = [key for key in self.maps if key.endswith("A")]
        steps = 0
        periods = [0] * len(cur_pos)
        while not (all(pos.endswith("Z") for pos in cur_pos)):
            next_pos = []
            for pos_idx, pos in enumerate(cur_pos):
                if self.dirs[steps % len(self.dirs)] == "L":
                    pos = self.maps[pos][0]
                else:
                    pos = self.maps[pos][1]
                next_pos.append(pos)
                if pos.endswith("Z") and periods[pos_idx] == 0:
                    periods[pos_idx] = steps + 1

            cur_pos = next_pos
            steps += 1
            if all(periods):
                break
        answer = lcm(*periods)
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
