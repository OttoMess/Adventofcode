import time


EXAMPLE = "AoC_inputs/2024/day_25_example.txt"
INPUT = "AoC_inputs/2024/day_25.txt"


class Puzzle25:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        self.locks = list()
        self.keys = list()
        with open(self.file_path) as file:
            # removing the base of the lock and key
            key_collector = [-1, -1, -1, -1, -1]
            lock_collector = [-1, -1, -1, -1, -1]
            new_section = True

            for line in file:
                if new_section:
                    if "#####" in line:
                        lock = True
                        key = False
                        new_section = False
                    else:
                        lock = False
                        key = True
                        new_section = False

                if lock:
                    for i, c in enumerate(line):
                        if c == "#":
                            lock_collector[i] += 1
                elif key:
                    for i, c in enumerate(line):
                        if c == "#":
                            key_collector[i] += 1

                if line.strip() == "":
                    if lock:
                        self.locks.append(lock_collector)
                        lock_collector = [-1, -1, -1, -1, -1]
                    elif key:
                        self.keys.append(key_collector)
                        key_collector = [-1, -1, -1, -1, -1]
                    new_section = True

    def part1(self):
        collector = 0
        for lock in self.locks:
            for key in self.keys:
                if self.fits(lock, key):
                    collector += 1
        return collector

    def part2(self):
        return

    @staticmethod
    def fits(lock, key):
        for i in range(5):
            if lock[i] + key[i] > 5:
                return False
        return True


Puzzle25(EXAMPLE)
Puzzle25(INPUT)
