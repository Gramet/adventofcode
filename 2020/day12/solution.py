from copy import deepcopy
from pathlib import Path

dir_dict = {0: "E", 90: "N", 180: "W", 270: "S"}
dir_fact = {"E": 1, "N": 1, "W": -1, "S": -1}
dir_map = {"E": "E", "N": "N", "W": "E", "S": "N"}


def rotate_right(waypoint, times):
    for i in range(times):
        new_waypoint = deepcopy(waypoint)
        new_waypoint["E"] = waypoint["N"]
        new_waypoint["N"] = -waypoint["E"]
        waypoint = new_waypoint
    return waypoint


def rotate_left(waypoint, times):
    for i in range(times):
        new_waypoint = deepcopy(waypoint)
        new_waypoint["E"] = -waypoint["N"]
        new_waypoint["N"] = waypoint["E"]
        waypoint = new_waypoint
    return waypoint


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        pos = {"E": 0, "N": 0}
        dir = 0
        for line in self.input:
            cap = line[0]
            degrees = int(line[1:])
            if cap == "R":
                dir = (dir - degrees) % 360
                continue
            if cap == "L":
                dir = (dir + degrees) % 360
                continue
            if cap == "F":
                pos[dir_map[dir_dict[dir]]] = (
                    pos[dir_map[dir_dict[dir]]] + dir_fact[dir_dict[dir]] * degrees
                )
                continue
            pos[dir_map[cap]] = pos[dir_map[cap]] + dir_fact[cap] * degrees
        answer = abs(pos["E"]) + abs(pos["N"])
        print(answer)
        return answer

    def solve_part_2(self):
        pos = {"E": 0, "N": 0}
        waypoint_pos = {"E": 10, "N": 1}
        for line in self.input:
            cap = line[0]
            degrees = int(line[1:])
            if cap == "R":
                waypoint_pos = rotate_right(waypoint_pos, 4 * degrees // 360)
            elif cap == "L":
                waypoint_pos = rotate_left(waypoint_pos, 4 * degrees // 360)
            elif cap == "F":
                pos["E"] += waypoint_pos["E"] * degrees
                pos["N"] += waypoint_pos["N"] * degrees
            else:
                waypoint_pos[dir_map[cap]] = (
                    waypoint_pos[dir_map[cap]] + dir_fact[cap] * degrees
                )

        answer = abs(pos["E"]) + abs(pos["N"])
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
