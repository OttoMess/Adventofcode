EXAMPLE = "Data/Puzzle_#5_example.txt"
DATA = "Data/Puzzle_#5.txt"
TEST = "Data/Puzzle_#5_test.txt"
TEST2 = "Data/Puzzle_#5_test2.txt"


class Puzzle5:

    def __init__(self, path):
        self.data = list()
        self.seeds = list()

        self.seeds_to_soil = None
        self.soil_to_fertilizer = None
        self.fertilizer_to_water = None
        self.water_to_light = None
        self.light_to_temperature = None
        self.temperature_to_humidity = None
        self.humidity_to_location = None

        self.file_path = path

        self.read_txt()
        self.extract_data()
        # self.searcher()
        # print("test")

    def read_txt(self):
        with open(self.file_path) as file:
            for line in file:
                self.data.append(line.strip())

    def extract_data(self):
        seeds = self.data[0].split(":")[1].strip()
        data = self.data
        self.seeds = [int(c) for c in seeds.split(" ")]

        seed_soil = [i+1 for i, _ in enumerate(data) if _ == "seed-to-soil map:"]
        soil_fer = [i+1 for i, _ in enumerate(data) if _ == "soil-to-fertilizer map:"]
        fer_water = [i+1 for i, _ in enumerate(data) if _ == "fertilizer-to-water map:"]
        water_light = [i+1 for i, _ in enumerate(data) if _ == "water-to-light map:"]
        light_temp = [i+1 for i, _ in enumerate(data) if _ == "light-to-temperature map:"]
        temp_hum = [i+1 for i, _ in enumerate(data) if _ == "temperature-to-humidity map:"]
        hum_location = [i+1 for i, _ in enumerate(data) if _ == "humidity-to-location map:"]

        seed_soil.append(soil_fer[0]-3)
        soil_fer.append(fer_water[0] - 3)
        fer_water.append(water_light[0]-3)
        water_light.append(light_temp[0]-3)
        light_temp.append(temp_hum[0]-3)
        temp_hum.append(hum_location[0]-3)
        hum_location.append(len(data)-1)
        # print("test")

        self.seeds_to_soil = self.range_builder(seed_soil)

        soils = self.finder(self.seeds,self.seeds_to_soil)
        # fertilizer = self.finder(soils,self.soil_to_fertilizer)
        # water = self.finder(fertilizer, self.fertilizer_to_water)
        # light = self.finder(water, self.water_to_light)
        # temperature = self.finder(light, self.light_to_temperature)
        # humidity = self.finder(temperature, self.temperature_to_humidity)
        # location = self.finder(humidity, self.humidity_to_location)
        # print(f"output part 1 = {min(location)}")
        #
        # self.soil_to_fertilizer = self.range_builder(soil_fer)
        # self.fertilizer_to_water = self.range_builder(fer_water)
        # self.water_to_light = self.range_builder(water_light)
        # self.light_to_temperature = self.range_builder(light_temp)
        # self.temperature_to_humidity = self.range_builder(temp_hum)
        # self.humidity_to_location = self.range_builder(hum_location)

    def range_builder(self,table):
        data = self.data
        output = dict()
        for i in range(table[0],table[1]+1):
            destination, source, lenght = map(int,data[i].split(" "))

            for j in range(lenght):
                output[source+j] = destination+j

        return output

    def finder(self,to_find,data):
        output = list()
        for i in to_find:
            if i in data.keys():
                output.append(data[i])
            else:
                output.append(i)
        return output

    def searcher(self):
        soils = self.finder(self.seeds,self.seeds_to_soil)
        fertilizer = self.finder(soils,self.soil_to_fertilizer)
        water = self.finder(fertilizer, self.fertilizer_to_water)
        light = self.finder(water, self.water_to_light)
        temperature = self.finder(light, self.light_to_temperature)
        humidity = self.finder(temperature, self.temperature_to_humidity)
        location = self.finder(humidity, self.humidity_to_location)
        print(f"output part 1 = {min(location)}")


# Puzzle5(EXAMPLE)
Puzzle5(DATA)
