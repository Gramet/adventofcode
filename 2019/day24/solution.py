from collections import defaultdict
from copy import deepcopy
from pathlib import Path

deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = [l.strip("\n") for l in f.readlines()]
        self.map = defaultdict(int)

        for r, row in enumerate(self.input):
            for c, char in enumerate(row):
                if char == "#":
                    self.map[(r, c)] = 1
                else:
                    self.map[(r, c)] = 0

    def solve_part_1(self):
        current_map = deepcopy(self.map)
        seen_maps = [deepcopy(current_map)]
        while True:
            next_map = defaultdict(int)
            for r in range(len(self.input)):
                for c in range(len(self.input)):
                    num_adj = 0
                    for delta in deltas:
                        new_coo = (r + delta[0], c + delta[1])
                        num_adj += current_map[new_coo]

                    if current_map[(r, c)] == 1:
                        if num_adj == 1:
                            next_map[(r, c)] = 1
                        else:
                            next_map[(r, c)] = 0
                    else:
                        if num_adj == 1 or num_adj == 2:
                            next_map[(r, c)] = 1
                        else:
                            next_map[(r, c)] = 0

            if next_map in seen_maps:
                answer = 0
                for r, row in enumerate(self.input):
                    for c, _ in enumerate(row):
                        if next_map[(r, c)] == 1:
                            answer += 2 ** (r * len(self.input) + c)
                print(answer)
                return answer
            else:
                seen_maps.append(deepcopy(next_map))
                current_map = deepcopy(next_map)

    def solve_part_2(self):
        current_map = deepcopy(self.map)
        current_map3d = defaultdict(int)
        for k, v in current_map.items():
            current_map3d[(*k, 0)] = v

        for minute in range(1, 201):
            max_level = (minute + 2) // 2
            next_map = defaultdict(int)
            for r in range(len(self.input)):
                for c in range(len(self.input)):
                    if r == 2 and c == 2:
                        continue
                    for level in range(-max_level, max_level + 1, 1):
                        num_adj = 0
                        for delta in deltas:
                            new_coo = (r + delta[0], c + delta[1])
                            if new_coo == (2, 2):
                                # Check inside
                                if delta == (0, 1):  # check right
                                    num_adj += sum(
                                        current_map3d[(i, 0, level - 1)]
                                        for i in range(len(self.input))
                                    )
                                elif delta == (1, 0):  # check down
                                    num_adj += sum(
                                        current_map3d[(0, i, level - 1)]
                                        for i in range(len(self.input))
                                    )
                                if delta == (0, -1):  # check left
                                    num_adj += sum(
                                        current_map3d[
                                            (i, len(self.input) - 1, level - 1)
                                        ]
                                        for i in range(len(self.input))
                                    )
                                elif delta == (-1, 0):  # check up
                                    num_adj += sum(
                                        current_map3d[
                                            (len(self.input) - 1, i, level - 1)
                                        ]
                                        for i in range(len(self.input))
                                    )
                            elif new_coo[0] < 0:
                                # Check up
                                num_adj += current_map3d[(1, 2, level + 1)]
                            elif new_coo[1] < 0:
                                # Check left
                                num_adj += current_map3d[(2, 1, level + 1)]
                            elif new_coo[0] >= len(self.input):
                                # Check down
                                num_adj += current_map3d[(3, 2, level + 1)]
                            elif new_coo[1] >= len(self.input):
                                # Check right
                                num_adj += current_map3d[(2, 3, level + 1)]
                            else:
                                num_adj += current_map3d[(*new_coo, level)]

                        if current_map3d[(r, c, level)] == 1:
                            if num_adj == 1:
                                next_map[(r, c, level)] = 1
                            else:
                                next_map[(r, c, level)] = 0
                        else:
                            if num_adj == 1 or num_adj == 2:
                                next_map[(r, c, level)] = 1
                            else:
                                next_map[(r, c, level)] = 0

            current_map3d = deepcopy(next_map)
            # map_str = ""
            # for level in range(-max_level, max_level + 1):
            #    map_str += f"\nDepth {-level}:\n"
            #    for r in range(len(self.input)):
            #        for c in range(len(self.input)):
            #            map_str += str(current_map3d[(r, c, level)])
            #        map_str += "\n"
            # print(map_str)
        answer = sum(current_map3d.values())
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
