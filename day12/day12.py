with open("input", "r") as f:
    lines = f.readlines()

pos = {"E": 0, "N": 0}
waypoint_pos = {"E": 10, "N": 1}
dir_dict = {0: "E", 90: "N", 180: "W", 270: "S"}
dir_fact = {"E": 1, "N": 1, "W": -1, "S": -1}
dir_map = {"E": "E", "N": "N", "W": "E", "S": "N"}

dir = 0

for line in lines:
    c = line[0]
    d = int(line[1:])
    if c == "R":
        dir = (dir - d) % 360
        continue
    if c == "L":
        dir = (dir + d) % 360
        continue
    if c == "F":
        pos[dir_map[dir_dict[dir]]] = (
            pos[dir_map[dir_dict[dir]]] + dir_fact[dir_dict[dir]] * d
        )
        continue
    pos[dir_map[c]] = pos[dir_map[c]] + dir_fact[c] * d

print(pos["E"], pos["N"])


from copy import deepcopy

pos = {"E": 0, "N": 0}
waypoint_pos = {"E": 10, "N": 1}
dir_dict = {0: "E", 90: "N", 180: "W", 270: "S"}
dir_fact = {"E": 1, "N": 1, "W": -1, "S": -1}
dir_map = {"E": "E", "N": "N", "W": "E", "S": "N"}

dir = 0


def rotate_right(waypoint, times):
    for i in range(times):
        new_waypoint = deepcopy(waypoint_pos)
        new_waypoint["E"] = waypoint["N"]
        new_waypoint["N"] = -waypoint["E"]
        waypoint = new_waypoint
    return waypoint


def rotate_left(waypoint, times):
    print(times)
    for i in range(times):
        new_waypoint = deepcopy(waypoint_pos)
        new_waypoint["E"] = -waypoint["N"]
        new_waypoint["N"] = waypoint["E"]
        waypoint = new_waypoint
    return waypoint


for line in lines:
    c = line[0]
    d = int(line[1:])
    if c == "R":
        waypoint_pos = rotate_right(waypoint_pos, 4 * d / 360)
    elif c == "L":
        waypoint_pos = rotate_left(waypoint_pos, 4 * d / 360)
    elif c == "F":
        pos["E"] += waypoint_pos["E"] * d
        pos["N"] += waypoint_pos["N"] * d
    else:
        waypoint_pos[dir_map[c]] = waypoint_pos[dir_map[c]] + dir_fact[c] * d

    print(line.strip(), waypoint_pos, pos)

print(pos["E"], pos["N"])
