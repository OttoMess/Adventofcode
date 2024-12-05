import time


EXAMPLE = "AoC_inputs/2024/day_5_example.txt"
INPUT = "AoC_inputs/2024/day_5.txt"


class Puzzle5:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.order = list()
        self.manuals = list()

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        with open(self.file_path) as file:
            for line in file:
                if "|" in line:
                    self.order.append(line.strip().split("|"))
                elif "," in line:
                    self.manuals.append(line.strip().split(","))

    def valid_manual(self, manual):
        for i, _ in enumerate(manual):
            after = [order[1] for order in self.order if order[0] == manual[i]]
            for j in range(i + 1, len(manual)):
                e = manual[j]
                if not manual[j] in after:
                    return False, [i, j]
        return True, _

    @staticmethod
    def find_middle(manual):
        middle_index = int((len(manual) - 1) / 2)
        return int(manual[middle_index])

    def part1(self):
        middle_values = list()
        for manual in self.manuals:
            found, _ = self.valid_manual(manual)
            if found:
                middle_values.append(self.find_middle(manual))
        return sum(middle_values)

    def part2(self):
        middle_values = list()
        for manual in self.manuals:
            found, pages = self.valid_manual(manual)
            if not found:
                while not found:
                    manual[pages[0]], manual[pages[1]] = (
                        manual[pages[1]],
                        manual[pages[0]],
                    )
                    found, pages = self.valid_manual(manual)
                middle_values.append(self.find_middle(manual))
        return sum(middle_values)


Puzzle5(EXAMPLE)
Puzzle5(INPUT)
