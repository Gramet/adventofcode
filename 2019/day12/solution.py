import re
from math import lcm
from pathlib import Path


class Planet:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def update_velocity(self, planet):
        if self.x < planet.x:
            self.vx += 1
        elif self.x > planet.x:
            self.vx -= 1

        if self.y < planet.y:
            self.vy += 1
        elif self.y > planet.y:
            self.vy -= 1

        if self.z < planet.z:
            self.vz += 1
        elif self.z > planet.z:
            self.vz -= 1

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def energy(self):
        pot = abs(self.x) + abs(self.y) + abs(self.z)
        kin = abs(self.vx) + abs(self.vy) + abs(self.vz)
        return pot * kin

    def __repr__(self) -> str:
        return f"pos=<x={self.x}, y={self.y}, z={self.z}>, vel=<x={self.vx}, y={self.vy}, z={self.vz}>\n"
        pass


class Solution:
    def __init__(self):
        with open(Path(__file__).parent / "input", "r") as f:
            self.input = f.readlines()

        self.planets = []
        for line in self.input:
            result = re.search(r".+(=-?\d+).+(=-?\d+).+(=-?\d+)", line)
            planet = Planet(
                result.group(1)[1:], result.group(2)[1:], result.group(3)[1:]
            )
            self.planets.append(planet)

    def solve_part_1(self):
        for _ in range(1000):
            for planet in self.planets:
                for planet2 in self.planets:
                    planet.update_velocity(planet2)

            for planet in self.planets:
                planet.apply_velocity()

        answer = sum(planet.energy() for planet in self.planets)
        print(answer)
        return answer

    def solve_part_2(self):
        self.planets = []
        for line in self.input:
            result = re.search(r".+(=-?\d+).+(=-?\d+).+(=-?\d+)", line)
            planet = Planet(
                result.group(1)[1:], result.group(2)[1:], result.group(3)[1:]
            )
            self.planets.append(planet)

        x_period = 0
        y_period = 0
        z_period = 0
        count = 0
        seen_x = set([tuple(((planet.x, planet.vx) for planet in self.planets))])
        seen_y = set([tuple(((planet.y, planet.vy) for planet in self.planets))])
        seen_z = set([tuple(((planet.z, planet.vz) for planet in self.planets))])
        while True:
            count += 1
            for planet in self.planets:
                for planet2 in self.planets:
                    planet.update_velocity(planet2)

            for planet in self.planets:
                planet.apply_velocity()

            pos_x = tuple(((planet.x, planet.vx) for planet in self.planets))
            pos_y = tuple(((planet.y, planet.vy) for planet in self.planets))
            pos_z = tuple(((planet.z, planet.vz) for planet in self.planets))
            if pos_x in seen_x and x_period == 0:
                x_period = count
                print("x", x_period)
            if pos_y in seen_y and y_period == 0:
                y_period = count
                print("y", y_period)
            if pos_z in seen_z and z_period == 0:
                z_period = count
                print("z", z_period)
            if x_period and y_period and z_period:
                break
            seen_x.add(pos_x)
            seen_y.add(pos_y)
            seen_z.add(pos_z)

        answer = lcm(x_period, y_period, z_period)
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
