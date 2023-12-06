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
        self.searcher()

        self.part2()
        # print("test")

    def part2(self):
        seeds = self.range_build_seeds()
        collector = 1e60
        for i in seeds["range"]:
            print(i)
            for j in i:
                temp = self.searcher_seeds(j)
                if temp < collector:
                    collector = temp

        print(f"Output of part 2 = {collector}")

    def range_build_seeds(self):
        seeds = self.seeds
        begin = list()
        end = list()
        ran = list()
        b = int()
        for j, i in enumerate(seeds):
            if j % 2 == 0:
                b = i
                begin.append(i)
            else:
                e = seeds[j-1] + i
                end.append(e)
                ran.append(range(b, e))
        output = {"begin": begin, "end": end, "range": ran}
        return output

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
        self.soil_to_fertilizer = self.range_builder(soil_fer)
        self.fertilizer_to_water = self.range_builder(fer_water)
        self.water_to_light = self.range_builder(water_light)
        self.light_to_temperature = self.range_builder(light_temp)
        self.temperature_to_humidity = self.range_builder(temp_hum)
        self.humidity_to_location = self.range_builder(hum_location)

    def range_builder(self, table):
        data = self.data
        source = list()
        destination = list()
        lenght = list()
        offset = list()
        for i in range(table[0], table[1]+1):
            de, so, le = map(int, data[i].split(" "))
            of = de - so

            source.append(so)
            destination.append(de)
            lenght.append(le)
            offset.append(of)
        output = {'source': source,
                  "destination": destination,
                  "lenght": lenght,
                  "offset": offset}

        return output

    @staticmethod
    def finder(to_find, data):
        output = list()
        for i in to_find:
            found = False
            for j, _ in enumerate(data["source"]):
                ran = [data["source"][j], data["source"][j] + data["lenght"][j]-1]
                ran.sort()
                if ran[0] <= i <= ran[1]:
                    output.append(i + data["offset"][j])
                    found = True
            if not found:
                output.append(i)
        return output

    @staticmethod
    def finder_single(to_find, data):
        output = int()
        found = False
        for j, _ in enumerate(data["source"]):
            ran = [data["source"][j], data["source"][j] + data["lenght"][j]-1]
            ran.sort()
            if ran[0] <= to_find <= ran[1]:
                output = to_find + data["offset"][j]
                found = True
        if not found:
            output = to_find
        return output

    def searcher(self):
        soils = self.finder(self.seeds, self.seeds_to_soil)
        fertilizer = self.finder(soils, self.soil_to_fertilizer)
        water = self.finder(fertilizer, self.fertilizer_to_water)
        light = self.finder(water, self.water_to_light)
        temperature = self.finder(light, self.light_to_temperature)
        humidity = self.finder(temperature, self.temperature_to_humidity)
        location = self.finder(humidity, self.humidity_to_location)
        print(f"output part 1 = {min(location)}")

    def searcher_seeds(self, seeds):
        soils = self.finder_single(seeds, self.seeds_to_soil)
        fertilizer = self.finder_single(soils, self.soil_to_fertilizer)
        water = self.finder_single(fertilizer, self.fertilizer_to_water)
        light = self.finder_single(water, self.water_to_light)
        temperature = self.finder_single(light, self.light_to_temperature)
        humidity = self.finder_single(temperature, self.temperature_to_humidity)
        location = self.finder_single(humidity, self.humidity_to_location)
        return location


# Puzzle5(EXAMPLE)
Puzzle5(DATA)
