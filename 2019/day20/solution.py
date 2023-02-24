from pathlib import Path

deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
            self.input = [line.strip("\n") for line in self.input]
        print(self.input)
        self.portals = {}
        self.pos_portals = {}
        for r, row in enumerate(self.input):
            for c, char in enumerate(row):
                if char.isupper():
                    tel_delta = None
                    for delta in deltas:
                        if (0 <= r + delta[0] < len(self.input)) and (
                            0 <= c + delta[1] < len(row)
                        ):
                            if self.input[r + delta[0]][c + delta[1]] == ".":
                                tel_delta = delta
                            if tel_delta is not None:
                                char2 = self.input[r - tel_delta[0]][c - tel_delta[1]]
                                if any(coo < 0 for coo in tel_delta):
                                    portal = char + char2
                                else:
                                    portal = char2 + char

                                portal_pos = (r + tel_delta[0], c + tel_delta[1])
                                portal_char = self.input[r + tel_delta[0]][
                                    c + tel_delta[1]
                                ]
                                self.portals[portal] = self.portals.get(
                                    portal, list()
                                ) + [portal_pos]
                                if portal not in ["AA", "ZZ"]:
                                    self.pos_portals[portal_pos] = portal
                                break

        print(self.portals)
        print(self.pos_portals)
        print(self.portals["AA"])
        print(self.portals["ZZ"])

    def solve_part_1(self):
        seen = set()
        current_pos = [(0, self.portals["AA"][0])]
        dest = self.portals["ZZ"][0]
        while True:
            pos = current_pos.pop(0)
            if pos[1] == dest:
                break
            if pos[1] in seen:
                continue
            seen.add((pos[1]))
            if pos[1] in self.pos_portals:
                other_port = self.portals[self.pos_portals[pos[1]]]
                other_port = [x for x in other_port if x != pos[1]][0]
                current_pos.append((pos[0] + 1, other_port))
            for delta in deltas:
                if (
                    self.input[pos[1][0] + delta[0]][pos[1][1] + delta[1]] == "."
                    and (pos[1][0] + delta[0], pos[1][1] + delta[1]) not in seen
                ):
                    current_pos.append(
                        (pos[0] + 1, (pos[1][0] + delta[0], pos[1][1] + delta[1]))
                    )
        answer = pos[0]
        print(answer)
        return answer

    def solve_part_2(self):
        seen = set()
        current_pos = [(0, self.portals["AA"][0], 1)]
        dest = self.portals["ZZ"][0]
        while True:
            # print(current_pos)
            pos = current_pos.pop(0)
            if pos[1] == dest and pos[2] == 1:
                break
            if (pos[1], pos[2]) in seen:
                continue
            seen.add((pos[1], pos[2]))
            if pos[1] in self.pos_portals:
                if pos[2] == 1 and any(
                    [pos[1][0] == 2, pos[1][1] == 2, pos[1][0] == 116, pos[1][1] == 120]
                ):
                    continue
                elif any(
                    [pos[1][0] == 2, pos[1][1] == 2, pos[1][0] == 116, pos[1][1] == 120]
                ):
                    other_port = self.portals[self.pos_portals[pos[1]]]
                    other_port = [x for x in other_port if x != pos[1]][0]
                    current_pos.append((pos[0] + 1, other_port, pos[2] - 1))
                else:
                    other_port = self.portals[self.pos_portals[pos[1]]]
                    other_port = [x for x in other_port if x != pos[1]][0]
                    current_pos.append((pos[0] + 1, other_port, pos[2] + 1))
            for delta in deltas:
                if (
                    self.input[pos[1][0] + delta[0]][pos[1][1] + delta[1]] == "."
                    and (pos[1][0] + delta[0], pos[1][1] + delta[1]) not in seen
                ):
                    current_pos.append(
                        (
                            pos[0] + 1,
                            (pos[1][0] + delta[0], pos[1][1] + delta[1]),
                            pos[2],
                        )
                    )
        answer = pos[0]
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
