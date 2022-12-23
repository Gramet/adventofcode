from collections import Counter, defaultdict
from copy import deepcopy
from pathlib import Path

deltas = [
    [(-1, 0), (-1, 1), (-1, -1)],  # N
    [(1, 0), (1, 1), (1, -1)],  # S
    [(0, -1), (-1, -1), (1, -1)],  # W
    [(0, 1), (-1, 1), (1, 1)],  # E
]

delta_elve = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


def display(elves):
    min_x = min(elves.values(), key=lambda x: x[0])[0]
    max_x = max(elves.values(), key=lambda x: x[0])[0]
    min_y = min(elves.values(), key=lambda x: x[1])[1]
    max_y = max(elves.values(), key=lambda x: x[1])[1]

    mapstr = ""
    for row in range(min_x, max_x + 1):
        for col in range(min_y, max_y + 1):
            if (row, col) in elves.values():
                mapstr += "#"
            else:
                mapstr += "."
        mapstr += "\n"
    print(mapstr)


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.map = defaultdict(int)
        self.elves = {}
        for row_idx, row in enumerate(self.input):
            for col_idx, char in enumerate(row.strip()):
                if char == "#":
                    self.map[(row_idx, col_idx)] = 1
                    self.elves[len(self.elves)] = (row_idx, col_idx)

    def solve_part_1(self):
        display(self.elves)
        elves = deepcopy(self.elves)
        map_ = deepcopy(self.map)
        delta_idx = 0
        for i in range(10):
            attempted_pos = {}
            for elve, pos in elves.items():
                if any(
                    map_[(pos[0] + delta[0], pos[1] + delta[1])] for delta in delta_elve
                ):
                    for idx in range(delta_idx, delta_idx + len(deltas)):
                        idx = idx % len(deltas)
                        if not any(
                            map_[(pos[0] + delta[0], pos[1] + delta[1])]
                            for delta in deltas[idx]
                        ):
                            attempted_pos[elve] = (
                                pos[0] + deltas[idx][0][0],
                                pos[1] + deltas[idx][0][1],
                            )
                            break
                attempted_pos[elve] = attempted_pos.get(elve, pos)
            count = Counter(attempted_pos.values())
            map_ = defaultdict(int)
            for elve, pos in elves.items():
                if count[attempted_pos[elve]] > 1:
                    attempted_pos[elve] = pos
                map_[attempted_pos[elve]] = 1

            elves = attempted_pos
            print(f"End of Round {i+1}")
            display(elves)
            delta_idx = (delta_idx + 1) % len(deltas)

        min_x = min(elves.values(), key=lambda x: x[0])[0]
        max_x = max(elves.values(), key=lambda x: x[0])[0]
        min_y = min(elves.values(), key=lambda x: x[1])[1]
        max_y = max(elves.values(), key=lambda x: x[1])[1]
        print(min_x, max_x, min_y, max_y)
        ground_tiles = (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)
        answer = ground_tiles
        print(answer)
        return answer

    def solve_part_2(self):

        elves = deepcopy(self.elves)
        map_ = deepcopy(self.map)
        delta_idx = 0
        answer = 0
        while True:
            stop_this_round = True
            answer += 1
            attempted_pos = {}
            for elve, pos in elves.items():
                if any(
                    map_[(pos[0] + delta[0], pos[1] + delta[1])] for delta in delta_elve
                ):
                    stop_this_round = False
                    for idx in range(delta_idx, delta_idx + len(deltas)):
                        idx = idx % len(deltas)
                        if not any(
                            map_[(pos[0] + delta[0], pos[1] + delta[1])]
                            for delta in deltas[idx]
                        ):
                            attempted_pos[elve] = (
                                pos[0] + deltas[idx][0][0],
                                pos[1] + deltas[idx][0][1],
                            )
                            break
                attempted_pos[elve] = attempted_pos.get(elve, pos)
            count = Counter(attempted_pos.values())
            map_ = defaultdict(int)
            for elve, pos in elves.items():
                if count[attempted_pos[elve]] > 1:
                    attempted_pos[elve] = pos
                map_[attempted_pos[elve]] = 1

            if stop_this_round:
                break
            elves = attempted_pos
            # display(elves)
            delta_idx = (delta_idx + 1) % len(deltas)

        display(elves)
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
