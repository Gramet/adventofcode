from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        print(self.input[0])
        self.points = [parse_relints(x) for x in self.input]
        print(self.points)

    def move_points(self, display=False):
        self.points = [
            [point[0] + point[2], point[1] + point[3], point[2], point[3]]
            for point in self.points
        ]
        if display:
            map_ = defaultdict(int)
            for point in self.points:
                map_[(point[1], point[0])] = 1
            print_2d_image(map_)

    def solve_part_1(self):
        self.part2 = 0
        cur_range = 99999999
        while True:
            self.part2 += 1
            self.move_points()
            new_range = max(point[0] for point in self.points) - min(
                point[0] for point in self.points
            )
            if new_range > cur_range:
                break
            cur_range = new_range

        self.points = [
            [point[0] - point[2], point[1] - point[3], point[2], point[3]]
            for point in self.points
        ]
        self.part2 -= 1
        map_ = defaultdict(int)
        for point in self.points:
            map_[(point[1], point[0])] = 1
        print_2d_image(map_)
        answer = "NBRALZPH"
        print(answer)
        return answer

    def solve_part_2(self):
        answer = self.part2
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
