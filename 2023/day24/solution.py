from pathlib import Path

from aoc_utils import *
import sympy


INPUT_FILE = Path(__file__).parent / "input"


def compute_h(x, y, dx, dy):
    return y - dy / dx * x


def compute_inter(m, h, m2, h2):
    x = (h2 - h) / (m - m2)
    y = m * x + h
    return x, y


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.hail = [parse_relints(x) for x in self.input]
        print(self.hail)

    def solve_part_1(self):
        bounds = [200000000000000, 400000000000000]
        answer = 0
        for i, hail in enumerate(self.hail):
            for hail2 in self.hail[i:]:
                x, y, _, dx, dy, _ = hail
                x2, y2, _, dx2, dy2, _ = hail2
                m = dy / dx
                h = compute_h(x, y, dx, dy)
                m2 = dy2 / dx2
                if m == m2:
                    # parallel lines
                    continue
                h2 = compute_h(x2, y2, dx2, dy2)
                xi, yi = compute_inter(m, h, m2, h2)
                if (
                    bounds[0] <= xi <= bounds[1]
                    and bounds[0] <= yi <= bounds[1]
                    and (xi >= x and dx >= 0 or xi <= x and dx <= 0)
                    and (xi >= x2 and dx2 >= 0 or xi <= x2 and dx2 <= 0)
                ):
                    answer += 1

        print(answer)
        return answer

    def solve_part_2(self):
        # create symbols
        p, v, t = [sympy.symbols(f"{ch}(:3)") for ch in "pvt"]
        # for each hailstone, equation is p_i + t*dp_i = P_i +V_i*t
        equations = [
            self.hail[i][j] + t[i] * self.hail[i][j + 3] - p[j] - v[j] * t[i]
            for i in range(3)
            for j in range(3)
        ]
        print(equations)
        res = sympy.solve(equations, (*p, *v, *t))
        print(res)
        answer = sum(res[0][:3])
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
