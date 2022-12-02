from pathlib import Path

RIGHT = "R"
LEFT = "L"
DOWN = "D"
UP = "U"


def get_wire_angles(wire_str):
    dirs = wire_str.split(",")
    angles = [(0, 0)]
    for dir in dirs:
        step = int(dir[1:])
        if dir[0] == RIGHT:
            angles.append((angles[-1][0] + step, angles[-1][1]))
        elif dir[0] == LEFT:
            angles.append((angles[-1][0] - step, angles[-1][1]))
        elif dir[0] == UP:
            angles.append((angles[-1][0], angles[-1][1] + step))
        elif dir[0] == DOWN:
            angles.append((angles[-1][0], angles[-1][1] - step))
    return angles


def crossing_point(point_1_s, point_1_e, point_2_s, point_2_e):
    if point_1_s[0] - point_1_e[0] != 0 and point_2_s[1] - point_2_e[1] != 0:
        # horizontal segment_1 and vertical segment 2
        if (
            point_1_s[0] <= point_2_s[0] <= point_1_e[0]
            or point_1_s[0] >= point_2_s[0] >= point_1_e[0]
        ):
            if (
                point_2_s[1] <= point_1_s[1] <= point_2_e[1]
                or point_2_s[1] >= point_1_s[1] >= point_2_e[1]
            ):
                return (point_2_s[0], point_1_s[1])
    elif point_1_s[1] - point_1_e[1] != 0 and point_2_s[0] - point_2_e[0] != 0:
        return crossing_point(point_2_s, point_2_e, point_1_s, point_1_e)
    else:
        return None


def get_crossing_points(angles_1, angles_2):
    intersects = []
    for point_1_s, point_1_e in zip(angles_1[:-1], angles_1[1:]):
        for point_2_s, point_2_e in zip(angles_2[:-1], angles_2[1:]):
            cross = crossing_point(point_1_s, point_1_e, point_2_s, point_2_e)
            if cross is not None:
                intersects.append(cross)

    return intersects


def steps_to_intersect(angles, inter):
    steps = 0
    for start, end in zip(angles[:-1], angles[1:]):
        if start[0] - end[0] != 0:
            # horizontal segment
            if inter[1] == start[1] and (
                start[0] <= inter[0] <= end[0] or start[0] >= inter[0] >= end[0]
            ):
                steps += abs(start[0] - inter[0])
                return steps
        else:
            # vertical segment
            if inter[0] == start[0] and (
                start[1] <= inter[1] <= end[1] or start[1] >= inter[1] >= end[1]
            ):
                steps += abs(start[1] - inter[1])
                return steps
        steps += abs(start[0] - end[0]) + abs(start[1] - end[1])


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
            self.angles_1 = get_wire_angles(self.input[0])
            self.angles_2 = get_wire_angles(self.input[1])

    def solve_part_1(self):
        self.intersects = get_crossing_points(self.angles_1, self.angles_2)
        manhattan_dists = [abs(p[0]) + abs(p[1]) for p in self.intersects]

        answer = min(manhattan_dists)
        print(answer)
        return answer

    def solve_part_2(self):
        dists = [
            steps_to_intersect(self.angles_1, inter)
            + steps_to_intersect(self.angles_2, inter)
            for inter in self.intersects
        ]
        answer = min(dists)
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
