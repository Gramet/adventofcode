from pathlib import Path


def compute_fuel(mass):
    return int(mass) // 3 - 2


def compute_fuel_rec(mass):
    fuel = compute_fuel(mass)
    if fuel >= 9:
        return fuel + compute_fuel_rec(fuel)
    else:
        return fuel


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        answer = sum(compute_fuel(x) for x in self.input)
        print(answer)
        return answer

    def solve_part_2(self):
        answer = sum(compute_fuel_rec(x) for x in self.input)
        print(answer)
        return answer

    def save_results(self):
        with open(Path(__file__).parent / "part1", "w") as opened_file:
            opened_file.write(str(self.solve_part_1()))

        with open(Path(__file__).parent / "part2", "w") as opened_file:
            opened_file.write(str(self.solve_part_2()))


if __name__ == "__main__":
    solution = Solution()
    solution.solve_part_1()
    solution.solve_part_2()
    solution.save_results()
