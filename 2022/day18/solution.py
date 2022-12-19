from pathlib import Path
from copy import deepcopy
from tqdm import tqdm


def dist(cube1, cube2):
    return (
        abs(cube1[0] - cube2[0]) + abs(cube1[1] - cube2[1]) + abs(cube1[2] - cube2[2])
    )


deltas = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.cubes = []
        for line in self.input:
            line = line.strip().split(",")
            cube = (int(line[0]), int(line[1]), int(line[2]))
            self.cubes.append(cube)
        self.cubes = set(self.cubes)
        self.max_x = max(x[0] for x in self.cubes)
        self.max_y = max(x[1] for x in self.cubes)
        self.max_z = max(x[2] for x in self.cubes)

    def is_pocket(self, cube):
        pocket = set([cube])
        while True:
            new_pocket = deepcopy(pocket)
            for cube in pocket:
                for delta in deltas:
                    cube_del = (
                        cube[0] + delta[0],
                        cube[1] + delta[1],
                        cube[2] + delta[2],
                    )
                    if cube_del not in self.cubes:
                        new_pocket.add(cube_del)

            max_x = max(x[0] for x in new_pocket)
            max_y = max(x[1] for x in new_pocket)
            max_z = max(x[2] for x in new_pocket)
            min_x = min(x[0] for x in new_pocket)
            min_y = min(x[1] for x in new_pocket)
            min_z = min(x[2] for x in new_pocket)
            if new_pocket == pocket:
                return True
            if (
                max_x >= self.max_x
                or max_y >= self.max_y
                or max_z >= self.max_z
                or min_x <= 0
                or min_y <= 0
                or min_z <= 0
            ):
                return False
            pocket = new_pocket

    def solve_part_1(self):
        answer = 0
        for cube in tqdm(self.cubes):
            answer += 6
            for cube2 in self.cubes:
                if dist(cube, cube2) == 1:
                    answer -= 1
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for cube in tqdm(self.cubes):
            answer += 6
            for delta in deltas:
                cube_del = (cube[0] + delta[0], cube[1] + delta[1], cube[2] + delta[2])
                if cube_del in self.cubes or self.is_pocket(cube_del):
                    answer -= 1

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
