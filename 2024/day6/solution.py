from itertools import cycle
from pathlib import Path

from tqdm import tqdm

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = ascii_image_to_map(self.input, chr_map=AOC_CHR_MAP | {"^": 2})
        for pos, val in self.map.items():
            if val == 2:
                self.start_pos = pos
                break

        self.min_r, self.max_r, self.min_c, self.max_c = get_min_coos(self.map)

    def step(self, pos, dir, map_):
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        while map_[next_pos] == 1:
            dir = next(self.dirs)
            next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        return next_pos, dir

    def walk(self, map_):
        self.dirs = cycle([deltas4_2d[3], *deltas4_2d[:3]])
        dir = next(self.dirs)
        seen_pos = set()
        pos = self.start_pos
        seen_pos.add((pos, dir))
        while self.min_r <= pos[0] <= self.max_r and self.min_c <= pos[1] <= self.max_c:
            seen_pos.add((pos, dir))
            pos, dir = self.step(pos, dir, map_)
            if (pos, dir) in seen_pos:
                return seen_pos, True

        return seen_pos, False

    def solve_part_1(self):
        seen_pos, _ = self.walk(self.map.copy())
        self.total_pos = set(pos for pos, _ in seen_pos)
        answer = len(self.total_pos)

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for obstacle_pos in tqdm(self.total_pos):
            if obstacle_pos == self.start_pos:
                continue
            new_map = self.map.copy()
            new_map[obstacle_pos] = 1
            _, loop = self.walk(new_map)
            if loop:
                answer += 1

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
