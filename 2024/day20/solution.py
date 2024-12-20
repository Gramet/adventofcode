from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


def manhattan_dirs(size):
    dirs = []
    for x in range(-size, size + 1):
        for y in range(-size + abs(x), size + 1 - abs(x)):
            dirs.append((x, y))

    return dirs


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = ascii_image_to_map(self.input, AOC_CHR_MAP | {"S": 2, "E": 3})
        self.start_pos = [p for p, v in self.map.items() if v == 2][0]
        self.end_pos = [p for p, v in self.map.items() if v == 3][0]

    def compute_cheat_dict(self, cheat_size):
        cheat_dict = defaultdict(int)
        for pos, dist in self.dist_dict.items():
            for neigh in pos.neighbours(manhattan_dirs(cheat_size)):
                if neigh in self.dist_dict:
                    dist_gain = (
                        dist - self.dist_dict[neigh] - pos.manhattan_distance(neigh)
                    )
                    if dist_gain >= 0:
                        cheat_dict[dist_gain] += 1
        return cheat_dict

    def solve_part_1(self):
        self.dist_dict = {self.start_pos: 0}
        pos = self.start_pos
        num_steps = 1
        while pos != self.end_pos:
            for neigh in pos.neighbours(deltas4_2d):
                if neigh not in self.dist_dict and self.map[neigh] != 1:
                    self.dist_dict[neigh] = num_steps
                    pos = neigh
            num_steps += 1
        tot_steps = self.dist_dict[self.end_pos]
        self.dist_dict = {k: tot_steps - v for k, v in self.dist_dict.items()}

        cheat_size = 2
        cheat_dict = self.compute_cheat_dict(cheat_size)
        answer = sum(v for k, v in cheat_dict.items() if k >= 100)
        print(sorted(cheat_dict.items()))
        print(answer)
        return answer

    def solve_part_2(self):
        cheat_size = 20
        cheat_dict = self.compute_cheat_dict(cheat_size)
        answer = sum(v for k, v in cheat_dict.items() if k >= 100)
        print(sorted(cheat_dict.items()))
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
