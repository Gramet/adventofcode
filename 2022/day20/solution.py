from copy import deepcopy
from pathlib import Path

from tqdm import tqdm


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return f"Node {self.data} - previous = {self.previous.data} - next = {self.next.data}"


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.len = 5000

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            node_to_remove = self.head
            self.head.previous.next = self.head.next
            self.head.next.previous = self.head.previous
            self.head = self.head.next
            return node_to_remove

        for node in self:
            if node.data == target_node_data:
                node_to_remove = node
                node.previous.next = node.next
                node.next.previous = node.previous
                return node_to_remove

        raise Exception("Node with data '%s' not found" % target_node_data)

    def move_right(self, target_node_data, steps):

        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                for _ in range(steps):
                    node_to_move = node
                    node.previous.next = node.next
                    node.next.previous = node.previous
                    node.next.next.previous = node
                    node.previous = node.next
                    node.next = node.next.next
                    node.previous.next = node
                return node_to_move

        raise Exception("Node with data '%s' not found" % target_node_data)

    def move_left(self, target_node_data, steps):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                for _ in range(steps):
                    node_to_move = node
                    node.next.previous = node.previous
                    node.previous.next = node.next
                    node.previous.previous.next = node
                    node.next = node.previous
                    node.previous = node.previous.previous
                    node.next.previous = node
                return node_to_move

        raise Exception("Node with data '%s' not found" % target_node_data)

    def move(self, target_node_data):
        if target_node_data[1] > 0:
            self.move_right(target_node_data, target_node_data[1] % (self.len - 1))
        elif target_node_data[1] < 0:
            self.move_left(target_node_data, abs(target_node_data[1]) % (self.len - 1))

    def traverse_from(self, target_node_data, steps):
        for node in self:
            if node.data == target_node_data:
                res_node = node
                for _ in range(steps):
                    res_node = res_node.next
                return res_node.data[1]


class Solution:
    def __init__(self):
        encryption_key = 811589153
        input_file = "input"
        with open(Path(__file__).parent / input_file, "r") as f:
            self.input = [
                Node((start_idx, int(x))) for start_idx, x in enumerate(f.readlines())
            ]
        with open(Path(__file__).parent / input_file, "r") as f:
            self.encrypted_input = [
                Node((start_idx, encryption_key * int(x)))
                for start_idx, x in enumerate(f.readlines())
            ]
        for i in range(1, len(self.input)):
            self.input[i].previous = self.input[i - 1]
            self.encrypted_input[i].previous = self.encrypted_input[i - 1]
        self.input[0].previous = self.input[-1]
        self.encrypted_input[0].previous = self.encrypted_input[-1]
        for i in range(0, len(self.input) - 1):
            self.input[i].next = self.input[i + 1]
            self.encrypted_input[i].next = self.encrypted_input[i + 1]
        self.input[-1].next = self.input[0]
        self.encrypted_input[-1].next = self.encrypted_input[0]
        for n in self.input:
            if n.data[1] == 0:
                self.zero_node_data = n.data
        for n in self.encrypted_input:
            if n.data[1] == 0:
                self.zero_node_data_encryted = n.data

    def solve_part_1(self):
        circ_list = CircularLinkedList()
        circ_list.head = self.input[0]
        for node in tqdm(self.input):
            circ_list.move(node.data)

        answer = (
            circ_list.traverse_from(self.zero_node_data, 1000)
            + circ_list.traverse_from(self.zero_node_data, 2000)
            + circ_list.traverse_from(self.zero_node_data, 3000)
        )

        print(answer)
        return answer

    def solve_part_2(self):
        circ_list = CircularLinkedList()
        circ_list.head = self.encrypted_input[0]
        for _ in range(10):
            for node in tqdm(self.encrypted_input):
                circ_list.move(node.data)

        answer = (
            circ_list.traverse_from(self.zero_node_data, 1000)
            + circ_list.traverse_from(self.zero_node_data, 2000)
            + circ_list.traverse_from(self.zero_node_data, 3000)
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
