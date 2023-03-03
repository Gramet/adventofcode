from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = [int(x) for x in f.readlines()]

    def solve_part_1(self):
        answer = 0
        for el1, el2 in zip(self.input[:-1], self.input[1:]):
            if el2 > el1:
                answer += 1
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for i in range(len(self.input) - 3):
            if sum(self.input[i : i + 3]) < sum(self.input[i + 1 : i + 4]):
                answer += 1
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
