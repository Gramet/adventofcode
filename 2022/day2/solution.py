from pathlib import Path

move_score = {"X": 1, "Y": 2, "Z": 3}
match_scores = {1: 6, 0: 3, -1: 0}
match_move_score = {"X": -1, "Y": 0, "Z": 1}


def rock_paper_scissor(opponent_move, my_move):
    """Return the match result"""
    match opponent_move:
        case "A":
            if my_move == "X":
                return 0
            elif my_move == "Y":
                return 1
            else:
                return -1
        case "B":
            if my_move == "X":
                return -1
            elif my_move == "Y":
                return 0
            else:
                return 1
        case "C":
            if my_move == "X":
                return 1
            elif my_move == "Y":
                return -1
            else:
                return 0


def rigged_rock_paper_scissor(opponent_move, expected_result):
    """Return the move to match the expected result"""
    match opponent_move:
        case "A":
            if expected_result == "X":
                return "Z"
            elif expected_result == "Y":
                return "X"
            else:
                return "Y"
        case "B":
            if expected_result == "X":
                return "X"
            elif expected_result == "Y":
                return "Y"
            else:
                return "Z"
        case "C":
            if expected_result == "X":
                return "Y"
            elif expected_result == "Y":
                return "Z"
            else:
                return "X"


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
            self.opponent_move = [x.split(" ")[0] for x in self.input]
            self.my_move = [x.split(" ")[1].strip() for x in self.input]

    def solve_part_1(self):
        score = 0
        for opponent_move, my_move in zip(self.opponent_move, self.my_move):
            score += (
                move_score[my_move]
                + match_scores[rock_paper_scissor(opponent_move, my_move)]
            )
        answer = score
        print(answer)
        return answer

    def solve_part_2(self):
        score = 0
        for opponent_move, my_move in zip(self.opponent_move, self.my_move):
            score += (
                move_score[rigged_rock_paper_scissor(opponent_move, my_move)]
                + match_scores[match_move_score[my_move]]
            )
        answer = score
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
