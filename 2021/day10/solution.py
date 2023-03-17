from pathlib import Path

opening = ["(", "<", "{", "["]
closing = [")", ">", "}", "]"]
close_map = {op: close for op, close in zip(opening, closing)}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
close_points = {")": 1, "]": 2, "}": 3, ">": 4}
from statistics import median


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        answer = 0
        for line in self.input:
            line = line.strip("\n")

            opened = [line[0]]
            for char in line[1:]:
                if char in opening:
                    opened.append(char)
                elif char in closing:
                    if char != close_map[opened[-1]]:
                        answer += points[char]
                        break
                    else:
                        opened.pop(-1)

        print(answer)
        return answer

    def solve_part_2(self):
        incomplete_scores = []
        for line in self.input:
            line = line.strip("\n")
            opened = [line[0]]
            is_corrupt = False
            for char in line[1:]:
                if char in opening:
                    opened.append(char)
                elif char in closing:
                    if char != close_map[opened[-1]]:
                        is_corrupt = True
                        break
                    else:
                        opened.pop(-1)
            if is_corrupt:
                continue
            closing_seq = list(map(lambda x: close_map[x], opened[::-1]))
            score = 0
            for char in closing_seq:
                score *= 5
                score += close_points[char]
            incomplete_scores.append(score)
        answer = median(incomplete_scores)

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
