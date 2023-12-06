EXAMPLE = "Data/Puzzle_#6_example.txt"
DATA = "Data/Puzzle_#6.txt"
TEST = "Data/Puzzle_#6_test.txt"
TEST2 = "Data/Puzzle_#6_test2.txt"


class Puzzle6:

    def __init__(self, path):
        self.data = list()
        self.time = list()
        self.distance = list()

        self.seeds_to_soil = None
        self.soil_to_fertilizer = None
        self.fertilizer_to_water = None
        self.water_to_light = None
        self.light_to_temperature = None
        self.temperature_to_humidity = None
        self.humidity_to_location = None

        self.file_path = path

        self.read_txt()
        self.find_time_distance()

        print("test")

    def read_txt(self):
        with open(self.file_path) as file:
            for line in file:
                self.data.append(line.strip())

    def find_time_distance(self):
        data = self.data
        time_str = data[0].split(":")[1].strip().split(" ")
        self.time = [int(c) for c in time_str if c.isdigit()]

        distance_str = data[1].split(":")[1].strip().split(" ")
        self.distance = [int(c) for c in distance_str if c.isdigit()]

        print("test")

Puzzle6(EXAMPLE)