from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"
from heapq import heapify



class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        AOC_CHR_MAP.update({">": 2, "^": 3, "<": 4, "v": 5})
        self.map = ascii_image_to_map(self.input)
        self.start_pos = (0,1)
        self.end_pos = max(self.map, key=lambda x: x if self.map[x] == 0 else (0, 0))
        self.crossings = [pos for pos in self.map if self.map[pos] == 0 and sum(
                    self.map.get((pos[0] + d[0], pos[1] + d[1]), 0) != 1
                    for d in deltas4_2d
                )!=2
                ]
        self.crossings += [self.start_pos, self.end_pos]
        self.graph = {pos: self.walk_from(pos) for pos in self.crossings}

    def find_next_pos(self, pos, cur_dir):
        next_pos = (pos[0] + cur_dir[0], pos[1] + cur_dir[1])
        if next_pos in self.map and self.map[next_pos] !=1:
            return next_pos, cur_dir
        else:
            for delta in deltas4_2d:
                if delta == cur_dir or delta == (-cur_dir[0], -cur_dir[1]):
                    continue
                next_pos = (pos[0] + delta[0], pos[1] + delta[1])
                if next_pos in self.map and self.map[next_pos] !=1:
                    return next_pos, delta
        return None, None

    def walk_from(self, pos):
        res = {}
        for delta in deltas4_2d:
            next_pos = (pos[0] + delta[0], pos[1] + delta[1])
            if next_pos in self.map and self.map[next_pos] != 1:
                step = 1
                cur_dir = delta
                while (next_pos not in self.crossings):
                    next_pos, cur_dir = self.find_next_pos(next_pos, cur_dir)
                    step += 1
                if next_pos is not None:
                    res[delta] = (next_pos, step)
        return res

    def create_next_state_p2(self, score, pos, path, delta):
        next_dest = self.graph[pos].get(delta, None)
        if next_dest is not None:
            next_pos, step = next_dest
            if next_pos not in path:
                next_path = path + (next_pos,)
                next_score = score + step
                return (next_score, next_pos,next_path)

        return None

    def create_next_state(self, score, pos, path, delta):
        next_pos = (pos[0] + delta[0], pos[1] + delta[1])
        if next_pos not in path and next_pos in self.map and self.map[next_pos] != 1:
            next_score = score + 1
            next_path = path + (next_pos,)
            next_state = (next_score, next_pos, next_path)
            return next_state
        return None

    def early_exit(self, pos_to_eval, visited, current_best, **kwargs):
        return False

    def get_next_states(self, pos_to_eval, visited, **kwargs):
        next_states = []
        for delta in deltas4_2d:
            score, pos, path = pos_to_eval
            if (
                self.map[pos] == 0
                or self.map[pos] == 2
                and delta == (0, 1)
                or self.map[pos] == 3
                and delta == (-1, 0)
                or self.map[pos] == 4
                and delta == (0, -1)
                or self.map[pos] == 5
                and delta == (1, 0)
            ):
                next_state = self.create_next_state(score, pos, path, delta)
                if next_state is not None:
                    next_states.append(next_state)
        return next_states

    def get_next_states_p2(self, pos_to_eval, visited, **kwargs):
        next_states = []
        for delta in deltas4_2d:
            score, pos, path = pos_to_eval
            next_state = self.create_next_state_p2(score, pos, path, delta)
            if next_state is not None:
                next_states.append(next_state)
        return next_states

    def reach_target(self, pos_to_eval, **kwargs):
        if pos_to_eval[1] == self.end_pos:
            return True
        return False

    def update_visited(self, visited, pos_to_eval):
        pass

    def update_current_best(self, current_best, pos_to_eval, **kwargs):
        return max(current_best, pos_to_eval[0])

    def solve_part_1(self):
        start_pos = [(0, (0, 1), ((0, 1),))]
        heapify(start_pos)
        answer = shortest_path_heap(
            starting_positions=start_pos,
            visited={},
            early_exit=self.early_exit,
            get_next_states=self.get_next_states,
            reach_target=self.reach_target,
            update_visited=self.update_visited,
            update_current_best=self.update_current_best,
            current_best=0,
        )
        print(answer)
        return answer

    def solve_part_2(self):
        start_pos = [(0, (0, 1), ((0, 1),))]
        heapify(start_pos)
        answer = shortest_path_heap(
            starting_positions=start_pos,
            visited={},
            early_exit=self.early_exit,
            get_next_states=self.get_next_states_p2,
            reach_target=self.reach_target,
            update_visited=self.update_visited,
            update_current_best=self.update_current_best,
            current_best=0,
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
