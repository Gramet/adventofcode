from pathlib import Path
from itertools import cycle
from collections import defaultdict
from copy import deepcopy


class Piece:
    def __init__(self, max_alt):
        self.coos = []

    def move_piece(self, delta):
        new_coos = [(x[0] + delta[0], x[1] + delta[1]) for x in self.coos]
        return new_coos

    def update_coos(self, coos):
        self.coos = coos


class DashPiece(Piece):
    def __init__(self, max_alt):
        self.coos = [
            (2, max_alt + 4),
            (3, max_alt + 4),
            (4, max_alt + 4),
            (5, max_alt + 4),
        ]


class PlusPiece(Piece):
    def __init__(self, max_alt):
        self.coos = [
            (3, max_alt + 4),
            (2, max_alt + 5),
            (3, max_alt + 5),
            (4, max_alt + 5),
            (3, max_alt + 6),
        ]


class LPiece(Piece):
    def __init__(self, max_alt):
        self.coos = [
            (2, max_alt + 4),
            (3, max_alt + 4),
            (4, max_alt + 4),
            (4, max_alt + 5),
            (4, max_alt + 6),
        ]


class IPiece(Piece):
    def __init__(self, max_alt):
        self.coos = [
            (2, max_alt + 4),
            (2, max_alt + 5),
            (2, max_alt + 6),
            (2, max_alt + 7),
        ]


class SquarePiece(Piece):
    def __init__(self, max_alt):
        self.coos = [
            (2, max_alt + 4),
            (3, max_alt + 4),
            (2, max_alt + 5),
            (3, max_alt + 5),
        ]


class Cave(defaultdict):
    def __missing__(self, key):
        return self.default_factory(key)


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()[0].strip()

    def solve_part_1(self):
        self.jet_cycle = cycle(self.input)
        self.piece_cycle = cycle([DashPiece, PlusPiece, LPiece, IPiece, SquarePiece])

        self.cave = Cave(lambda pos: 1 if pos[0] <= -1 or pos[0] >= 7 else 0)
        for i in range(-1, 8):
            self.cave[(i, 0)] = 1
        max_alt = 0
        for _ in range(2022):
            piece = next(self.piece_cycle)(max_alt)
            while True:
                move = next(self.jet_cycle)
                if move == "<":
                    delta = (-1, 0)
                elif move == ">":
                    delta = (1, 0)
                attempted_coos = piece.move_piece(delta)
                if not any(self.cave[coo] for coo in attempted_coos):
                    piece.update_coos(attempted_coos)

                delta_down = (0, -1)
                attempted_coos = piece.move_piece(delta_down)
                if not any(self.cave[coo] for coo in attempted_coos):
                    piece.update_coos(attempted_coos)
                else:
                    for coo in piece.coos:
                        self.cave[coo] = 1
                    break
            max_alt = max(max_alt, max(x[1] for x in piece.coos))
        answer = max_alt
        print(answer)
        return answer

    def solve_part_2(self):
        self.jet_cycle = cycle(self.input)
        self.piece_cycle = cycle([DashPiece, PlusPiece, LPiece, IPiece, SquarePiece])
        self.cave = Cave(lambda pos: 1 if pos[0] <= -1 or pos[0] >= 7 else 0)
        for i in range(-1, 8):
            self.cave[(i, 0)] = 1
        max_alt = 0
        max_alts = [0, 0, 0, 0, 0, 0, 0]
        piece_idx = 0
        jet_idx = 0
        alts_dict = {}
        num_pieces = 0
        period = None
        target_num = 1000000000000
        while True:
            # Cycle detection
            max_diffs = [max_alt - max_alts[i] for i in range(len(max_alts))]
            max_diff = max(max_diffs)
            tableau = [
                str(self.cave[(x, y)])
                for x in range(0, 7)
                for y in range(max_alt - max_diff, max_alt + 2)
            ]
            key = "-".join(str(x) for x in tableau + [piece_idx, jet_idx])
            if key in alts_dict and period is None:
                period = num_pieces - alts_dict[key][0]
                alt_diff = max_alt - alts_dict[key][1]
                num_period_left = (target_num - num_pieces) // period
            else:
                alts_dict[key] = (num_pieces, max_alt)

            piece = next(self.piece_cycle)(max_alt)
            while True:
                jet_idx = (jet_idx + 1) % len(self.input)
                move = next(self.jet_cycle)
                if move == "<":
                    delta = (-1, 0)
                elif move == ">":
                    delta = (1, 0)
                attempted_coos = piece.move_piece(delta)
                if not any(self.cave[coo] for coo in attempted_coos):
                    piece.update_coos(attempted_coos)

                delta_down = (0, -1)
                attempted_coos = piece.move_piece(delta_down)
                if not any(self.cave[coo] for coo in attempted_coos):
                    piece.update_coos(attempted_coos)
                else:
                    for coo in piece.coos:
                        self.cave[coo] = 1
                    break
            for i in range(len(max_alts)):
                max_alts[i] = max(
                    max_alts[i],
                    max(x[1] if x[0] == i else 0 for x in piece.coos),
                )
            max_alt = max(max_alts)
            piece_idx = (piece_idx + 1) % 5
            num_pieces += 1
            if period is not None and num_pieces % period == target_num % period:
                num_period_left = (target_num - num_pieces) // period
                answer = max_alt + num_period_left * alt_diff
                break
            if num_pieces == target_num:
                break

        # answer = max_alt
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
