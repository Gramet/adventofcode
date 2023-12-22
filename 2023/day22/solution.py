from copy import deepcopy
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = defaultdict(int)
        self.bricks = {idx: [] for idx in range(len(self.input))}
        for idx, line in enumerate(self.input):
            x1, y1, z1, x2, y2, z2 = parse_ints(line)
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        self.map[(x, y, z)] = idx
                        self.bricks[idx].append((x, y, z))

    def solve_part_1(self):
        new_bricks = {}
        for brick, brick_pixels in sorted(
            self.bricks.items(), key=lambda pair: min(pixel[2] for pixel in pair[1])
        ):
            can_fall = True
            cur_brick_pixels = deepcopy(brick_pixels)
            while can_fall:
                can_fall = True
                for pixel in cur_brick_pixels:
                    below_pixel = (pixel[0], pixel[1], pixel[2] - 1)
                    if below_pixel[2] < 1 or (
                        below_pixel in self.map and below_pixel not in cur_brick_pixels
                    ):
                        can_fall = False
                if can_fall:
                    cur_brick_pixels = [
                        (px[0], px[1], px[2] - 1) for px in cur_brick_pixels
                    ]
            new_bricks[brick] = cur_brick_pixels
            for px in brick_pixels:
                del self.map[px]
            for px in cur_brick_pixels:
                self.map[px] = brick
        self.bricks = new_bricks

        self.supporters = {brick: set() for brick in self.bricks}
        for brick, brick_pixels in self.bricks.items():
            for pixel in brick_pixels:
                below_pixel = (pixel[0], pixel[1], pixel[2] - 1)
                if below_pixel in self.map and below_pixel not in brick_pixels:
                    self.supporters[brick].add(self.map[below_pixel])
        safe_bricks = set(list(self.bricks.keys()))
        self.bad_bricks = set()
        for supporter in self.supporters.values():
            if len(supporter) == 1:
                self.bad_bricks |= supporter
        safe_bricks -= self.bad_bricks

        answer = len(safe_bricks)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for brick in self.bad_bricks:
            cur_bad_bricks = set([brick])
            for brick, _ in sorted(
                self.bricks.items(), key=lambda pair: min(pixel[2] for pixel in pair[1])
            ):
                if all(s in cur_bad_bricks for s in self.supporters[brick]) and len(
                    self.supporters[brick]
                ):
                    cur_bad_bricks.add(brick)
            answer += len(cur_bad_bricks) - 1

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
