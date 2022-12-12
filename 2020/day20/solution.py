from pathlib import Path

import numpy as np
from scipy.signal import convolve2d

char_map = {".": 0, "#": 1}


def find_neighbours(id, tiles):
    neighbours = []
    tile = tiles[id]

    sides = [
        tile[0, :],
        tile[-1, :],
        tile[:, 0],
        tile[:, -1],
        tile[0, :][::-1],
        tile[-1, :][::-1],
        tile[:, 0][::-1],
        tile[:, -1][::-1],
    ]
    for neigh_id, neigh_tile in tiles.items():
        if neigh_id == id:
            continue
        for side in sides:
            if (
                np.all(side == neigh_tile[0, :])
                or np.all(side == neigh_tile[-1, :])
                or np.all(side == neigh_tile[:, 0])
                or np.all(side == neigh_tile[:, -1])
            ):
                neighbours.append(neigh_id)
    return neighbours


def find_neighbours_sides(id, tiles):
    neighbours = []
    tile = tiles[id]

    sides = [
        tile[0, :],
        tile[-1, :],
        tile[:, 0],
        tile[:, -1],
    ]
    neigh_sides = []
    for neigh_id, neigh_tile in tiles.items():
        if neigh_id == id:
            continue
        neighbour_sides = [
            neigh_tile[0, :],
            neigh_tile[-1, :],
            neigh_tile[:, 0],
            neigh_tile[:, -1],
            neigh_tile[0, :][::-1],
            neigh_tile[-1, :][::-1],
            neigh_tile[:, 0][::-1],
            neigh_tile[:, -1][::-1],
        ]
        for side_id, side in enumerate(sides):
            for neigh_idx, neighbour_side in enumerate(neighbour_sides):
                if np.all(side == neighbour_side):
                    neighbours.append(neigh_id)
                    neigh_sides.append((side_id, neigh_idx))
    return list((neighbours, neigh_sides))


def generate_all_rots(tile):
    tile_lr = np.fliplr(tile)
    tile_ud = np.flipud(tile)
    rots = [
        tile,
        np.rot90(tile, 1),
        np.rot90(tile, 2),
        np.rot90(tile, 3),
        tile_lr,
        np.rot90(tile_lr, 1),
        np.rot90(tile_lr, 2),
        np.rot90(tile_lr, 3),
        tile_ud,
        np.rot90(tile_ud, 1),
        np.rot90(tile_ud, 2),
        np.rot90(tile_ud, 3),
    ]
    return rots


