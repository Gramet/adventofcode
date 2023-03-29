from pathlib import Path
import heapq

deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

        self.map = {}
        for r, row in enumerate(self.input):
            for c, risk in enumerate(row.strip("\n")):
                self.map[(r, c)] = int(risk)

        self.end_pos = (r, c)

    def solve_part_1(self):
        start_pos = (0, 0, 0)
        queue = [start_pos]
        best_path_risk = 999999999
        seen = {(0, 0): 0}
        while queue:
            pos = queue.pop(0)
            pos, risk = (pos[0], pos[1]), pos[2]
            for delta in deltas:
                next_pos = (pos[0] + delta[0], pos[1] + delta[1])
                if next_pos not in self.map:
                    continue
                next_risk = risk + self.map[next_pos]
                if next_risk >= best_path_risk:
                    continue
                if next_pos in seen and next_risk >= seen[next_pos]:
                    continue
                seen[next_pos] = next_risk
                if next_pos == self.end_pos:
                    best_path_risk = next_risk
                else:
                    queue.append(next_pos + (next_risk,))

        answer = best_path_risk
        print(answer)
        return answer

    def solve_part_2(self):
        self.full_map = {}
        self.map_length, self.map_height = self.end_pos
        for r, row in enumerate(self.input):
            for c, risk in enumerate(row.strip("\n")):
                for rep_right in range(5):
                    for rep_down in range(5):
                        risk_val = int(risk) + rep_down + rep_right
                        if risk_val > 9:
                            risk_val -= 9
                        self.full_map[
                            (
                                r + rep_right * (self.map_length + 1),
                                c + rep_down * (self.map_height + 1),
                            )
                        ] = risk_val

        self.end_pos = (
            r + rep_right * (self.map_length + 1),
            c + rep_down * (self.map_height + 1),
        )

        start_pos = (0, 0, 0)
        queue = [start_pos]
        best_path_risk = 0
        for col in range(1, self.end_pos[0] + 1):
            best_path_risk += self.full_map[(col, 0)]
        for row in range(1, self.end_pos[1] + 1):
            best_path_risk += self.full_map[(self.end_pos[0], row)]
        seen = {(0, 0): 0}
        while queue:
            pos = heapq.heappop(queue)
            risk, pos = pos[0], (pos[1], pos[2])
            for delta in deltas:
                next_pos = (pos[0] + delta[0], pos[1] + delta[1])
                if next_pos not in self.full_map:
                    continue
                next_risk = risk + self.full_map[next_pos]
                if next_risk >= best_path_risk:
                    continue
                if next_pos in seen and next_risk >= seen[next_pos]:
                    continue
                seen[next_pos] = next_risk
                if next_pos == self.end_pos:
                    best_path_risk = next_risk
                else:
                    heapq.heappush(queue, (next_risk,) + next_pos)

        answer = best_path_risk
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
