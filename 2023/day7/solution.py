from collections import Counter
from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"

order = "23456789TJQKA"
order_joker = "J23456789TQKA"


def get_hand_val(hand_count):
    count_vals = sorted(hand_count.values())
    match count_vals:
        case [5]:
            return 6
        case [1, 4]:
            return 5
        case [2, 3]:
            return 4
        case [1, 1, 3]:
            return 3
        case [1, 2, 2]:
            return 2
        case [1, 1, 1, 2]:
            return 1
        case [1, 1, 1, 1, 1]:
            return 0


def parse_hand(hand):
    hand, bid = hand.split(" ")
    hand_count = Counter(hand)
    hand_val = get_hand_val(hand_count)
    return (hand_val, tuple(order.index(card) for card in hand), int(bid))


def parse_hand_with_jokers(hand):
    hand, bid = hand.split(" ")
    hand_count = Counter(hand)
    count_no_j = Counter(hand.replace("J", ""))
    if len(count_no_j):
        max_card = max(count_no_j, key=hand_count.get)
        hand_count[max_card] += hand_count.get("J", 0)
        del hand_count["J"]
    hand_val = get_hand_val(hand_count)
    return (hand_val, tuple(order_joker.index(card) for card in hand), int(bid))


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.hands = [parse_hand(x) for x in self.input]
        self.hands_with_jokers = [parse_hand_with_jokers(x) for x in self.input]

    def solve_part_1(self):
        answer = sum(
            (idx + 1) * hand[-1] for idx, hand in enumerate(sorted(self.hands))
        )
        print(answer)
        return answer

    def solve_part_2(self):
        answer = sum(
            (idx + 1) * hand[-1]
            for idx, hand in enumerate(sorted(self.hands_with_jokers))
        )
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
