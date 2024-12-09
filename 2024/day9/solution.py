from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"


class Solution:
    def __init__(self):
        self.input = [int(x) for x in read_input(INPUT_FILE)[0].strip("\n")]
        self.files = [int(self.input[i]) for i in range(0, len(self.input), 2)]
        self.file_ids = list(range(len(self.files)))
        self.spaces = [int(self.input[i]) for i in range(1, len(self.input), 2)]

    def solve_part_1(self):
        answer = 0
        cur_id = 0
        pos = 0
        temp_files = self.files.copy()
        temp_files_id = self.file_ids.copy()
        while cur_id < len(temp_files):
            file_len = temp_files[cur_id]
            for _ in range(file_len):
                answer += pos * cur_id
                pos += 1
            space_len = self.spaces[cur_id]
            for _ in range(space_len):
                answer += pos * temp_files_id[-1]
                pos += 1
                temp_files[-1] -= 1
                if temp_files[-1] == 0:
                    temp_files.pop(-1)
                    temp_files_id.pop(-1)

            cur_id += 1

        print(answer)
        return answer

    def solve_part_2(self):
        answer = 0
        disk = []
        file_count = 0
        for i, length in enumerate(self.input):
            if i % 2 == 1:
                file_count += 1
                file_id = -1
            else:
                file_id = file_count

            disk.append([file_id, length, False])
        copy_disk = disk.copy()
        reversed_disk = copy_disk[::-1]
        for reverse_id, (file_id, file_length, has_moved) in enumerate(reversed_disk):
            if file_id == -1 or has_moved:
                continue

            reversed_disk[reverse_id][2] = True
            for i, (space_id, space_length, _) in enumerate(reversed_disk[::-1]):
                if space_id != -1:
                    continue
                if (space_length >= file_length) and len(
                    reversed_disk
                ) - i > reverse_id:
                    file_to_move = reversed_disk[reverse_id].copy()
                    reversed_disk[reverse_id] = [-1, file_length, False]
                    reversed_disk.insert(len(reversed_disk) - i, file_to_move)
                    new_space_length = space_length - file_length
                    reversed_disk[len(reversed_disk) - i - 2] = [
                        space_id,
                        new_space_length,
                        False,
                    ]
                    break

        copy_disk = reversed_disk[::-1]
        pos = 0
        for file_id, length, _ in copy_disk:
            for _ in range(length):
                if file_id != -1:
                    answer += pos * file_id
                pos += 1

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
