from pathlib import Path
from math import atan2, gcd, pi


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.asts = set(
            [
                (line_num, char_num)
                for line_num, line in enumerate(self.input)
                for char_num, char in enumerate(line)
                if char == "#"
            ]
        )

    def sight_line(self, ast, station):
        return (ast[0] - station[0], ast[1] - station[1])

    def is_visible(self, ast, station):
        if ast == station:
            return False

        sight_line = self.sight_line(ast, station)
        gcd_ = gcd(sight_line[0], sight_line[1])
        if gcd_ == 1:
            return True
        sight_line_norm = (sight_line[0] / gcd_, sight_line[1] / gcd_)
        for i in range(1, gcd_):
            if (
                station[0] + i * sight_line_norm[0],
                station[1] + i * sight_line_norm[1],
            ) in self.asts:
                return False
        return True

    def solve_part_1(self):
        answer = 0
        for ast in self.asts:
            visible_count = 0
            for ast2 in self.asts:
                if self.is_visible(ast2, ast):
                    visible_count += 1
            if visible_count > answer:
                answer = max(answer, visible_count)
                self.best_ast = ast
        print(answer)
        return answer

    def solve_part_2(self):
        station = self.best_ast
        self.ast_sight_ = {}
        for ast in self.asts:
            sight_line = self.sight_line(ast, station)
            angle = atan2(-sight_line[1], sight_line[0])
            if angle == pi:
                angle = -pi
            if angle not in self.ast_sight_:
                self.ast_sight_[angle] = [ast]
            else:
                self.ast_sight_[angle].append(ast)
                self.ast_sight_[angle] = sorted(
                    self.ast_sight_[angle],
                    key=lambda x: (x[0] - station[0]) ** 2 + (x[1] - station[1]) ** 2,
                )
        sorted_angles = sorted(list(self.ast_sight_.keys()))
        ast = self.ast_sight_[sorted_angles[199]]

        answer = 100 * ast[0][1] + ast[0][0]
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
