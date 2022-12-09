from pathlib import Path


def update_cur_dir(cur_dir, new_dir):
    if cur_dir is None:
        return new_dir
    elif new_dir == "..":
        return "/".join(cur_dir.split("/")[:-1])
    else:
        return f"{cur_dir}/{new_dir}"


def list_content(input, start_idx, cur_dir):
    line = input[start_idx]
    idx = start_idx
    content = {"dirs": [], "filesizes": [], "filenames": []}
    while not line.startswith("$"):
        if line.startswith("dir"):
            content["dirs"].append(f"{cur_dir}/{line.split(' ')[-1].strip()}")
        else:
            content["filenames"].append(line.split(" ")[-1].strip())
            content["filesizes"].append(int(line.split(" ")[0]))
        idx += 1
        try:
            line = input[idx]
        except:
            return content

    return content


def parse_terminal(input):
    cur_dir = None
    tree = {}
    for i, line in enumerate(input):
        line = line.strip()
        if line.startswith("$ cd"):
            cur_dir = update_cur_dir(cur_dir, line.split("cd ")[1])
        elif line.startswith("$ ls"):
            tree[cur_dir] = list_content(input, i + 1, cur_dir)
        else:
            pass
    return tree


def compute_dir_size(dir, tree):
    tree[dir]["dirsize"] = tree[dir].get(
        "dirsize",
        sum(tree[dir]["filesizes"])
        + sum(
            compute_dir_size(internal_dir, tree) for internal_dir in tree[dir]["dirs"]
        ),
    )
    return tree[dir]["dirsize"]


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

    def solve_part_1(self):
        tree = parse_terminal(self.input)
        answer = 0
        for dir in tree:
            dir_size = compute_dir_size(dir, tree)
            if dir_size <= 100000:
                answer += dir_size
        print(answer)
        return answer

    def solve_part_2(self):
        tree = parse_terminal(self.input)
        for dir in tree:
            dir_size = compute_dir_size(dir, tree)
        free_space = 70000000 - tree["/"]["dirsize"]
        needed_space = 30000000 - free_space

        answer = free_space
        for dir in tree:
            if answer >= tree[dir]["dirsize"] >= needed_space:
                answer = tree[dir]["dirsize"]

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
