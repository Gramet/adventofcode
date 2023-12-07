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
            hand_val = 6
        case [1, 4]:
            hand_val = 5
        case [2, 3]:
            hand_val = 4
        case [1, 1, 3]:
            hand_val = 3
        case [1, 2, 2]:
            hand_val = 2
        case [1, 1, 1, 2]:
            hand_val = 1
        case [1, 1, 1, 1, 1]:
            hand_val = 0
    return hand_val


def parse_hand(hand):
    hand, bid = hand.split(" ")
    bid = int(bid)
    hand_count = Counter(hand)

    hand_val = get_hand_val(hand_count)

    return (hand_val, tuple(order.index(card) for card in hand), bid)


def parse_hand_with_jokers(hand):
    hand, bid = hand.split(" ")
    bid = int(bid)

    hand_count = Counter(hand)
    count_no_j = Counter(hand.replace("J", ""))
    if len(count_no_j):
        max_card = max(count_no_j, key=hand_count.get)

        hand_count[max_card] += hand_count.get("J", 0)
        del hand_count["J"]
    hand_val = get_hand_val(hand_count)

    return (hand_val, tuple(order_joker.index(card) for card in hand), bid)


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.hands = [parse_hand(x) for x in self.input]
        self.hands_with_jokers = [parse_hand_with_jokers(x) for x in self.input]

    def solve_part_1(self):
        hands = sorted(self.hands)
        answer = 0
        for idx, hand in enumerate(hands):
            answer += (idx + 1) * hand[-1]
        print(answer)
        return answer

    def solve_part_2(self):
        hands = sorted(self.hands_with_jokers)
        answer = 0
        for idx, hand in enumerate(hands):
            answer += (idx + 1) * hand[-1]
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
