import re
from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

        self.instructions = []
        for line in self.input[10:]:
            line = line[5:]
            num = int(line.split("from")[0])
            col1 = int(line.split("from")[1].split("to")[0])
            col2 = int(line.split("to")[1])
            self.instructions.append((num, col1, col2))

    def get_piles(self):
        schema = self.input[:8]
        self.piles = {x: [] for x in range(1, 10)}
        for line in schema:
            pile = 1
            for i in range(1, 34, 4):
                self.piles[pile].append(line[i].strip())
                pile += 1
        self.piles = {k: "".join(v) for k, v in self.piles.items()}

    def solve_part_1(self):
        self.get_piles()
        for instr in self.instructions:
            num, col1, col2 = instr
            self.piles[col2] = self.piles[col1][:num][::-1] + self.piles[col2]
            self.piles[col1] = self.piles[col1][num:]
        answer = "".join([x[0] for x in self.piles.values()])
        print(answer)
        return answer

    def solve_part_2(self):
        self.get_piles()
        for instr in self.instructions:
            num, col1, col2 = instr
            self.piles[col2] = self.piles[col1][:num] + self.piles[col2]
            self.piles[col1] = self.piles[col1][num:]
        answer = "".join([x[0] for x in self.piles.values()])
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
