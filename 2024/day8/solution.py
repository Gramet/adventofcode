from pathlib import Path

from aoc_utils import *
from string import ascii_letters, digits

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = ascii_image_to_map(
            self.input, chr_map=AOC_CHR_MAP | {x: x for x in ascii_letters + digits}
        )
        self.antennas = {pos: val for pos, val in self.map.items() if val != 0}

    def solve_part_1(self):
        antinodes = set()
        for antenna, freq in self.antennas.items():
            other_antennas = {
                pos: val for pos, val in self.antennas.items() if val == freq
            }
            for other in other_antennas:
                if antenna == other:
                    continue
                delta_pos = (other[0] - antenna[0], other[1] - antenna[1])
                antinode_pos = (antenna[0] - delta_pos[0], antenna[1] - delta_pos[1])
                if antinode_pos in self.map:
                    antinodes.add(antinode_pos)
        answer = len(antinodes)
        print(answer)
        return answer

    def solve_part_2(self):
        antinodes = set()
        for antenna, freq in self.antennas.items():
            other_antennas = {
                pos: val for pos, val in self.antennas.items() if val == freq
            }
            for other in other_antennas:
                if antenna == other:
                    continue
                delta_pos = (other[0] - antenna[0], other[1] - antenna[1])
                antinode_pos = antenna
                while antinode_pos in self.map:
                    antinodes.add(antinode_pos)
                    antinode_pos = (
                        antinode_pos[0] - delta_pos[0],
                        antinode_pos[1] - delta_pos[1],
                    )
        answer = len(antinodes)
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
