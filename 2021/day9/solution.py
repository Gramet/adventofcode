from copy import deepcopy
from pathlib import Path

deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.map = {}
        for row, line in enumerate(self.input):
            for col, char in enumerate(line.strip("\n")):
                self.map[(row, col)] = int(char)

    def solve_part_1(self):
        answer = 0
        for k, v in self.map.items():
            if all(
                self.map.get((k[0] + delta[0], k[1] + delta[1]), 9999) > v
                for delta in deltas
            ):
                answer += v + 1
        print(answer)
        return answer

    def solve_part_2(self):
        bassins = []
        for k, v in self.map.items():
            if any(k in b for b in bassins) or v == 9:
                continue
            new_bassin = {k}
            cur_bassin = set()
            while new_bassin - cur_bassin:
                cur_bassin = deepcopy(new_bassin)
                for pos in cur_bassin:
                    for delta in deltas:
                        next_pos = (pos[0] + delta[0], pos[1] + delta[1])
                        if self.map.get(next_pos, 9) != 9:
                            new_bassin.add(next_pos)
            bassins.append(new_bassin)

        bassins = sorted(bassins, key=lambda x: len(x), reverse=True)
        answer = len(bassins[0]) * len(bassins[1]) * len(bassins[2])
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
