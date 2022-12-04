from pathlib import Path
from string import ascii_letters

priority = {letter: i+1 for i, letter in enumerate(ascii_letters)}


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        answer = 0
        for bag in self.input:
            comp1, comp2 = bag[:round(len(bag)//2)], bag[round(len(bag)//2):]
            common_item = set(comp1).intersection(set(comp2))
            answer += priority[list(common_item)[0]]
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for i in range(0, len(self.input), 3):
            bag1, bag2, bag3 = set(self.input[i].strip()), set(
                self.input[i+1].strip()), set(self.input[i+2].strip())
            common_item = bag1.intersection(bag2, bag3)
            answer += priority[list(common_item)[0]]
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
