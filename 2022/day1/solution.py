from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        buff = []
        self.foods = []
        for line in self.input:
            if line != "\n":
                buff.append(int(line))
            else:
                self.foods.append(sum(buff))
                buff = []
        answer = max(self.foods)

        print(answer)
        return answer

    def solve_part_2(self):
        sorted_foods = sorted(self.foods)
        answer = sorted_foods[-1] + sorted_foods[-2] + sorted_foods[-3]
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
