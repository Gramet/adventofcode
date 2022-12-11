from pathlib import Path


def find_loopsize(key, init=7):
    val = 1
    i = 0
    while val != key:
        val *= init
        val = val % 20201227
        i += 1
    return i


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        card_key = int(self.input[0])
        door_key = int(self.input[1])

        card_loop = find_loopsize(card_key, 7)

        val = 1
        for i in range(card_loop):
            val *= door_key
            val = val % 20201227

        answer = val
        print(answer)
        return answer

    def solve_part_2(self):
        answer = "None"
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
