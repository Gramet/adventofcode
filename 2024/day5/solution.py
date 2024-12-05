from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = read_input_parts(INPUT_FILE)
        self.page_orders, self.page_updates = self.input

        self.page_orders = [parse_ints(p) for p in self.page_orders.splitlines()]
        self.page_updates = [parse_ints(p) for p in self.page_updates.splitlines()]

        self.page_order_dict = {}
        for page_before, page_after in self.page_orders:
            self.page_order_dict[page_before] = self.page_order_dict.get(
                page_before, {"before": [], "after": []}
            )
            self.page_order_dict[page_before]["after"].append(page_after)

            self.page_order_dict[page_after] = self.page_order_dict.get(
                page_after, {"before": [], "after": []}
            )
            self.page_order_dict[page_after]["before"].append(page_before)

    def is_update_correct(self, page_update):
        for i, page_number in enumerate(page_update):
            pages_before = page_update[:i]
            pages_after = page_update[i + 1 :]
            if any(
                page not in self.page_order_dict[page_number]["before"]
                for page in pages_before
            ) or any(
                page not in self.page_order_dict[page_number]["after"]
                for page in pages_after
            ):
                return False
        return True

    def correct_update(self, page_update):
        corrected_update = {}
        for page_number in page_update:
            pages_before = self.page_order_dict[page_number]["before"]
            corrected_update[page_number] = {
                "before": [p for p in pages_before if p in page_update],
            }
        corrected_update = sorted(
            corrected_update.keys(), key=lambda k: len(corrected_update[k]["before"])
        )
        return corrected_update

    def solve_part_1(self):
        answer = 0
        for update in self.page_updates:
            if self.is_update_correct(update):
                answer += update[(len(update) - 1) // 2]
        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        for update in self.page_updates:
            if not self.is_update_correct(update):
                corrected_update = self.correct_update(update)
                answer += corrected_update[(len(corrected_update) - 1) // 2]
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
