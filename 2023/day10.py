import time

DATA = "data/day10.txt"
EXAMPLE = "data/day10_example.txt"


class Puzzle10:

    def __init__(self, file_path):
        self.data = list()
        self.file_path = file_path
        self.start = list()

        self.part1_collector = 0
        self.part2_collector = 0

        self.lookup = {"|": ['up', 'down'],
                       "-": ['left','right'],
                       "L": ['up','right'],
                       "J": ['left','up'],
                       "7": ['left','down'],
                       "F": ['down','right'],
                       ".": ["no tube"],
                       "S": "start"}

        start_time = time.time()
        self.read_txt()
        self.part1()
        # self.part2()
        print(file_path)
        print(f"Sum for part 1: {self.part1_collector}")
        print(f"Number of steps part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
        self.data = raw

    def part1(self):
        self.start = self.find_start()
        self.tubes_connected_start()
        print(self.start)

    def find_start(self):
        data = self.data
        for i in data:
            for c in i:
                if c == "S":
                    return [data.index(i), i.find(c)]

    def tubes_connected_start(self):
        print("test")
        data = self.data
        start = self.start
        lookup = self.lookup
        connected = list()

        for i in range(4):
            if i == 0:
                row = start[0]-1
                col = start[1]
                tube = data[row][col]
                if "down" in lookup[tube]:
                    connected.append([row,col])

            if i == 1:
                row = start[0]+1
                col = start[1]
                tube = data[row][col]
                if "up" in lookup[tube]:
                    connected.append([row,col])

            if i == 2:
                row = start[0]
                col = start[1]-1
                tube = data[row][col]
                if "right" in lookup[tube]:
                    connected.append([row,col])

            if i == 3:
                row = start[0]
                col = start[1]+1
                tube = data[row][col]
                if "left" in lookup[tube]:
                    connected.append([row,col])

        print("test")




Puzzle10(EXAMPLE)
