from heapq import heapify
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = ascii_image_to_map(self.input, AOC_CHR_MAP | {"S": 2, "E": 3})
        self.end_pos = [x for x, val in self.map.items() if val == 3][0]

    def early_exit(self, pos, visited, current_best):
        return pos[0] >= current_best or (
            pos[1:] in visited and visited[pos[1:]] <= pos[0]
        )

    def early_exit_p2(self, pos, visited, current_best):
        return pos[0] > current_best or (
            pos[1:-1] in visited and visited[pos[1:-1]] < pos[0]
        )

    def get_next_states(self, pos_to_eval, visited, **kwargs):
        next_step = []
        if self.map[pos_to_eval[1] + pos_to_eval[2]] != 1:
            next_step = [
                (pos_to_eval[0] + 1, pos_to_eval[1] + pos_to_eval[2], pos_to_eval[2])
            ]
        rots = []
        if (
            self.map[pos_to_eval[1] + (pos_to_eval[2][1], pos_to_eval[2][0])] == 0
            or self.map[pos_to_eval[1] - (pos_to_eval[2][1], pos_to_eval[2][0])] == 0
        ):
            rots = [
                (
                    pos_to_eval[0] + 1000,
                    pos_to_eval[1],
                    (pos_to_eval[2][1], pos_to_eval[2][0]),
                ),
                (
                    pos_to_eval[0] + 1000,
                    pos_to_eval[1],
                    (-pos_to_eval[2][1], -pos_to_eval[2][0]),
                ),
            ]
        return next_step + rots

    def get_next_states_p2(self, pos_to_eval, visited, **kwargs):
        next_step = []
        if self.map[pos_to_eval[1] + pos_to_eval[2]] != 1:
            next_step = [
                (
                    pos_to_eval[0] + 1,
                    pos_to_eval[1] + pos_to_eval[2],
                    pos_to_eval[2],
                    pos_to_eval[3] + (pos_to_eval[1] + pos_to_eval[2],),
                )
            ]
        rots = []
        if (
            self.map[pos_to_eval[1] + (pos_to_eval[2][1], pos_to_eval[2][0])] == 0
            or self.map[pos_to_eval[1] - (pos_to_eval[2][1], pos_to_eval[2][0])] == 0
        ):
            rots = [
                (
                    pos_to_eval[0] + 1000,
                    pos_to_eval[1],
                    (pos_to_eval[2][1], pos_to_eval[2][0]),
                    pos_to_eval[3],
                ),
                (
                    pos_to_eval[0] + 1000,
                    pos_to_eval[1],
                    (-pos_to_eval[2][1], -pos_to_eval[2][0]),
                    pos_to_eval[3],
                ),
            ]
        return next_step + rots

    def reach_target(self, pos_to_eval, **kwargs):
        if pos_to_eval[1] == self.end_pos:
            return True
        return False

    def reach_target_p2(self, pos_to_eval, **kwargs):
        if pos_to_eval[1] == self.end_pos:
            self.reach_tiles.update(pos_to_eval[3])
            return True
        return False

    def update_visited(self, visited, pos_to_eval):
        visited[pos_to_eval[1:]] = pos_to_eval[0]

    def update_visited_p2(self, visited, pos_to_eval):
        visited[pos_to_eval[1:-1]] = pos_to_eval[0]

    def update_current_best(self, current_best, pos_to_eval, **kwargs):
        return min(current_best, pos_to_eval[0])

    def solve_part_1(self):
        start_pos = [(0, p, (0, 1)) for p, val in self.map.items() if val == 2]
        heapify(start_pos)

        answer = shortest_path_heap(
            starting_positions=start_pos,
            visited={},
            early_exit=self.early_exit,
            get_next_states=self.get_next_states,
            reach_target=self.reach_target,
            update_visited=self.update_visited,
            update_current_best=self.update_current_best,
            current_best=1e10,
        )
        print(answer)
        return answer

    def solve_part_2(self):
        start_pos = [(0, p, (0, 1), (p,)) for p, val in self.map.items() if val == 2]
        heapify(start_pos)
        self.reach_tiles = set()
        _ = shortest_path_heap(
            starting_positions=start_pos,
            visited={},
            early_exit=self.early_exit_p2,
            get_next_states=self.get_next_states_p2,
            reach_target=self.reach_target_p2,
            update_visited=self.update_visited_p2,
            update_current_best=self.update_current_best,
            current_best=1e10,
        )
        answer = len(self.reach_tiles)
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
