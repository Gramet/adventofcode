from functools import cache
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"

num_pad = {
    Point2D(0, 0): "7",
    Point2D(0, 1): "8",
    Point2D(0, 2): "9",
    Point2D(1, 0): "4",
    Point2D(1, 1): "5",
    Point2D(1, 2): "6",
    Point2D(2, 0): "1",
    Point2D(2, 1): "2",
    Point2D(2, 2): "3",
    Point2D(3, 1): "0",
    Point2D(3, 2): "A",
}
num_pad_rev = {v: k for k, v in num_pad.items()}

dir_pad = {
    Point2D(0, 1): "^",
    Point2D(0, 2): "A",
    Point2D(1, 0): "<",
    Point2D(1, 1): "v",
    Point2D(1, 2): ">",
}
dir_pad_rev = {v: k for k, v in dir_pad.items()}


def num_path(start, end):
    start_pos = num_pad_rev[start]
    end_pos = num_pad_rev[end]
    path = ""
    delta_r = end_pos.x - start_pos.x
    delta_c = end_pos.y - start_pos.y
    r_path = ""
    c_path = ""
    if delta_r > 0:
        r_path += "v" * delta_r
    else:
        r_path += "^" * abs(delta_r)
    if delta_c > 0:
        c_path += ">" * delta_c
    else:
        c_path += "<" * abs(delta_c)

    if start_pos.x == 3 and end_pos.y == 0:
        path = [r_path + c_path + "A"]
    elif start_pos.y == 0 and end_pos.x == 3:
        path = [c_path + r_path + "A"]
    else:
        path = list(set([r_path + c_path + "A", c_path + r_path + "A"]))
    return path


def dir_path(start, end):
    start_pos = dir_pad_rev[start]
    end_pos = dir_pad_rev[end]
    path = ""
    delta_r = end_pos.x - start_pos.x
    delta_c = end_pos.y - start_pos.y
    r_path = ""
    c_path = ""
    if delta_r > 0:
        r_path += "v" * delta_r
    else:
        r_path += "^" * abs(delta_r)
    if delta_c > 0:
        c_path += ">" * delta_c
    else:
        c_path += "<" * abs(delta_c)

    if start_pos.x == 0 and end_pos.y == 0 and end_pos.x == 1:
        path = [r_path + c_path + "A"]
    elif start_pos.y == 0 and start_pos.x == 1 and end_pos.x == 0:
        path = [c_path + r_path + "A"]
    else:
        path = list(set([r_path + c_path + "A", c_path + r_path + "A"]))
    return path


num_paths = {}
for start_pos, start_k in num_pad.items():
    for end_pos, end_k in num_pad.items():
        num_paths[(start_k, end_k)] = num_path(start_k, end_k)

dir_paths = {}
for start_pos, start_k in dir_pad.items():
    for end_pos, end_k in dir_pad.items():
        dir_paths[(start_k, end_k)] = dir_path(start_k, end_k)


@cache
def find_path(seq, level, num_bots):
    if level == num_bots:
        return len(seq)
    key_maps = num_paths if level == 0 else dir_paths
    res = 0
    start = "A"
    for next_chr in seq:
        presses = [
            find_path(subseq, level + 1, num_bots)
            for subseq in key_maps[(start, next_chr)]
        ]
        start = next_chr
        res += min(presses)
    return res


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def solve_part_1(self):
        answer = 0
        for line in self.input:
            line = line.strip()
            path = find_path(line, 0, 3)

            complexity = path * parse_ints(line)[0]
            answer += complexity

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for line in self.input:
            line = line.strip()
            path = find_path(line, 0, 26)

            complexity = path * parse_ints(line)[0]
            answer += complexity

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
