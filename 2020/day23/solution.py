from pathlib import Path

from tqdm import tqdm


def rotate(l, n):
    return l[n:] + l[:n]


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()[0].strip()

    def solve_part_1(self):
        cups = [int(x) for x in self.input]
        for move in range(100):
            pos = move % len(cups)
            init_label = cups[pos]
            pickup = [
                cups[(pos + 1) % len(cups)],
                cups[(pos + 2) % len(cups)],
                cups[(pos + 3) % len(cups)],
            ]
            for p in pickup:
                cups.remove(p)

            current_label = init_label - 1
            while current_label not in cups:
                current_label -= 1
                if all(current_label < x for x in cups):
                    current_label = max(cups)

            new_pos = cups.index(current_label)
            cups = cups[: new_pos + 1] + pickup + cups[new_pos + 1 :]

            new_idx = cups.index(init_label)
            if new_idx != pos:
                cups = rotate(cups, new_idx - pos)

        final_pos = cups[cups.index(1) :] + cups[: cups.index(1)]
        answer = "".join(str(x) for x in final_pos[1:])
        print(answer)
        return answer

    def solve_part_2(self):
        dict_cup = {}
        cups = [int(x) for x in self.input]
        for i in range(1000000):
            if i < len(cups) - 1:
                dict_cup[cups[i]] = cups[i + 1]
            elif i == len(cups) - 1:
                dict_cup[cups[-1]] = max(cups) + 1
            else:
                dict_cup[i + 1] = i + 2

        dict_cup[1000000] = cups[0]

        current_cup = cups[0]

        for _ in tqdm(range(10000000)):
            pickup1 = dict_cup[current_cup]
            pickup2 = dict_cup[pickup1]
            pickup3 = dict_cup[pickup2]

            dict_cup[current_cup] = dict_cup[pickup3]

            dest_cup = 1000000 if current_cup == 1 else current_cup - 1
            while dest_cup in [pickup1, pickup2, pickup3]:
                dest_cup = 1000000 if dest_cup == 1 else dest_cup - 1

            dict_cup[pickup3] = dict_cup[dest_cup]

            dict_cup[dest_cup] = pickup1

            current_cup = dict_cup[current_cup]

        answer = dict_cup[1] * dict_cup[dict_cup[1]]
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
