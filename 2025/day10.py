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
    def correct_joltage(machine, pressed):

        mutable = [0 for _ in machine.joltage]

        for but_loc, times in enumerate(pressed):
            if times == 0:
                continue

            button = machine.buttons[but_loc]
            for loc in button:
                mutable[loc] += 1 * times
                if mutable[loc] > machine.joltage[loc]:
                    return False

        if mutable == machine.joltage:
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

    def distribute(self, presses, n_buttons):

        if n_buttons == 1:
            return [[presses]]

        output = []
        for i in range(presses + 1):
            for rest in self.distribute(presses - i, n_buttons - 1):
                output.append([i] + rest)
        return output

    def part2(self) -> int:
        # TODO need different approach, this will not work for large set of combinations
        collector = []

        for machine in self.input:
            # print(machine)
            correct = False
            # n_pressed = 20

            q = self.distribute(2, 6)

            # TODO use index for button and amount of time pressed
            while correct is False:
                n_buttons = len(machine.buttons)
                combo = list(itertools.product(
                    range(n_pressed+1), repeat=n_buttons))

                combo.sort(key=lambda k: sum(k))

                for test in combo:
                    correct = self.correct_joltage(machine, test)
                    if correct:
                        collector.append(n_pressed)

                        break
                n_pressed += 1
                print(n_pressed)
        return sum(collector)


@dataclass
class machine:
    lights: list
    buttons: list
    joltage: list


Puzzle10(EXAMPLE)
Puzzle10(INPUT)
