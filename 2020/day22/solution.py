from pathlib import Path


def compute_start(input_):
    p1 = []
    p2 = []
    second = False
    for line in input_[1:]:
        if line == "\n" or line.startswith("Player"):
            second = True
            continue

        if second:
            p2.append(int(line))
        else:
            p1.append(int(line))
    return p1, p2


def compute_answer(p1, p2):
    answer = 0
    if p1:
        for i, c in enumerate(p1[::-1]):
            answer += (i + 1) * c
    else:
        for i, c in enumerate(p2[::-1]):
            answer += (i + 1) * c
    return answer


def recursive_combat(p1, p2):
    played_games = set()

    while len(p1) > 0 and len(p2) > 0:
        if hash((tuple(p1), tuple(p2))) in played_games:
            return p1, []

        played_games.add(hash((tuple(p1), tuple(p2))))
        c1 = p1.pop(0)
        c2 = p2.pop(0)

        if c1 <= len(p1) and c2 <= len(p2):
            tmp1, _ = recursive_combat(p1[:c1], p2[:c2])
            if tmp1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)

    return p1, p2


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        p1, p2 = compute_start(self.input)

        while len(p1) > 0 and len(p2) > 0:
            c1 = p1.pop(0)
            c2 = p2.pop(0)

            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)

        answer = compute_answer(p1, p2)
        print(answer)
        return answer

    def solve_part_2(self):
        p1, p2 = compute_start(self.input)

        p1, p2 = recursive_combat(p1, p2)

        answer = compute_answer(p1, p2)
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
