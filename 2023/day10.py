import time

DATA = "data/day10.txt"
EXAMPLE = "data/day10_example.txt"
TEST = "data/day10_test.txt"


class Puzzle10:

    def __init__(self, file_path):
        self.remap = None
        self.path = None
        self.row_amount = None
        self.col_amount = None
        self.data = list()
        self.file_path = file_path
        self.start = list()

        self.part1_collector = 0
        self.part2_collector = 0

        self.lookup = {"|": ['║', 'up', 'down'],
                       "-": ['═', 'left', 'right'],
                       "L": ['╚', 'up', 'right'],
                       "J": ['╝', 'left', 'up'],
                       "7": ['╗', 'left', 'down'],
                       "F": ['╔', 'down', 'right'],
                       ".": ["no tube"],
                       "S": ['S', "up", "down", "left", "right"]}

        start_time = time.time()
        self.read_txt()
        self.part1()
        self.part2()
        print(file_path)
        print(f"Path lenght for part 1: {self.part1_collector}")
        print(f"Number of steps part 2: {self.part2_collector}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
        self.col_amount = len(raw[0])
        self.row_amount = len(raw)
        self.data = raw

    def part1(self):
        self.start = self.find_start()
        connected_start = self.tubes_connected_start()
        path_1 = [self.start, connected_start[0]]
        path_2 = [self.start, connected_start[1]]
        while True:
            e = self.adjacent_tube(path_1[-2], path_1[-1])
            if e == self.start:
                break
            else:
                path_1.append(e)
        while True:
            e = self.adjacent_tube(path_2[-2], path_2[-1])
            if e == self.start:
                break
            else:
                path_2.append(e)

        for j, _ in enumerate(path_1):
            if _ == self.start:
                self.path = [path_1, path_2]
                continue
            elif path_1[j] == path_2[j]:
                self.part1_collector = j
                break

    def part2(self):
        self.redraw()
        self.shoelace()

    def shoelace(self):
        lace = self.path[0]
        count = 0
        for j in range(len(lace)):
            x1 = lace[j][0]
            y1 = lace[j][1]
            if j == len(lace)-1:
                x2 = lace[0][0]
                y2 = lace[0][1]
            else:
                x2 = lace[j+1][0]
                y2 = lace[j+1][1]
            count += abs(x1 * y2) - abs(x2 * y1)

        count = int(count / 2)
        inner = abs(count) - (len(lace)/2 - 1)  # the -1 related to the fact there are 4 inward corner each 1/4
        print(inner)
        self.part2_collector = int(inner)

    def redraw(self):
        mapper = list()
        mapper.extend([["-" for _ in self.data[0]] for _ in self.data])
        for i in self.path[0]:
            symbol = self.data[i[0]][i[1]]
            mapper[i[0]][i[1]] = self.lookup[symbol][0]
        for i in mapper:
            string = "".join(_ for _ in i)
            print(string)
        self.remap = mapper

    def outsider(self, current):

        for i in range(4):
            if i == 0 and current[0] > 0:
                row = current[0] - 1
                col = current[1]
                tube = self.remap[row][col]
                if tube == "-":
                    self.remap[row][col] = "o"

            if i == 1 and current[0] < self.row_amount - 1:
                row = current[0] + 1
                col = current[1]
                tube = self.data[row][col]
                if tube == "-":
                    self.remap[row][col] = "o"

            if i == 2 and current[1] > 0:
                row = current[0]
                col = current[1] - 1
                tube = self.data[row][col]
                if tube == "-":
                    self.remap[row][col] = "o"

            if i == 3 and current[1] < self.col_amount - 1:
                row = current[0]
                col = current[1] + 1
                tube = self.data[row][col]
                if tube == "-":
                    self.remap[row][col] = "o"

    def find_start(self):
        data = self.data
        for i in data:
            for c in i:
                if c == "S":
                    return [data.index(i), i.find(c)]

    def adjacent_tube(self, previous: list, current: list):
        connections = self.lookup[self.data[current[0]][current[1]]]
        for i in range(4):
            if i == 0 and current[0] > 0:
                row = current[0] - 1
                col = current[1]
                tube = self.data[row][col]
                if [row, col] == previous:
                    continue
                elif "down" in self.lookup[tube] and "up" in connections:
                    next_tube = [row, col]
                    return next_tube

            if i == 1 and current[0] < self.row_amount-1:
                row = current[0] + 1
                col = current[1]
                tube = self.data[row][col]
                if [row, col] == previous:
                    continue
                elif "up" in self.lookup[tube] and "down" in connections:
                    next_tube = [row, col]
                    return next_tube

            if i == 2 and current[1] > 0:
                row = current[0]
                col = current[1] - 1
                tube = self.data[row][col]
                if [row, col] == previous:
                    continue
                elif "right" in self.lookup[tube] and "left" in connections:
                    next_tube = [row, col]
                    return next_tube

            if i == 3 and current[1] < self.col_amount-1:
                row = current[0]
                col = current[1] + 1
                tube = self.data[row][col]
                if [row, col] == previous:
                    continue
                elif "left" in self.lookup[tube] and "right" in connections:
                    next_tube = [row, col]
                    return next_tube

    def tubes_connected_start(self):
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
                    connected.append([row, col])

            if i == 1:
                row = start[0]+1
                col = start[1]
                tube = data[row][col]
                if "up" in lookup[tube]:
                    connected.append([row, col])

            if i == 2:
                row = start[0]
                col = start[1]-1
                tube = data[row][col]
                if "right" in lookup[tube]:
                    connected.append([row, col])

            if i == 3:
                row = start[0]
                col = start[1]+1
                tube = data[row][col]
                if "left" in lookup[tube]:
                    connected.append([row, col])

        return connected


Puzzle10(EXAMPLE)
# Puzzle10(TEST)
Puzzle10(DATA)
