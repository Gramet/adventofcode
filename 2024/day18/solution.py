from heapq import heapify
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"

SIZE = 70


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)

    def early_exit(self, pos, visited, current_best):
        return pos[0] >= current_best or (
            pos[1:] in visited and visited[pos[1:]] <= pos[0]
        )

    def get_next_states(self, pos_to_eval, visited, **kwargs):
        next_step = []
        for neigh in pos_to_eval[1].neighbours(deltas4_2d):
            if 0 <= neigh.x <= SIZE and 0 <= neigh.y <= SIZE and self.map[neigh] != 1:
                next_step.append((pos_to_eval[0] + 1, neigh))

        return next_step

    def reach_target(self, pos_to_eval, **kwargs):
        if pos_to_eval[1] == self.end_pos:
            return True
        return False

    def update_current_best(self, current_best, pos_to_eval, **kwargs):
        return min(current_best, pos_to_eval[0])

    def update_visited(self, visited, pos_to_eval):
        visited[pos_to_eval[1:]] = pos_to_eval[0]

    def find_path_with_bytes(self, n_bytes):
        self.map = defaultdict(int)
        for line in self.input[:n_bytes]:
            x, y = parse_ints(line)
            self.map[Point2D(x, y)] = 1
        start_pos = Point2D(0, 0)
        self.end_pos = Point2D(SIZE, SIZE)
        start_pos = [(0, start_pos)]
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
        return answer

    def solve_part_1(self):
        answer = self.find_path_with_bytes(1024)
        print(answer)
        return answer

    def solve_part_2(self):
        for n in range(len(self.input))[::-1]:
            answer = self.find_path_with_bytes(n)
            if answer != 1e10:
                answer = self.input[n]
                break
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
