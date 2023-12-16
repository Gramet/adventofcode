from itertools import cycle
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"
from copy import deepcopy


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.chr_map = {"#": 1, ".": 0, "O": 2}
        self.map = ascii_image_to_map(self.input, chr_map=self.chr_map)
        self.map_dim = max(self.map)

    def iterate_pos_from_dir(self, dir):
        if dir == (-1, 0):
            return sorted(self.map)
        elif dir == (0, -1):
            return sorted(self.map, key=lambda x: x[1])
        elif dir == (1, 0):
            return sorted(self.map, key=lambda x: -x[0])
        elif dir == (0, 1):
            return sorted(self.map, key=lambda x: -x[1])

    def compute_load(self):
        load = 0
        for cur_pos in self.map:
            if self.map[cur_pos] == 2:
                load += self.map_dim[0] + 1 - cur_pos[0]
        return load

    def try_to_move(self, cur_pos, dir):
        if self.map[cur_pos] != 2:
            return
        dest_pos = cur_pos
        while True:
            next_pos = (dest_pos[0] + dir[0], dest_pos[1] + dir[1])
            if (
                self.map_dim[0] >= next_pos[0] >= 0
                and self.map_dim[1] >= next_pos[1] >= 0
                and self.map[next_pos] == 0
            ):
                dest_pos = next_pos
            else:
                break
        if dest_pos != cur_pos:
            self.map[dest_pos] = 2
            self.map[cur_pos] = 0

    def solve_part_1(self):
        dir = (-1, 0)
        for cur_pos in self.iterate_pos_from_dir(dir):
            self.try_to_move(cur_pos, dir)

        answer = self.compute_load()
        print(answer)
        return answer

    def solve_part_2(self):
        self.map = ascii_image_to_map(self.input, chr_map=self.chr_map)
        seen = []
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        num_cycles = 1000000000
        for move in range(num_cycles):
            for dir in dirs:
                for cur_pos in self.iterate_pos_from_dir(dir):
                    self.try_to_move(cur_pos, dir)

            state = deepcopy(self.map)
            if state in seen:
                period = move - seen.index(state)
                move_done = move + 1
                next_move = move_done + period * ((num_cycles - move_done) // period)
                move_left = num_cycles - next_move
                correct_state = seen[seen.index(state) + move_left]
                break
            seen.append(state)
        self.map = correct_state
        answer = self.compute_load()
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
