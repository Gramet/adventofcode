import itertools
from pathlib import Path

import numpy as np

swaps = list(itertools.permutations([0, 1, 2]))
inverts = list(itertools.product([1, -1], repeat=3))


def generate_rotations(scanner):
    res = []
    for swap in swaps:
        for invert in inverts:
            res.append((scanner[:, swap] * np.array(invert), swap, invert))
    return res


def revert_coordinates(beacons, swap, invert, scanner_pos):
    # Revert axes and swap
    beacons = beacons[:, swap] * np.array(invert)
    beacons = beacons + scanner_pos
    return beacons


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        scanners = dict()
        scanner_num = 0
        for line in self.input[1:]:
            if line.startswith("\n"):
                continue
            if line.startswith("---"):
                scanner_num += 1
                continue
            x, y, z = list(map(int, line.strip().split(",")))
            scanners[scanner_num] = scanners.get(scanner_num, []) + [[x, y, z]]

        self.scanners = {k: np.array(v) for k, v in scanners.items()}

    def solve_part_1(self):
        answer = "None"
        beacons = set(tuple(x) for x in self.scanners[0])
        self.known_scanners = {
            0: (
                0,
                0,
                0,
            )
        }
        checked = set()
        while len(self.known_scanners) != len(self.scanners):
            exit_loops = False
            for scan_num in self.known_scanners:
                for scan_num2 in range(len(self.scanners)):
                    if (
                        scan_num2 in self.known_scanners
                        or (scan_num, scan_num2) in checked
                    ):
                        continue
                    checked.add((scan_num, scan_num2))
                    rots = generate_rotations(self.scanners[scan_num2])
                    for rot in rots:
                        diffs = {}
                        for beacon in self.scanners[scan_num]:
                            for beacon1 in rot[0]:
                                diffs[tuple(beacon - beacon1)] = (
                                    diffs.get(tuple(beacon - beacon1), 0) + 1
                                )
                        max_k = max(diffs, key=diffs.get)
                        if diffs[max_k] == 12:
                            print(
                                f"Found intersection between scanners {scan_num} and {scan_num2} with swap {rot[1]} and invert {rot[2]}"
                            )
                            self.known_scanners[scan_num2] = tuple(max_k)
                            beacon_coos = revert_coordinates(
                                beacons=self.scanners[scan_num2],
                                swap=rot[1],
                                invert=rot[2],
                                scanner_pos=max_k,
                            )
                            self.scanners[scan_num2] = beacon_coos
                            beacons = beacons.union(set(tuple(x) for x in beacon_coos))
                            exit_loops = True
                        if exit_loops:
                            break
                    if exit_loops:
                        break
                if exit_loops:
                    break
        answer = len(beacons)
        print(answer)
        return answer

    def solve_part_2(self):
        max_dist = 0
        print(self.known_scanners)
        for scanner in self.known_scanners.values():
            for scanner2 in self.known_scanners.values():
                max_dist = max(
                    abs(scanner[0] - scanner2[0])
                    + abs(scanner[1] - scanner2[1])
                    + abs(scanner[2] - scanner2[2]),
                    max_dist,
                )
        answer = max_dist
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
