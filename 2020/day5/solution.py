from pathlib import Path

val_dict = {"F": 0, "B": 1, "R": 1, "L": 0}


def get_seat(line):
    row = 0
    col = 0
    for i, chr in enumerate(line[:7]):
        row += 2 ** (6 - i) * val_dict[chr]
    for i, chr in enumerate(line[7:]):
        col += 2 ** (2 - i) * val_dict[chr]
    seat_id = row * 8 + col
    return row, col, seat_id


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        rows = []
        cols = []
        self.seats_id = []
        for line in self.input:
            row, col, seat_id = get_seat(line.strip("\n"))
            rows.append(row)
            cols.append(col)
            self.seats_id.append(seat_id)
        answer = max(self.seats_id)
        print(answer)
        return answer

    def solve_part_2(self):
        for i in range(min(self.seats_id), max(self.seats_id)):
            if i not in self.seats_id:
                answer = i
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
