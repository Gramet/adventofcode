from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = ascii_image_to_map(self.input, {x: x for x in "S|-LJ7F."})
        self.start_pos = [k for k, v in self.map.items() if v == "S"][0]

    def traverse_pipe(self, cur_pos, prev_pos):
        match self.map[cur_pos]:
            case "|":
                if cur_pos[0] > prev_pos[0]:
                    return (cur_pos[0] + 1, cur_pos[1])
                else:
                    return (cur_pos[0] - 1, cur_pos[1])
            case "-":
                if cur_pos[1] > prev_pos[1]:
                    return (cur_pos[0], cur_pos[1] + 1)
                else:
                    return (cur_pos[0], cur_pos[1] - 1)
            case "L":
                if cur_pos[0] > prev_pos[0]:
                    return (cur_pos[0], cur_pos[1] + 1)
                else:
                    return (cur_pos[0] - 1, cur_pos[1])
            case "J":
                if cur_pos[0] > prev_pos[0]:
                    return (cur_pos[0], cur_pos[1] - 1)
                else:
                    return (cur_pos[0] - 1, cur_pos[1])
            case "7":
                if cur_pos[0] < prev_pos[0]:
                    return (cur_pos[0], cur_pos[1] - 1)
                else:
                    return (cur_pos[0] + 1, cur_pos[1])
            case "F":
                if cur_pos[0] < prev_pos[0]:
                    return (cur_pos[0], cur_pos[1] + 1)
                else:
                    return (cur_pos[0] + 1, cur_pos[1])

    def solve_part_1(self):
        steps = 1
        cur_pos = (self.start_pos[0], self.start_pos[1] - 1)  # connected to S
        prev_pos = self.start_pos
        self.curve = [cur_pos]
        while self.map[cur_pos] != "S":
            temp = cur_pos
            cur_pos = self.traverse_pipe(cur_pos, prev_pos)
            self.curve.append(cur_pos)
            prev_pos = temp
            steps += 1
        answer = int(steps / 2)
        print(answer)
        return answer

    def solve_part_2(self):
        # area with Shoelace theorem
        curve_area = 0
        for i, pos in enumerate(self.curve):
            curve_area += (
                pos[0] * self.curve[(i + 1) % len(self.curve)][1]
                - pos[1] * self.curve[(i + 1) % len(self.curve)][0]
            )
        curve_area = abs(curve_area / 2)

        # Picks theorem
        answer = int(curve_area - len(self.curve) / 2 + 1)
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
