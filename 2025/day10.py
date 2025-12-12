import time
from dataclasses import dataclass
import itertools


EXAMPLE = "AoC_inputs/2025/day_10_example.txt"
INPUT = "AoC_inputs/2025/day_10.txt"


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
                    machine(lights, buttons, joltage))

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

    @staticmethod
    def correct_joltage(joltage, pressed):

        mutable = [0 for _ in joltage]

        for press in pressed:
            for loc in press:
                mutable[loc] += 1
                if mutable[loc] < joltage[loc]:
                    return False

        if mutable == joltage:
            return True

        return False

    def part1(self) -> int:
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
        collector = []

        for machine in self.input:
            correct = False
            n_pressed = min(machine.joltage)

            while correct is False:
                combo = itertools.combinations_with_replacement(
                    machine.buttons, n_pressed)

                for test in combo:
                    correct = self.correct_joltage(machine.joltage, test)
                    if correct:
                        collector.append(n_pressed)
                        break
                n_pressed += 1
        return sum(collector)


@dataclass
class machine:
    lights: list
    buttons: list
    joltage: list


Puzzle10(EXAMPLE)
Puzzle10(INPUT)
