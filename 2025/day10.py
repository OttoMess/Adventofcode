from scipy.optimize import milp, LinearConstraint, Bounds, linprog
import numpy as np
import time
from dataclasses import dataclass
import itertools
import resource
import sys

EXAMPLE = "AoC_inputs/2025/day_10_example.txt"
INPUT = "AoC_inputs/2025/day_10.txt"


def memory_limit_half(ram_size_gb: int):
    """Limit max memory usage to half."""
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    # Convert Gb adn to KiB to bytes
    resource.setrlimit(resource.RLIMIT_AS, (ram_size_gb*1_000_000*1024, hard))


memory_limit_half(10)


class Puzzle10:
    def __init__(self, path) -> None:
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self) -> None:
        data = list()
        with open(self.file_path) as file:
            for line in file:
                part_1, part_b = line.split("]")

                lights = []
                for x in part_1:
                    if x == ".":
                        lights.append(0)
                    elif x == "#":
                        lights.append(1)

                col = part_b.strip().split("{")[0].strip().split()
                buttons = []
                for but in col:
                    red = []
                    for c in but:
                        if c.isdigit():
                            red.append(int(c))
                    buttons.append(red)

                joltage = [int(i)
                           for i in part_b.strip().split("{")[1][:-1].split(",")]

                data.append(
                    Machine(lights, buttons, joltage))

        self.input = data

    @staticmethod
    def correct_lights_on(lights, pressed):
        mutable = [0 for _ in lights]

        for press in pressed:
            for loc in press:
                mutable[loc] = (mutable[loc] + 1) % 2

        if mutable == lights:
            return True

        return False

    def part1(self) -> int:
        machine: Machine
        collector = []

        for machine in self.input:
            correct = False
            n_pressed = 1

            while correct is False:
                combo = itertools.combinations_with_replacement(
                    machine.buttons, n_pressed)

                for test in combo:
                    correct = self.correct_lights_on(machine.lights, test)
                    if correct:
                        collector.append(n_pressed)
                        break
                n_pressed += 1

        return sum(collector)

    def part2(self) -> int:
        # TODO need different approach, this will not work for large set of combinations
        collector = []
        machine: Machine

        col_2 = []

        for machine in self.input:
            # print(machine)
            # correct = False
            # minimal = max(machine.joltage)
            n_joltage = len(machine.joltage)
            # n_pressed = minimal
            n_buttons = len(machine.buttons)
            # q = self.distribute(2, 6)

            B = np.zeros((n_joltage, n_buttons), dtype=int)
            for i, button in enumerate(machine.buttons):
                for j in button:
                    B[j, i] = 1

            J = np.array(machine.joltage, dtype=int)

            c = np.ones(n_buttons, dtype=float)
            constraints = LinearConstraint(B, lb=J, ub=J)
            # bounds = Bounds(lb=np.zeros(n_buttons),
            #                 ub=np.full(n_buttons, np.inf))
            integrality = np.ones(n_buttons, dtype=int)  # bool is also fine

            # result = milp(c=c, constraints=constraints,
            #               bounds=bounds, integrality=integrality)

            result = milp(c=c, constraints=constraints,
                          integrality=integrality)

            # e = linprog(c=c, constraints=constraints,
            #             bounds=bounds, integrality=integrality)

            if not result.success:
                raise ValueError("No solution found")

            a = result.x.astype(int)
            b = np.rint(result.x).astype(int)

            compare = a == b
            if c.any() == False in compare:
                print('stop')

            collector.append(a)
            col_2.append(b)

        return sum([sum(x)for x in collector])


@dataclass
class Machine:
    lights: list
    buttons: list
    joltage: list


# Puzzle10(EXAMPLE)
Puzzle10(INPUT)
# 17967 to low
# 17983 to low
