from pathlib import Path
import heapq
from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


def early_exit(pos, visited, current_best, **kwargs):
    if pos[0] >= current_best or pos[0] >= visited.get(pos[1:], 1e100):
        return True


def get_next_states(pos_to_eval, visited, map_, **kwargs):
    next_pos = [
        ((pos_to_eval[1][0] + dir[0], pos_to_eval[1][1] + dir[1]), dir)
        for dir in deltas4_2d
        if not pos_to_eval[2].count(dir) == 3
        and dir != (-pos_to_eval[2][0][0], -pos_to_eval[2][0][1])
    ]
    next_pos = [pos for pos in next_pos if pos[0] in map_]
    next_states = [
        (
            pos_to_eval[0] + map_[adj_pos[0]],
            adj_pos[0],
            (adj_pos[1],) + pos_to_eval[2][:2],
        )
        for adj_pos in next_pos
    ]
    next_states = [
        state for state in next_states if visited.get(state[1:], 1e100) >= state[0]
    ]
    return next_states


def get_next_states_part2(pos_to_eval, visited, map_, **kwargs):
    last_dir = pos_to_eval[2][0]
    if not all(dir == last_dir for dir in pos_to_eval[2][:4]):
        next_pos = [
            (
                (pos_to_eval[1][0] + last_dir[0], pos_to_eval[1][1] + last_dir[1]),
                last_dir,
            )
        ]
    else:
        next_pos = [
            ((pos_to_eval[1][0] + dir[0], pos_to_eval[1][1] + dir[1]), dir)
            for dir in deltas4_2d
            if not pos_to_eval[2].count(dir) == 10
            and dir != (-pos_to_eval[2][0][0], -pos_to_eval[2][0][1])
        ]
    next_pos = [pos for pos in next_pos if pos[0] in map_]
    next_states = [
        (
            pos_to_eval[0] + map_[adj_pos[0]],
            adj_pos[0],
            (adj_pos[1],) + pos_to_eval[2][:9],
        )
        for adj_pos in next_pos
    ]
    next_states = [
        state for state in next_states if visited.get(state[1:], 1e100) >= state[0]
    ]
    return next_states


def update_current_best(current_best, pos, **kwargs):
    print(f"found solution with cost {pos[0]}")
    return min(current_best, pos[0])


def update_visited(visited, pos, **kwargs):
    visited[pos[1:]] = pos[0]


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.chr_map = {str(x): x for x in range(10)}
        self.map = ascii_image_to_map(self.input, self.chr_map)
        self.map_dim = max(self.map)
        print(self.map)

    def reach_target(self, pos, **kwargs):
        return pos[1] == self.map_dim

    def reach_target_part2(self, pos, **kwargs):
        last_dir = pos[2][0]

        return pos[1] == self.map_dim and all(dir == last_dir for dir in pos[2][:4])

    def solve_part_1(self):
        start_pos = [(0, (0, 0), ((0, 0),))]
        heapq.heapify(start_pos)
        answer = shortest_path_heap(
            start_pos,
            {},
            early_exit,
            get_next_states,
            self.reach_target,
            update_visited,
            update_current_best,
            map_=self.map,
        )
        print(answer)
        return answer

    def solve_part_2(self):
        start_pos = [(0, (0, 0), ((0, 0),))]
        heapq.heapify(start_pos)
        answer = shortest_path_heap(
            start_pos,
            {},
            early_exit,
            get_next_states_part2,
            self.reach_target_part2,
            update_visited,
            update_current_best,
            map_=self.map,
        )
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
