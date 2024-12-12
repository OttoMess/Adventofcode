import time


EXAMPLE = "AoC_inputs/2024/day_11_example.txt"
INPUT = "AoC_inputs/2024/day_11.txt"


class Puzzle11:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)
        # self.read_txt()

        print(f"output part one: {len(self.part1())}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        with open(self.file_path) as file:
            for line in file:
                data = [int(i) for i in line.strip().split()]
        # data = [int(i) for i in line.strip().split()]
        return data

    def part1(self):
        stones = self.read_txt()
        for _ in range(25):
            stones = self.apply_rules(stones)
        return stones

    def part2(self):
        stones = self.part1()
        counter = 0
        i = 1
        loop_time = time.time()
        for stone in stones:  # build heap que ?
            stone = [stone]
            for i in range(25):
                stone = self.apply_rules(stone)
                for st in stone:
                    st = [st]
                    for i in range(25):
                        st = self.apply_rules(st)
                    counter += len(st)
            print(f"{i} done of {len(stones)} {round(time.time()-loop_time ,4)}")
        return len(stones)

    @staticmethod
    def rules(stone):
        stone_string = str(stone)
        if stone == 0:
            return [1]
        elif len(stone_string) % 2 == 0:
            mid = len(stone_string) // 2
            left = int(stone_string[:mid])
            right = int(stone_string[mid:])
            return [left, right]
        else:
            return [stone * 2024]

    @staticmethod
    def apply_rules(stones):
        new_stones = list()
        for stone in stones:
            new = Puzzle11.rules(stone)
            for i in new:
                new_stones.append(i)

        return new_stones


Puzzle11(EXAMPLE)
Puzzle11(INPUT)
