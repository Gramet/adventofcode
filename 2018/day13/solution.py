from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"

directions = ["N", "E", "S", "W"]
dir_map = {"^": "N", ">": "E", "v": "S", "<": "W"}


class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = dir_map[direction]  # N, E, S, W
        self.turn_dir = "left"

    def move(self, cur_pos):
        match cur_pos:
            case "+":
                self.turn()
                self.change_turn_dir()
            case cur_pos if cur_pos in ["-", "|", "v", "^", "<", ">"]:
                match self.direction:
                    case "N":
                        self.y -= 1
                    case "E":
                        self.x += 1
                    case "S":
                        self.y += 1
                    case "W":
                        self.x -= 1
            case "/":
                match self.direction:
                    case "N":
                        self.direction = "E"
                        self.x += 1
                    case "W":
                        self.direction = "S"
                        self.y += 1
                    case "S":
                        self.direction = "W"
                        self.x -= 1
                    case "E":
                        self.direction = "N"
                        self.y -= 1
            case "\\":
                match self.direction:
                    case "S":
                        self.direction = "E"
                        self.x += 1
                    case "W":
                        self.direction = "N"
                        self.y -= 1
                    case "N":
                        self.direction = "W"
                        self.x -= 1
                    case "E":
                        self.direction = "S"
                        self.y += 1
            case _:
                raise ValueError(f"Invalid move {cur_pos}")

    def turn(self):
        match self.direction, self.turn_dir:
            case "N", "left":
                self.x -= 1
                self.direction = "W"
            case "N", "straight":
                self.y -= 1
            case "N", "right":
                self.x += 1
                self.direction = "E"
            case "E", "left":
                self.y -= 1
                self.direction = "N"
            case "E", "straight":
                self.x += 1
            case "E", "right":
                self.y += 1
                self.direction = "S"
            case "S", "left":
                self.x += 1
                self.direction = "E"
            case "S", "straight":
                self.y += 1
            case "S", "right":
                self.x -= 1
                self.direction = "W"
            case "W", "left":
                self.y += 1
                self.direction = "S"
            case "W", "straight":
                self.x -= 1
            case "W", "right":
                self.y -= 1
                self.direction = "N"
            case _:
                raise ValueError(
                    f"Invalid direction {self.direction} - {self.turn_dir}"
                )

    def change_turn_dir(self):
        match self.turn_dir:
            case "left":
                self.turn_dir = "straight"
            case "straight":
                self.turn_dir = "right"
            case "right":
                self.turn_dir = "left"


class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.map = {}
        self.carts = []
        for y, line in enumerate(self.input):
            for x, char in enumerate(line.strip("\n")):
                self.map[(x, y)] = char
                if char in ["v", "^", "<", ">"]:
                    self.carts.append(Cart(x, y, char))

    def solve_part_1(self):
        while True:
            for cart in sorted(self.carts, key=lambda cart: (cart.y, cart.x)):
                cart.move(self.map[(cart.x, cart.y)])
                for cart2 in self.carts:
                    if cart is not cart2 and cart.x == cart2.x and cart.y == cart2.y:
                        answer = f"{cart.x},{cart.y}"
                        print(answer)
                        return answer

    def solve_part_2(self):
        self.carts = []
        for y, line in enumerate(self.input):
            for x, char in enumerate(line.strip("\n")):
                self.map[(x, y)] = char
                if char in ["v", "^", "<", ">"]:
                    self.carts.append(Cart(x, y, char))
        while True:
            carts_to_remove = []
            for cart in sorted(self.carts, key=lambda cart: (cart.y, cart.x)):
                if cart in carts_to_remove:
                    continue
                cart.move(self.map[(cart.x, cart.y)])
                for cart2 in self.carts:
                    if cart is not cart2 and cart.x == cart2.x and cart.y == cart2.y:
                        carts_to_remove.append(cart2)
                        carts_to_remove.append(cart)
            for cart in carts_to_remove:
                self.carts.remove(cart)
            if len(self.carts) == 1:
                answer = f"{self.carts[0].x},{self.carts[0].y}"
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
