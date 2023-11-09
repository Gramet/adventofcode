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

AOC_CHR_MAP = {1: "#", 0: "."}


def get_min_coos(d):
    min_r = min(d.keys(), key=lambda x: x[0])[0]
    max_r = max(d.keys(), key=lambda x: x[0])[0]
    min_c = min(d.keys(), key=lambda x: x[1])[1]
    max_c = max(d.keys(), key=lambda x: x[1])[1]
    return min_r, max_r, min_c, max_c


def print_2d_image(d, chr_map=AOC_CHR_MAP):
    min_r, max_r, min_c, max_c = get_min_coos(d)
    img_str = ""
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            img_str += chr_map[d[(r, c)]]
        img_str += "\n"
    img_str += "\n"
    print(img_str)
