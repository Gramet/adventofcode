from copy import deepcopy
from pathlib import Path

coo_map = {"e": 0, "se": 1, "ne": 2}
dir_map = {"e": 1, "se": 1, "ne": 1, "w": -1, "sw": -1, "nw": -1}

dirs = ["e", "se", "ne", "w", "sw", "nw"]


def tile_neigh(tile, dir):
    match dir:
        case "e":
            return (tile[0] + 1, tile[1], tile[2])
        case "w":
            return (tile[0] - 1, tile[1], tile[2])
        case "ne":
            return (tile[0], tile[1], tile[2] + 1)
        case "nw":
            return (tile[0] - 1, tile[1], tile[2] + 1)
        case "se":
            return (tile[0] + 1, tile[1], tile[2] - 1)
        case "sw":
            return (tile[0], tile[1], tile[2] - 1)


def reduce(coos):
    reduced_coos = []
    for coo in coos:
        reduced_coo = (coo[0] + coo[1], 0, coo[2] - coo[1])
        reduced_coos.append(reduced_coo)
    return reduced_coos


def get_neighbours(tiles):
    neighs = []
    for tile in tiles:
        new_neighs = [tile_neigh(tile, dir) for dir in dirs]
        neighs += new_neighs
    return neighs


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = [line.strip() for line in f.readlines()]
        self.coos = []
        for line_num, line in enumerate(self.input):
            self.coos.append((0, 0, 0))
            i = 0
            while i < len(line):
                if line[i] == "e":
                    self.coos[line_num] = tile_neigh(self.coos[line_num], "e")
                    i += 1
                elif line[i] == "w":
                    self.coos[line_num] = tile_neigh(self.coos[line_num], "w")
                    i += 1
                elif line[i : i + 2] == "se":
                    self.coos[line_num] = tile_neigh(self.coos[line_num], "se")
                    i += 2
                elif line[i : i + 2] == "nw":
                    self.coos[line_num] = tile_neigh(self.coos[line_num], "nw")
                    i += 2
                elif line[i : i + 2] == "ne":
                    self.coos[line_num] = tile_neigh(self.coos[line_num], "ne")
                    i += 2
                elif line[i : i + 2] == "sw":
                    self.coos[line_num] = tile_neigh(self.coos[line_num], "sw")
                    i += 2

    def solve_part_1(self):
        self.coos = reduce(self.coos)
        self.black = set()
        for tile in self.coos:
            if tile not in self.black:
                self.black.add(tile)
            else:
                self.black.remove(tile)
        answer = len(self.black)
        print(answer)
        return answer

    def solve_part_2(self):
        for day in range(100):
            neighbours = get_neighbours(self.black)
            new_black = set()
            for black_tile in self.black:
                if 0 < neighbours.count(black_tile) <= 2:
                    new_black.add(black_tile)

            for neigh in neighbours:
                if (
                    neighbours.count(neigh) == 2
                    and (neigh not in self.black)
                    and (neigh not in new_black)
                ):
                    new_black.add(neigh)

            self.black = new_black
            print(f"Day {day}: {len(self.black)} black tiles")
        answer = len(self.black)
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
