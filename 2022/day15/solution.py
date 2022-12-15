from pathlib import Path
import re
from tqdm import tqdm
from collections import defaultdict
import numpy as np


def manhattan(a, b):
    return int(abs(a[0] - b[0]) + abs(a[1] - b[1]))


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.map = defaultdict(int)
        self.dists = {}
        self.sensors = []
        for line in tqdm(self.input):
            matches = re.search(r".+(=-?\d+).+(=-?\d+).+(=-?\d+).+(=-?\d+)", line)
            sensor = (int(matches.group(1)[1:]), int(matches.group(2)[1:]))
            beacon = (int(matches.group(3)[1:]), int(matches.group(4)[1:]))
            self.map[beacon] = 1
            self.map[sensor] = 2
            dist = manhattan(beacon, sensor)
            self.sensors.append(sensor)
            self.dists[sensor] = dist

    def blacklist(self, coos):

        if not self.map[coos]:
            self.map[coos] = -1

    def solve_part_1(self):
        min_x = min(x[0] for x in self.map if self.map[x] == 1) - max(
            self.dists.values()
        )
        max_x = max(x[0] for x in self.map if self.map[x] == 1) + max(
            self.dists.values()
        )
        answer = 0
        for x in tqdm(range(min_x, max_x + 1)):
            for sensor in self.sensors:
                if (x, 2000000) in self.map:
                    continue
                if manhattan((x, 2000000), sensor) <= self.dists[sensor]:
                    answer += 1
                    break

        print(answer)
        return answer

    def solve_part_2(self):
        max_ = 4000000
        for sensor in tqdm(self.sensors):
            dist = self.dists[sensor]
            for i in range(dist + 1):
                j = dist - i
                boundary_points = [
                    (sensor[0] + i + 1, sensor[1] + j),
                    (sensor[0] + i + 1, sensor[1] - j),
                    (sensor[0] - i - 1, sensor[1] + j),
                    (sensor[0] - i - 1, sensor[1] - j),
                ]
                for point in boundary_points:
                    if not (0 <= point[0] <= max_ and 0 <= point[1] <= max_):
                        continue
                    if all(
                        [
                            manhattan(point, sens) > self.dists[sens]
                            for sens in self.sensors
                        ]
                    ):
                        answer = point[0] * 4000000 + point[1]
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
