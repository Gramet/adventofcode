from pathlib import Path

from aoc_utils import *

INPUT_FILE = Path(__file__).parent / "input"
import networkx as nx

class Solution:
    def __init__(self):
        self.input = read_input(INPUT_FILE)
        self.edge_list = []
        for line in self.input:
            node, dest = line.strip().split(': ')
            for dest_node in dest.split():
                self.edge_list.append((node, dest_node))
                
        self.graph = nx.from_edgelist(self.edge_list)

        print(self.graph)
        
    def solve_part_1(self):
        self.graph.remove_edges_from(nx.minimum_edge_cut(self.graph))
        components = list(nx.connected_components(self.graph))
        answer = len(components[0]) * len(components[1])
        
        print(answer)
        return answer

    def solve_part_2(self):
        answer = "None"
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
