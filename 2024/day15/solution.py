from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"

EMPTY = 0
WALL = 1
BOX = 2
ROBOT = 3
BOX_LEFT = 4
BOX_RIGHT = 5


class Solution:
    def __init__(self):
        self.mapstr, self.moves = read_input_parts(INPUT_FILE)
        self.map = ascii_image_to_map(
            self.mapstr.splitlines(), AOC_CHR_MAP | {"O": BOX, "@": ROBOT}
        )
        self.moves = self.moves.replace("\n", "")

    def move_robot(self, robot_pos, dir):
        new_robot_pos = robot_pos + dir

        if self.map[new_robot_pos] == WALL:
            return robot_pos
        if self.map[new_robot_pos] == EMPTY:
            self.map[robot_pos] = EMPTY
            self.map[new_robot_pos] = ROBOT
            return new_robot_pos
        if self.map[new_robot_pos] == BOX:
            pos_to_check = new_robot_pos
            while self.map[next_pos := pos_to_check + dir] == BOX:
                pos_to_check = next_pos
            pos_to_check += dir
            if self.map[pos_to_check] == EMPTY:
                self.map[robot_pos] = EMPTY
                self.map[new_robot_pos] = ROBOT
                self.map[pos_to_check] = BOX

                return new_robot_pos
            if self.map[pos_to_check] == WALL:
                return robot_pos

    def solve_part_1(self):
        robot_pos = [pos for pos, val in self.map.items() if val == ROBOT][0]
        for move in self.moves.replace("\n", ""):
            dir = AOC_MOVE_DICT[move]
            robot_pos = self.move_robot(robot_pos, dir)

        answer = sum(100 * pos.x + pos.y for pos, val in self.map.items() if val == BOX)
        print(answer)
        return answer

    def can_box_move(self, box_left_pos, dir, box_to_move=None):
        if box_to_move is None:
            box_to_move = set([box_left_pos])
        else:
            box_to_move.add(box_left_pos)
        box_right_pos = box_left_pos + (0, 1)
        above_left = box_left_pos + dir
        above_right = box_right_pos + dir
        if self.map[above_left] == WALL or self.map[above_right] == WALL:
            return False, box_to_move
        if self.map[above_left] == EMPTY and self.map[above_right] == EMPTY:
            return True, box_to_move

        if self.map[above_left] == BOX_LEFT:
            left_can_move, box_to_move = self.can_box_move(above_left, dir, box_to_move)
        elif self.map[above_left] == BOX_RIGHT:
            left_can_move, box_to_move = self.can_box_move(
                above_left + (0, -1), dir, box_to_move
            )
        elif self.map[above_left] == EMPTY:
            left_can_move = True

        if self.map[above_right] == BOX_LEFT:
            right_can_move, box_to_move = self.can_box_move(
                above_right, dir, box_to_move
            )
        elif self.map[above_right] == BOX_RIGHT:
            right_can_move, box_to_move = self.can_box_move(
                above_right + (0, -1), dir, box_to_move
            )
        elif self.map[above_right] == EMPTY:
            right_can_move = True

        return right_can_move and left_can_move, box_to_move

    def move_robot_p2(self, robot_pos, dir):
        new_robot_pos = robot_pos + dir

        if self.map[new_robot_pos] == WALL:
            return robot_pos
        if self.map[new_robot_pos] == EMPTY:
            self.map[robot_pos] = EMPTY
            self.map[new_robot_pos] = ROBOT
            return new_robot_pos
        if dir[1] == 0 and self.map[new_robot_pos] in [BOX_LEFT, BOX_RIGHT]:
            # Trying to push a box up/down, need to check for multiple spaces

            pos_to_check = new_robot_pos
            if self.map[new_robot_pos] == BOX_LEFT:
                can_move, box_to_move = self.can_box_move(new_robot_pos, dir)
            else:
                can_move, box_to_move = self.can_box_move(new_robot_pos + (0, -1), dir)

            if not can_move:
                return robot_pos

            for box in box_to_move:
                self.map[box] = EMPTY
                self.map[box + (0, 1)] = EMPTY
            for box in box_to_move:
                self.map[box + dir] = BOX_LEFT
                self.map[box + dir + (0, 1)] = BOX_RIGHT
            self.map[new_robot_pos] = ROBOT
            self.map[robot_pos] = EMPTY
            return new_robot_pos

        if self.map[new_robot_pos] in [BOX_LEFT, BOX_RIGHT]:
            pos_to_check = new_robot_pos
            while self.map[next_pos := pos_to_check + dir] in [BOX_LEFT, BOX_RIGHT]:
                pos_to_check = next_pos
            pos_to_check += dir
            if self.map[pos_to_check] == EMPTY:
                while pos_to_check != robot_pos:
                    self.map[pos_to_check] = self.map[pos_to_check - dir]
                    pos_to_check -= dir
                self.map[robot_pos] = EMPTY
                return new_robot_pos
            if self.map[pos_to_check] == WALL:
                return robot_pos

    def solve_part_2(self):
        new_map_str = ""
        for chr in self.mapstr:
            if chr == "#":
                new_map_str += "##"
            elif chr == ".":
                new_map_str += ".."
            elif chr == "O":
                new_map_str += "[]"
            elif chr == "@":
                new_map_str += "@."
            else:
                new_map_str += chr
        chr_dict = AOC_CHR_MAP | {"[": BOX_LEFT, "]": BOX_RIGHT, "@": ROBOT}
        self.map = ascii_image_to_map(
            new_map_str.splitlines(),
            chr_dict,
        )
        robot_pos = [pos for pos, val in self.map.items() if val == ROBOT][0]
        for move in self.moves.replace("\n", ""):
            dir = AOC_MOVE_DICT[move]
            robot_pos = self.move_robot_p2(robot_pos, dir)

        answer = sum(
            100 * pos.x + pos.y for pos, val in self.map.items() if val == BOX_LEFT
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
