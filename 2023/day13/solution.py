from pathlib import Path

import numpy as np

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


def summarize(img) -> int:
    ret = 0
    for r in range(1, img.shape[0]):
        up = img[:r]
        down = img[r:]
        comp = np.flipud(up)
        if up.shape[0] <= down.shape[0]:
            if np.all(comp == down[:r]):
                ret += 100 * r
        else:
            if np.all(comp[: down.shape[0]] == down):
                ret += 100 * r

    for c in range(1, img.shape[1]):
        left = img[:, :c]
        right = img[:, c:]
        comp = np.fliplr(left)
        if left.shape[1] <= right.shape[1]:
            if np.all(comp == right[:, :c]):
                ret += c
        else:
            if np.all(comp[:, : right.shape[1]] == right):
                ret += c

    return ret


def fix_image(img) -> np.ndarray:
    for r in range(1, img.shape[0]):
        up = img[:r]
        down = img[r:]
        comp = np.flipud(up)
        if up.shape[0] <= down.shape[0]:
            diff = np.sum(comp != down[:r])
            if diff == 1:
                return 100 * r

        else:
            diff = np.sum(comp[: down.shape[0]] != down)
            if diff == 1:
                return 100 * r

    for c in range(1, img.shape[1]):
        left = img[:, :c]
        right = img[:, c:]
        comp = np.fliplr(left)
        if left.shape[1] <= right.shape[1]:
            diff = np.sum(comp != right[:, :c])
            if diff == 1:
                return c

        else:
            diff = np.sum(comp[:, : right.shape[1]] != right)
            if diff == 1:
                return c

    raise ValueError()


class Solution:
    def __init__(self):
        self.input = read_input_parts(INPUT_FILE)
        self.images = [ascii_image_to_numpy(img.split("\n")) for img in self.input]

    def solve_part_1(self):
        answer = 0
        for img in self.images:
            answer += summarize(img)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = sum([fix_image(img) for img in self.images])
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
