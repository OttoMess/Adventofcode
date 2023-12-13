import time

EXAMPLE = "data/day6_example.txt"
DATA = "data/day6.txt"


class Puzzle6:

    def __init__(self, path):
        self.data = list()
        self.time = None
        self.distance = None

        self.file_path = path
        self.collector_1 = 1
        self.collector_2 = 0
        self.collector_3 = 0
        self.collector_4 = 0

        self.read_txt()
        self.find_time_distance_part1()
        self.part1()
        print(f"Output part 1 : {self.collector_1}")
        self.find_time_distance_part2()
        self.part2()

        print(f"Output part 2 : {self.collector_2}")
        print(f"Output part 2 with V2: {self.collector_3}")
        print(f"Output part 2 with V3: {self.collector_4}")

    def read_txt(self):
        with open(self.file_path) as file:
            for line in file:
                self.data.append(line.strip())

    def find_time_distance_part2(self):
        data = self.data
        time_str = data[0].split(":")[1].strip().split(" ")
        self.time = int("".join(c for c in time_str if c.isdigit()))

        distance_str = data[1].split(":")[1].strip().split(" ")
        self.distance = int("".join(c for c in distance_str if c.isdigit()))

    def find_time_distance_part1(self):
        data = self.data
        time_str = data[0].split(":")[1].strip().split(" ")
        self.time = [int(c) for c in time_str if c.isdigit()]

        distance_str = data[1].split(":")[1].strip().split(" ")
        self.distance = [int(c) for c in distance_str if c.isdigit()]

    @staticmethod
    def travelled(play_time, record):
        distance = [0 for _ in range(play_time+1)]
        for i in range(play_time+1):
            press = i
            speed = press
            travel_time = play_time - press
            distance[i] = speed * travel_time

        above_record = [j for j in distance if j > record]
        amount = len(above_record)

        return distance, amount

    @staticmethod
    def travelled_v2(play_time, record):
        above_record = 0
        for i in range(play_time+1):
            travel_time = play_time - i
            distance = i * travel_time
            if distance > record:
                above_record += 1

        return above_record

    @staticmethod
    def travelled_v3(play_time, record):
        below_record = list()
        for i in range(play_time+1):
            travel_time = play_time - i
            distance = i * travel_time
            if distance > record:
                below_record.append(i)
                break

        for j in range(play_time+1,0,-1):
            travel_time = play_time - j
            distance = j * travel_time
            if distance > record:
                below_record.append(j+1)
                break

        return below_record[1] - below_record[0]

    def part1(self):
        for j, _ in enumerate(self.time):
            _, f = self.travelled(self.time[j], self.distance[j])
            self.collector_1 *= f

    def part2(self):
        start_time = time.time()
        _, self.collector_2 = self.travelled(self.time, self.distance)
        print(f"Part 2 took : {round(time.time()-start_time,4)} [sec]")

        start_time = time.time()
        self.collector_3 = self.travelled_v2(self.time, self.distance)
        print(f"Part 2 V2 took : {round(time.time()-start_time,4)} [sec]")

        start_time = time.time()
        self.collector_4 = self.travelled_v3(self.time, self.distance)
        print(f"Part 2 V3 took : {round(time.time()-start_time,4)} [sec]")


Puzzle6(EXAMPLE)
Puzzle6(DATA)
