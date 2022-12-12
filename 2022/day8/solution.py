from pathlib import Path

import numpy as np


def view_score(view, height):
    score = 0
    for tree in view:
        if tree < height:
            score += 1
        else:
            score += 1
            break
    return score


def scenic_view(trees, i, j):
    tree = trees[i, j]
    view1 = trees[:i, j][::-1]
    view2 = trees[i, :j][::-1]
    view3 = trees[i + 1 :, j]
    view4 = trees[i, j + 1 :]
    return (
        view_score(view1, tree)
        * view_score(view2, tree)
        * view_score(view3, tree)
        * view_score(view4, tree)
    )


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
            self.trees = np.array(
                [[int(x) for x in line.strip()] for line in self.input]
            )

    def solve_part_1(self):
        answer = 0
        for i in range(self.trees.shape[0]):
            for j in range(self.trees.shape[1]):
                tree = self.trees[i, j]
                if (
                    np.all(tree > self.trees[:i, j])
                    or np.all(tree > self.trees[i, :j])
                    or np.all(tree > self.trees[i + 1 :, j])
                    or np.all(tree > self.trees[i, j + 1 :])
                ):
                    answer += 1
        print(answer)
        return answer

    def solve_part_2(self):
        max_ = 0
        for i in range(self.trees.shape[0]):
            for j in range(self.trees.shape[1]):
                max_ = max(max_, scenic_view(self.trees, i, j))
        print(max_)
        return max_

    def save_results(self):
        with open(Path(__file__).parent / "part1", "w") as opened_file:
            opened_file.write(str(self.solve_part_1()))

        with open(Path(__file__).parent / "part2", "w") as opened_file:
            opened_file.write(str(self.solve_part_2()))


if __name__ == "__main__":
    solution = Solution()
    solution.save_results()
