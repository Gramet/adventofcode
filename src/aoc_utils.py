from collections import defaultdict
from pathlib import Path

## Input parsing


def read_input(path: Path):
    with open(path, "r") as f:
        return f.readlines()


def read_input_parts(path: Path):
    with open(path, "r") as f:
        data = f.read()
        return data.split("\n\n")


## 2d Map and images

deltas4_2d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
deltas5_2d = deltas4_2d + [(0, 0)]
deltas8_2d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
deltas9_2d = deltas8_2d + [(0, 0)]

AOC_INT_MAP = {1: "#", 0: "."}
AOC_CHR_MAP = {"#": 1, ".": 0}


def get_min_coos(d: dict):
    min_r = min(d.keys(), key=lambda x: x[0])[0]
    max_r = max(d.keys(), key=lambda x: x[0])[0]
    min_c = min(d.keys(), key=lambda x: x[1])[1]
    max_c = max(d.keys(), key=lambda x: x[1])[1]
    return min_r, max_r, min_c, max_c


def ascii_image_to_map(
    image: list[str], chr_map: dict[str, int] = AOC_CHR_MAP
) -> defaultdict:
    res = defaultdict(int)
    for r, line in enumerate(image):
        for c, chr in enumerate(line.strip()):
            res[(r, c)] = chr_map[chr]
    return res


def print_2d_image(d: dict, int_map: dict[int, str] = AOC_INT_MAP):
    min_r, max_r, min_c, max_c = get_min_coos(d)
    img_str = ""
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            img_str += int_map[d[(r, c)]]
        img_str += "\n"
    img_str += "\n"
    print(img_str)
