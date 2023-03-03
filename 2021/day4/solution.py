from pathlib import Path

import numpy as np


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.read().split("\n\n")
        self.numbers = self.input[0]
        self.numbers = [int(x) for x in self.numbers.split(",")]
        self.boards = self.input[1:]
        self.boards = [
            np.array(
                [
                    [int(row[i : i + 2]) for i in range(0, len(row.strip("\n")), 3)]
                    for row in board.split("\n")
                ]
            )
            for board in self.boards
        ]

    def solve_part_1(self):
        for num in self.numbers:
            for board in self.boards:
                board[board == num] = 0
                if np.any(board.sum(axis=0) == 0) or np.any(board.sum(axis=1) == 0):
                    answer = num * np.sum(board)
                    print(answer)
                    return answer

    def solve_part_2(self):
        winnings = list(range(len(self.boards)))
        for num in self.numbers:
            for board_num, board in enumerate(self.boards):
                board[board == num] = 0
                if np.any(board.sum(axis=0) == 0) or np.any(board.sum(axis=1) == 0):
                    try:
                        winnings.remove(board_num)
                    except ValueError:
                        pass
                    if len(winnings) == 0:

                        answer = num * np.sum(board)
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
