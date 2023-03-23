from pathlib import Path

deltas = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.map = {}
        for r, row in enumerate(self.input):
            for c, val in enumerate(row.strip("\n")):
                self.map[(r, c)] = int(val)

    def solve_part_1(self):
        answer = 0
        for _ in range(100):
            # first increase
            new_map = {k: v + 1 for k, v in self.map.items()}
            flashed = set()
            while True:
                for pos, val in new_map.items():
                    if val > 9 and pos not in flashed:
                        answer += 1
                        flashed.add(pos)
                        for delta in deltas:
                            new_pos = (pos[0] + delta[0], pos[1] + delta[1])
                            if new_pos in new_map:
                                new_map[new_pos] += 1

                if all(k in flashed for k, v in new_map.items() if v > 9):
                    break
            self.map = {k: v if v <= 9 else 0 for k, v in new_map.items()}
        print(answer)
        return answer

    def solve_part_2(self):
        step = 0
        while True:
            step += 1
            # first increase
            new_map = {k: v + 1 for k, v in self.map.items()}
            flashed = set()
            while True:
                for pos, val in new_map.items():
                    if val > 9 and pos not in flashed:
                        flashed.add(pos)
                        for delta in deltas:
                            new_pos = (pos[0] + delta[0], pos[1] + delta[1])
                            if new_pos in new_map:
                                new_map[new_pos] += 1
                if all(k in flashed for k in new_map):
                    answer = step + 100
                    print(answer)
                    return answer
                if all(k in flashed for k, v in new_map.items() if v > 9):
                    break
            self.map = {k: v if v <= 9 else 0 for k, v in new_map.items()}

    def save_results(self):
        with open(Path(__file__).parent / "part1", "w") as opened_file:
            opened_file.write(str(self.solve_part_1()))

        with open(Path(__file__).parent / "part2", "w") as opened_file:
            opened_file.write(str(self.solve_part_2()))


if __name__ == "__main__":
    solution = Solution()
    solution.save_results()
