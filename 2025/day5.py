import time

EXAMPLE = "AoC_inputs/2025/day_5_example.txt"
INPUT = "AoC_inputs/2025/day_5.txt"


class Puzzle5:
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
        data = list()
        fresh = list()
        ingredients = list()
        with open(self.file_path) as file:
            next = False
            for line in file:
                if line.strip() == "":
                    next = True
                    continue
                if next:
                    ingredients.append(int(line.strip()))
                else:
                    fresh.append(tuple([int(i)
                                 for i in line.strip().split("-")]))

        self.fresh = tuple(fresh)
        self.ingredients = tuple(ingredients)

    def part1(self):
        counter = 0
        for ingredient in self.ingredients:
            for start, end in self.fresh:
                if ingredient >= start and ingredient <= end:
                    counter += 1
                    break
        return counter

    def part2(self):
        # sorting the ranges was the key to make is simple
        intervals = list(sorted(self.fresh))

        section = list(intervals[0])
        counter = 0
        for i in range(1, len(intervals)):
            current = intervals[i]

            # If current interval overlaps with the last merged
            # interval, merge them
            if current[0] <= section[1]:
                section[1] = max(section[1], current[1])
            else:
                counter += section[1] - section[0] + 1
                section = list(current)

        counter += section[1] - section[0] + 1  # add last section
        return counter


Puzzle5(EXAMPLE)
Puzzle5(INPUT)
