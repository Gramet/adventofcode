from pathlib import Path


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        answer = 0
        for pair in self.input:
            range1, range2 = pair.split(',')
            start1, end1 = map(int, range1.split('-'))
            start2, end2 = map(int, range2.split('-'))
            if (start1 <= start2 and end1 >= end2) or (start1 >= start2 and end1 <= end2):
                answer += 1
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for pair in self.input:
            range1, range2 = pair.split(',')
            start1, end1 = map(int, range1.split('-'))
            start2, end2 = map(int, range2.split('-'))
            if not((start1 < start2 and end1 < start2) or (start1 > start2 and start1 > end2)):
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
