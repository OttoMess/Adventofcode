import time

EXAMPLE = "AoC_inputs/2024/day_11_example.txt"
INPUT = "AoC_inputs/2024/day_11.txt"


class Puzzle11:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)

        answer = self.part1and2()
        print(f"output part one: {next(answer)}")
        print(f"output part two: {next(answer)}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        with open(self.file_path) as file:
            for line in file:
                data = [int(i) for i in line.strip().split()]
        return data

    def part1and2(self):
        stones = self.read_txt()
        stones_count = {stone: 1 for stone in stones}
        for i in range(75):
            if i == 25:
                yield sum(stones_count.values())
            stones_count = self.blink(stones_count)

        yield sum(stones_count.values())

    def blink(self, stones):
        new_stones = dict()
        for stone in stones.keys():
            blink_stones = self.rules(stone)
            for new in blink_stones:
                if new in new_stones.keys():
                    new_stones[new] += stones[stone]
                else:
                    new_stones[new] = stones[stone]
        return new_stones

    @staticmethod
    def rules(stone):
        if stone == 0:
            return [1]
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])
            return [left, right]
        else:
            return [stone * 2024]


Puzzle11(EXAMPLE)
Puzzle11(INPUT)