def build_mat(tiles):
    edges = []
    tiles_neigh = {}
    for tile_id in tiles:
        tiles_neigh[tile_id] = find_neighbours_sides(tile_id, tiles)
        if len(tiles_neigh[tile_id][0]) == 2:
            edges.append(tile_id)
            print(tile_id, tiles_neigh[tile_id])

    for edge in edges:
        dir1 = tiles_neigh[edge][1][0][0]
        dir2 = tiles_neigh[edge][1][1][0]
        if dir1 == 3 and dir2 == 1:
            start = edge
            break
        elif dir2 == 3 and dir1 == 1:
            tiles_neigh[edge][0] = tiles_neigh[edge][0][::-1]
            tiles_neigh[edge][1] = tiles_neigh[edge][1][::-1]
            start = edge
            break
        else:
            tiles[edge] = np.fliplr(tiles[edge])
            tiles_neigh[edge] = find_neighbours_sides(edge, tiles)
            dir1 = tiles_neigh[edge][1][0][0]
            dir2 = tiles_neigh[edge][1][1][0]
            if dir1 == 3 and dir2 == 1:
                start = edge
                break
            elif dir2 == 3 and dir1 == 1:
                print(tiles_neigh[edge][1])
                tiles_neigh[edge][1] = tiles_neigh[edge][1][::-1]
                tiles_neigh[edge][0] = tiles_neigh[edge][0][::-1]
                start = edge
                break
            else:
                tiles[edge] = np.flipud(tiles[edge])
                tiles_neigh[edge] = find_neighbours_sides(edge, tiles)
                dir1 = tiles_neigh[edge][1][0][0]
                dir2 = tiles_neigh[edge][1][1][0]
                if dir1 == 3 and dir2 == 1:
                    start = edge
                    break
                elif dir2 == 3 and dir1 == 1:
                    tiles_neigh[edge][0] = tiles_neigh[edge][0][::-1]
                    tiles_neigh[edge][1] = tiles_neigh[edge][1][::-1]
                    start = edge
                    break
                else:
                    tiles[edge] = np.fliplr(tiles[edge])
                    tiles_neigh[edge] = find_neighbours_sides(edge, tiles)
                    dir1 = tiles_neigh[edge][1][0][0]
                    dir2 = tiles_neigh[edge][1][1][0]
                    if dir1 == 3 and dir2 == 1:
                        start = edge
                        break
                    elif dir2 == 3 and dir1 == 1:
                        tiles_neigh[edge][0] = tiles_neigh[edge][0][::-1]
                        tiles_neigh[edge][1] = tiles_neigh[edge][1][::-1]
                        start = edge
                        break

    print(start, tiles_neigh[start])
    dir1 = tiles_neigh[start][1][0][0]
    dir2 = tiles_neigh[start][1][1][0]
    print(dir1, dir2)
    current = start
    row = [start]
    side_length = int(np.sqrt(len(tiles)))
    for _ in range(side_length - 1):
        for neigh_num, neigh_dir in enumerate(tiles_neigh[current][1]):
            if neigh_dir[0] == dir1:
                nxt = tiles_neigh[current][0][neigh_num]
        all_rots_nxt = generate_all_rots(tiles[nxt])
        for r in all_rots_nxt:
            if dir1 == 0:
                if np.all(r[-1, :] == tiles[current][0, :]):
                    tiles[nxt] = r
                    tiles_neigh[nxt] = find_neighbours_sides(nxt, tiles)
                    row.append(nxt)
                    current = nxt
                    break
            elif dir1 == 1:
                if np.all(r[0, :] == tiles[current][-1, :]):
                    tiles[nxt] = r
                    tiles_neigh[nxt] = find_neighbours_sides(nxt, tiles)
                    row.append(nxt)
                    current = nxt
                    break
            elif dir1 == 2:
                if np.all(r[:, -1] == tiles[current][:, 0]):
                    tiles[nxt] = r
                    tiles_neigh[nxt] = find_neighbours_sides(nxt, tiles)
                    row.append(nxt)
                    current = nxt
                    break
            elif dir1 == 3:
                if np.all(r[:, 0] == tiles[current][:, -1]):
                    tiles[nxt] = r
                    tiles_neigh[nxt] = find_neighbours_sides(nxt, tiles)
                    print(tiles[current][:, -1], tiles[nxt][:, 0])
                    row.append(nxt)
                    current = nxt
                    break

    cols = []
    for new_start in row:
        current = new_start
        col = [new_start]
        side_length = int(np.sqrt(len(tiles)))
        for _ in range(side_length - 1):
            for neigh_num, neigh_dir in enumerate(tiles_neigh[current][1]):
                if neigh_dir[0] == dir2:
                    nxt = tiles_neigh[current][0][neigh_num]
            all_rots_nxt = generate_all_rots(tiles[nxt])
            for r in all_rots_nxt:
                if dir2 == 0:
                    if np.all(r[-1, :] == tiles[current][0, :]):
                        tiles[nxt] = r
                        tiles_neigh[nxt] = find_neighbours_sides(nxt, tiles)
                        print(current, nxt, tiles[current][0, :], tiles[nxt][-1, :])
                        col.append(nxt)
                        current = nxt
                        break
                elif dir2 == 1:
                    if np.all(r[0, :] == tiles[current][-1, :]):
                        tiles[nxt] = r
                        tiles_neigh[nxt] = find_neighbours_sides(nxt, tiles)
                        col.append(nxt)
                        current = nxt
                        break
                elif dir2 == 2:
                    if np.all(r[:, -1] == tiles[current][:, 0]):
                        tiles[nxt] = r
                        tiles_neigh[nxt] = find_neighbours_sides(nxt, tiles)
                        col.append(nxt)
                        current = nxt
                        break
                elif dir2 == 3:
                    if np.all(r[:, 0] == tiles[current][:, -1]):
                        tiles[nxt] = r
                        tiles_neigh[nxt] = find_neighbours_sides(nxt, tiles)
                        col.append(nxt)
                        current = nxt
                        break
        cols.append(col)

    rows = np.transpose(np.array(cols))

    big_mat = np.zeros((int(np.sqrt(len(tiles))) * 10, int(np.sqrt(len(tiles))) * 10))
    for r_id, r in enumerate(rows):
        for c_id, c in enumerate(r):
            big_mat[r_id * 10 : (r_id + 1) * 10, c_id * 10 : (c_id + 1) * 10] = tiles[c]

    to_del = [x for x in range(len(big_mat)) if x % 10 == 0 or x % 10 == 9]
    big_mat = np.delete(big_mat, to_del, 0)
    big_mat = np.delete(big_mat, to_del, 1)

    return big_mat


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()
        self.tiles = {}
        for line in self.input:
            if line.startswith("Tile"):
                tile_id = int(line[5:9])
                tile = np.zeros((10, 10))
                row = 0
            elif line.startswith(".") or line.startswith("#"):
                tile[row] = np.array([char_map[x] for x in line.strip()])
                row += 1
            elif line == "\n":
                self.tiles[tile_id] = tile

    def solve_part_1(self):
        edges = []
        for tile_id in self.tiles:
            if len(find_neighbours(tile_id, self.tiles)) == 2:
                edges.append(tile_id)
                print(tile_id, find_neighbours(tile_id, self.tiles))
        print(edges)
        answer = 1
        for edge in edges:
            answer *= edge
        print(answer)
        return answer

    def solve_part_2(self):
        big_mat = build_mat(self.tiles)

        pattern = "                  # #    ##    ##    ### #  #  #  #  #  #   "
        pattern = [0 if chr == " " else 1 for chr in pattern]
        pattern = np.array(pattern)
        pattern = np.reshape(pattern, (3, -1))
        patterns = generate_all_rots(pattern)
        min_ = np.sum(pattern)
        for p in patterns:
            if np.sum(convolve2d(big_mat, p, mode="valid") >= min_):
                answer = int(
                    np.sum(big_mat)
                    - np.sum(convolve2d(big_mat, p, mode="valid") >= 15) * min_
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
