from pathlib import Path

from aoc_utils import *
from contextlib import redirect_stdout

INPUT_FILE = Path(__file__).parent / "input"

MAX_X = 101
MAX_Y = 103


def display_robots(robots):
    map = defaultdict(int)
    for robot, _ in robots:
        map[robot] = 1
    print_2d_image(map)


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.robots = []
        for line in self.input:
            p_x, p_y, v_x, v_y = parse_relints(line)
            self.robots.append((Point2D(p_x, p_y), Point2D(v_x, v_y)))

    def safety_score(self):
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        for robot, _ in self.robots:
            if robot.x < (MAX_X - 1) / 2 and robot.y < (MAX_Y - 1) / 2:
                q1 += 1
            elif robot.x > (MAX_X - 1) / 2 and robot.y < (MAX_Y - 1) / 2:
                q2 += 1
            elif robot.x < (MAX_X - 1) / 2 and robot.y > (MAX_Y - 1) / 2:
                q3 += 1
            elif robot.x > (MAX_X - 1) / 2 and robot.y > (MAX_Y - 1) / 2:
                q4 += 1
        return q1 * q2 * q3 * q4

    def solve_part_1(self):
        for _ in range(100):
            new_robots = []
            for robot, speed in self.robots:
                robot += speed
                new_robot = Point2D(robot.x % MAX_X, robot.y % MAX_Y)
                new_robots.append((new_robot, speed))
            self.robots = new_robots
        answer = self.safety_score()
        print(answer)
        return answer

    def solve_part_2(self):
        self.robots = []
        for line in self.input:
            p_x, p_y, v_x, v_y = parse_relints(line)
            self.robots.append((Point2D(p_x, p_y), Point2D(v_x, v_y)))

        for s in range(10000):
            new_robots = []
            for robot, speed in self.robots:
                robot += speed
                new_robot = Point2D(robot.x % MAX_X, robot.y % MAX_Y)
                new_robots.append((new_robot, speed))
            self.robots = new_robots
            if self.safety_score() < 45_000_000:
                print(f"After {s+1} seconds {self.safety_score()=}: ")
                display_robots(self.robots)
                answer = s + 1
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
