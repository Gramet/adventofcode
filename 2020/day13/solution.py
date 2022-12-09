from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        timestamp = int(self.input[0])

        best = timestamp * 2
        best_bus = None
        for bus in self.input[1].strip().split(","):
            if bus == "x":
                continue
            if timestamp % int(bus) == 0:
                print(best, best_bus)
                break
            if int(bus) * (timestamp // int(bus)) + int(bus) < best:
                best = int(bus) * (timestamp // int(bus)) + int(bus)
                best_bus = int(bus)

        answer = (best - timestamp) * best_bus
        print(answer)
        return answer

    def solve_part_2(self):
        conds = {}
        t = 0
        prod = 1
        for i, bus in enumerate(self.input[1].strip().split(",")):
            if bus == "x":
                continue
            conds[i] = int(bus)
            while t % conds[i] != (conds[i] - i) % conds[i]:
                t += prod
            prod *= conds[i]
        answer = t
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
