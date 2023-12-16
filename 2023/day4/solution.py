from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.games = []
        for line in self.input:
            self.games.append(parse_ints(line))

    def solve_part_1(self):
        answer = 0
        for game in self.games:
            correct_nums = game[1:11]
            my_nums = game[11:]
            pow = -1
            for num in correct_nums:
                if num in my_nums:
                    pow += 1
            if pow >= 0:
                answer += 2**pow

        print(answer)
        return answer

    def solve_part_2(self):
        num_cards = [1] * len(self.games)
        for game_idx, game in enumerate(self.games):
            correct_nums = game[1:11]
            my_nums = game[11:]
            matches = 0
            for num in correct_nums:
                if num in my_nums:
                    matches += 1
            for i in range(game_idx + 1, game_idx + 1 + matches):
                if i <= len(self.games):
                    num_cards[i] += num_cards[game_idx]
        answer = sum(num_cards)
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
