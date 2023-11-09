from pathlib import Path
from aoc_utils import read_input_parts, deltas9_2d, print_2d_image, get_min_coos
from collections import defaultdict

INPUT_FILE = Path(__file__).parent / "input"


def enhance_pix(map_, coo, algo):
    res = ""
    for delta in sorted(deltas9_2d):
        res += str(map_[(coo[0] + delta[0], coo[1] + delta[1])])
    idx = int(res, 2)
    next_val = algo[idx]
    return int(next_val)


def get_next_default(map_, algo):
    start_coo = (1e10, 1e10)
    return lambda: int(algo[map_[start_coo]])


class Solution:
    def __init__(self):
        self.algo, self.image = read_input_parts(INPUT_FILE)
        self.algo = self.algo.replace("#", "1").replace(".", "0").strip()
        self.image = self.image.split("\n")

    def solve_part_1(self):
        self.map = defaultdict(int)
        for r, line in enumerate(self.image):
            for c, chr in enumerate(line.strip()):
                if chr == "#":
                    self.map[(r, c)] = 1
                elif chr == ".":
                    self.map[(r, c)] = 0
        self.min_r, self.max_r, self.min_c, self.max_c = get_min_coos(self.map)
        # print_2d_image(self.map)

        for _ in range(2):
            next_map = defaultdict(get_next_default(self.map, self.algo))
            for r in range(self.min_r - 1, self.max_r + 2):
                for c in range(self.min_c - 1, self.max_c + 2):
                    next_map[(r, c)] = enhance_pix(self.map, (r, c), self.algo)
            self.map = next_map
            self.min_r -= 1
            self.min_c -= 1
            self.max_r += 1
            self.max_c += 1
            # print_2d_image(self.map)
        answer = sum(self.map.values())
        print(answer)
        return answer

    def solve_part_2(self):
        for _ in range(48):
            next_map = defaultdict(get_next_default(self.map, self.algo))
            for r in range(self.min_r - 1, self.max_r + 2):
                for c in range(self.min_c - 1, self.max_c + 2):
                    next_map[(r, c)] = enhance_pix(self.map, (r, c), self.algo)
            self.map = next_map
            self.min_r -= 1
            self.min_c -= 1
            self.max_r += 1
            self.max_c += 1
            # print_2d_image(self.map)
        answer = sum(self.map.values())
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
