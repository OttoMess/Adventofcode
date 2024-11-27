import time

EXAMPLE = "AoC_inputs/2022/day_5_example.txt"
INPUT = "AoC_inputs/2022/day_5.txt"


class puzzle5:
    def __init__(self, path):
        self.file_path = path
        self.stacks_raw = list()  # direct txt input into list with str format
        self.moves = list()  # list to collect the moves needed in str format
        self.stacks = list()  # each stack position will have it's own list to represent the stack on than position

        start_time = time.time()
        print(self.file_path)
        self.read_txt()
        self.stack_arrays()

        part1 = self.move_crates_onebyone()
        print(f"output part one: {self.find_message(part1)}")

        part2 = self.move_crates_in_bulk()
        print(f"output part two: {self.find_message(part2)}")

        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        raw_stack = list()
        raw_moves = list()

        with open(self.file_path) as file:
            for line in file:
                # sorting the information with the begin stacks from the moves needed to be made
                if "move" in line:
                    raw_moves.append(line.strip())
                else:
                    raw_stack.append(
                        line
                    )  # can not be stripped, will lose info which letter from which stack

        self.moves = raw_moves
        raw_stack.pop()
        self.stacks_raw = raw_stack

    def stack_arrays(self):
        # finding the index where the letters and number are located in the raw strings
        # the numbers are located at the same spot in the line string as the letters this is used
        index = [i for i, str in enumerate(self.stacks_raw[-1]) if str.isnumeric()]

        # making x number list to hold the stacks
        self.stacks = [list() for idx in index]

        for line in self.stacks_raw[:-1]:
            for j, idx in enumerate(index):
                if line[idx] != " ":
                    if len(self.stacks[j]) == 0:
                        self.stacks[j].append(line[idx])
                    else:
                        self.stacks[j].insert(0, line[idx])

    def move_crates_onebyone(self):  # part one
        cache = [i[:] for i in self.stacks]
        for move in self.moves:
            numbers = [int(s) for s in move.split() if s.isnumeric()]
            amount = numbers[0]
            from_loc = numbers[1] - 1  # compensate for count start at 0
            to_loc = numbers[2] - 1  # compensate for count start at 0

            for i in range(amount):
                cache[to_loc].append(cache[from_loc].pop())
        return cache

    def move_crates_in_bulk(self):
        cache = [i[:] for i in self.stacks]
        for move in self.moves:
            numbers = [int(s) for s in move.split() if s.isnumeric()]
            amount = numbers[0]
            from_loc = numbers[1] - 1  # compensate for count start at 0
            to_loc = numbers[2] - 1  # compensate for count start at 0

            temp_stack = list()
            for i in range(amount):
                temp_stack.append(cache[from_loc].pop())

            for _ in range(len(temp_stack)):
                cache[to_loc].append(temp_stack.pop())
        return cache

    def find_message(self, stacks):
        message = list()
        for pos in stacks:
            message.append(pos.pop())
        return "".join(message)


puzzle5(EXAMPLE)
puzzle5(INPUT)
