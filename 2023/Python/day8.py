import time
import math

EXAMPLE = "2023/data/day8_example.txt"
DATA = "2023/data/day8.txt"
TEST = "2023/data/day8_test.txt"
TEST2 = "2023/data/day8_test2.txt"


class Puzzle8:

    def __init__(self,file_path):
        self.steps_2 = None
        self.starting_keys = None
        self.data = None
        self.file_path = file_path
        self.instructions = None
        self.map = None
        self.steps = None

        start_time = time.time()
        self.read_txt()
        self.part1()
        self.part2_v2()
        print(file_path)
        print(f"Number of steps part 1 {self.steps}")
        print(f"Number of steps part 2 {self.steps_2}")
        print(f"Run time {round(time.time()-start_time,4)} [sec]\n")

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for j, line in enumerate(file):
                if j == 0:
                    self.instructions = line.strip()
                elif j > 1:
                    raw.append(line.strip())
        data = [i.split("=") for i in raw]
        keys = [i[0].strip() for i in data]
        
        self.starting_keys = [i for i in keys if i.endswith("A")]
        
        m = [i[1] for i in data]
        m = [i.replace(" (","").replace(")", "") for i in m]
        map_data = [i.split(", ") for i in m]
        self.map = dict()
        for j, _ in enumerate(map_data):
            self.map[keys[j]] = map_data[j]

    def part1(self):
        loop = len(self.instructions)
        run = True
        step = 1
        indexer = 0
        current_key = "AAA"
        next_key = None
        while run:

            instruction = self.instructions[indexer]
            if instruction == "R":
                next_key = self.map[current_key][1]
            elif instruction == "L":
                next_key = self.map[current_key][0]

            if next_key == "ZZZ":
                # run = False
                break
            else:
                current_key = next_key

            if step % loop == 0:
                indexer = 0  # resetting de indexed based on the lenght of the instruction set
                # print(step, current_key)
            else:
                indexer += 1
            step += 1

            if step % int(1e7) == 0:
                print(step)

        self.steps = step

    def part2(self):
        loop = len(self.instructions)
        run = True
        step = 1
        # step = 3000000
        # indexer = int(199)
        # last run
        # 1357000000 ['NKP', 'TSS', 'LTV', 'SXG', 'RQJ', 'MTK'] 0
        indexer = 0
        current_keys = self.starting_keys
        # current_keys = ['LJP', 'LDS', 'PNS', 'LKM', 'RRS', 'BBB']
        next_keys = [str() for _ in current_keys]
        print(step, current_keys, indexer)
        while run:
            if step % int(1e6) == 0:
                print(step, current_keys, indexer)
            # print(loop, self.instructions)
            instruction = self.instructions[indexer]

            for j, k in enumerate(current_keys):

                if instruction == "R":
                    next_keys[j] = self.map[k][1]
                elif instruction == "L":
                    next_keys[j] = self.map[k][0]

            if all(i.endswith("Z") for i in next_keys):
                break
            else:
                current_keys = next_keys

            if step % loop == 0:
                indexer = 0  # resetting de indexed based on the lenght of the instruction set
            else:
                indexer += 1
            step += 1

        self.steps_2 = step

    def part2_v2(self):
        loop = len(self.instructions)
        current_keys = self.starting_keys
        loop_lenght = list()
        for ke in current_keys:
            indexer = 0
            run = True
            step = 1
            next_key = str()
            current = ke
            while run:
                if step % int(1e6) == 0:
                    print(step, current, indexer)

                instruction = self.instructions[indexer]

                if instruction == "R":
                    next_key = self.map[current][1]
                elif instruction == "L":
                    next_key = self.map[current][0]

                if next_key.endswith("Z"):
                    loop_lenght.append(step)
                    break
                else:
                    current = next_key

                if step % loop == 0:
                    indexer = 0  # resetting de indexed based on the lenght of the instruction set
                else:
                    indexer += 1
                step += 1
        print(loop_lenght)
        self.steps_2 = math.lcm(*loop_lenght)


# Puzzle8(TEST2)
Puzzle8(EXAMPLE)
# Puzzle8(TEST)
Puzzle8(DATA)
