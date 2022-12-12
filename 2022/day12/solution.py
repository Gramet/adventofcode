from pathlib import Path
from string import ascii_lowercase

import numpy as np

elev_dict = {l: i for i, l in enumerate(ascii_lowercase)}
elev_dict["E"] = 26
elev_dict["S"] = -1

deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.input = [[elev_dict[char] for char in line.strip()] for line in self.input]
        self.mat = np.array(self.input)

    def get_reachable_neigh(self, pos):
        alt = self.mat[pos]
        reachable = set()
        for delta in deltas:
            try:
                coo_x = pos[0] + delta[0]
                coo_y = pos[1] + delta[1]
                if (
                    alt >= self.mat[pos[0] + delta[0], pos[1] + delta[1]] - 1
                    and 0 <= coo_x
                    and 0 <= coo_y
                ):
                    reachable.add((pos[0] + delta[0], pos[1] + delta[1]))
            except IndexError:
                pass
        return reachable

    def get_to_end(self, start_pos, end_pos):
        steps = 0
        reached = set([start_pos])
        newly_added = set([start_pos])
        while end_pos not in reached:
            steps += 1
            future_pos = set()
            for pos in newly_added:
                future_pos = future_pos.union(self.get_reachable_neigh(pos))
            newly_added = future_pos.difference(reached)
            reached = reached.union(newly_added)
            if len(newly_added) == 0:
                return np.inf
        return steps

    def solve_part_1(self):
        start_pos = np.where(self.mat == -1)
        start_pos = (start_pos[0][0], start_pos[1][0])
        self.end_pos = np.where(self.mat == 26)
        self.end_pos = (self.end_pos[0][0], self.end_pos[1][0])
        # Need to set the correct start and end altitude
        self.mat[start_pos] = 0
        self.mat[self.end_pos] = 25
        steps = self.get_to_end(start_pos, self.end_pos)
        print(f"reached in {steps} steps")
        answer = steps
        print(answer)
        return answer

    def solve_part_2(self):
        coos_x, coos_y = np.where(self.mat == 0)
        min_steps = self.mat.shape[0] * self.mat.shape[1]
        for coo_x, coo_y in zip(coos_x, coos_y):
            pos = (coo_x, coo_y)
            steps = self.get_to_end(pos, self.end_pos)
            min_steps = min(steps, min_steps)

        answer = min_steps
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
