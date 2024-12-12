from pathlib import Path
from string import ascii_uppercase

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = ascii_image_to_map(
            self.input, chr_map={x: x for x in ascii_uppercase}
        )

    def check_neighbours(self, pos, plant):
        for dir in deltas4_2d:
            neigh = (pos[0] + dir[0], pos[1] + dir[1])
            if (
                neigh not in self.pos_in_region
                and neigh in self.map
                and self.map[neigh] == plant
                and neigh not in self.regions[self.current_region_num]
            ):
                self.pos_in_region.add(neigh)
                self.regions[self.current_region_num].append(neigh)
                self.check_neighbours(neigh, plant)

    def solve_part_1(self):
        self.regions = {}
        self.pos_in_region = set()
        self.current_region_num = 0
        for pos, plant in self.map.items():
            if pos not in self.pos_in_region:
                self.pos_in_region.add(pos)
                self.regions[self.current_region_num] = [pos]
                self.check_neighbours(pos, plant)
                self.current_region_num += 1

        answer = 0
        for _, positions in self.regions.items():
            area = len(positions)
            perimeter = 0
            for pos in positions:
                for dir in deltas4_2d:
                    neigh = (pos[0] + dir[0], pos[1] + dir[1])
                    if neigh not in positions:
                        perimeter += 1
            answer += area * perimeter

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for _, positions in self.regions.items():
            area = len(positions)
            edges = {(0, 1): [], (1, 0): [], (0, -1): [], (-1, 0): []}
            for pos in sorted(positions):
                for dir in deltas4_2d:
                    neigh = (pos[0] + dir[0], pos[1] + dir[1])
                    if neigh not in positions:
                        if len(edges[dir]) == 0:
                            edges[dir].append([pos])
                        else:
                            part_of_fence = False
                            for fence in edges[dir]:
                                side_dir = (dir[1], dir[0])
                                anti_dir = (-side_dir[0], -side_dir[1])
                                if (
                                    pos[0] + side_dir[0],
                                    pos[1] + side_dir[1],
                                ) in fence or (
                                    pos[0] + anti_dir[0],
                                    pos[1] + anti_dir[1],
                                ) in fence:
                                    fence.append(pos)
                                    part_of_fence = True
                            if not part_of_fence:
                                # New fence
                                edges[dir].append([pos])

                num_edges = sum(len(edge) for edge in edges.values())
            answer += area * num_edges
        print(answer)

    def save_results(self):
        with open(Path(__file__).parent / "part1", "w") as opened_file:
            opened_file.write(str(self.solve_part_1()))

        with open(Path(__file__).parent / "part2", "w") as opened_file:
            opened_file.write(str(self.solve_part_2()))


if __name__ == "__main__":
    solution = Solution()
    solution.save_results()
