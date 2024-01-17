from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


def read_node(nums):
    num_childs = nums[0]
    num_meta = nums[1]

    if num_childs == 0:
        meta = nums[2 : 2 + num_meta]
        return sum(meta), 2 + num_meta
    else:
        tot_idx_next = 0
        meta = 0
        for child in range(num_childs):
            child_meta, idx_next = read_node(nums[2 + tot_idx_next :])
            tot_idx_next += idx_next
            meta += child_meta
        meta += sum(nums[2 + tot_idx_next : 2 + tot_idx_next + num_meta])
        return (
            meta,
            2 + tot_idx_next + num_meta,
        )


def read_node_value(nums):
    num_childs = nums[0]
    num_meta = nums[1]

    if num_childs == 0:
        meta = nums[2 : 2 + num_meta]
        value = sum(meta)
        return value, 2 + num_meta
    else:
        tot_idx_next = 0
        meta = {}
        for child in range(num_childs):
            child_meta, idx_next = read_node_value(nums[2 + tot_idx_next :])
            tot_idx_next += idx_next
            meta[child] = child_meta

        cur_meta = nums[2 + tot_idx_next : 2 + tot_idx_next + num_meta]
        value = sum(meta.get(idx - 1, 0) for idx in cur_meta)
        return (
            value,
            2 + tot_idx_next + num_meta,
        )


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.input = parse_ints(self.input[0])

    def solve_part_1(self):
        meta, idx_next = read_node(self.input)

        answer = meta
        print(answer)
        return answer

    def solve_part_2(self):
        value, idx_next = read_node_value(self.input)
        print(value, idx_next)
        answer = value
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
