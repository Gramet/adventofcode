from pathlib import Path

from aoc_utils import *
import time

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input_parts(INPUT_FILE)
        self.seeds = parse_ints(self.input[0])
        self.maps = []
        for map_ in self.input[1:]:
            cur_map = []
            for line in map_.split("\n")[1:]:
                cur_map.append(parse_ints(line))
            self.maps.append(cur_map)

    def solve_part_1(self):
        for map_ in self.maps:
            for seed_num, seed in enumerate(self.seeds):
                mapped = False
                for desc in map_:
                    if not mapped:
                        dest_start, source_start, range_len = desc
                        if source_start <= seed < source_start + range_len:
                            seed = dest_start + seed - source_start
                            mapped = True
                self.seeds[seed_num] = seed
        answer = min(self.seeds)
        print(answer)
        return answer

    def solve_part_2(self):
        self.seeds = parse_ints(self.input[0])
        self.seeds = [
            (self.seeds[k], self.seeds[k + 1]) for k in range(0, len(self.seeds), 2)
        ]
        seeds_to_map = self.seeds
        for i, map_ in enumerate(self.maps):
            mapped_seeds = []
            while seeds_to_map:
                seed = seeds_to_map.pop(0)
                (seed_start, seed_range) = seed
                mapped = False
                for desc in map_:
                    dest_start, source_start, range_len = desc
                    if (
                        not mapped
                        and seed_start < source_start + range_len
                        and seed_start + seed_range - 1 >= source_start
                    ):
                        # compute range intersect
                        inter_start, inter_end = range_intersect(
                            seed_start,
                            seed_start + seed_range - 1,
                            source_start,
                            source_start + range_len - 1,
                        )
                        # print(
                        #     f"intersection of {seed} and {desc}: {(inter_start, inter_end)}"
                        # )
                        mapped_seeds.append(
                            (
                                inter_start + dest_start - source_start,
                                inter_end - inter_start + 1,
                            )
                        )
                        # split seed range and append to seeds_to_map
                        mapped = True

                        if inter_start != seed_start:
                            seeds_to_map.append((seed_start, inter_start - seed_start))
                        if inter_end != seed_start + seed_range - 1:
                            seeds_to_map.append(
                                (inter_end + 1, seed_start + seed_range - inter_end - 1)
                            )
                        # print(f"seeds to map: {seeds_to_map}")
                        # print(f"mapped seeds: {mapped_seeds}")
                if not mapped:
                    mapped_seeds.append(seed)
            seeds_to_map = mapped_seeds

        answer = min(mapped_seeds, key=lambda x: x[0])[0]
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
