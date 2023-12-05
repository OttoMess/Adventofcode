EXAMPLE = "Data/Puzzle_#3_example.txt"
DATA = "Data/Puzzle_#3.txt"
TEST = "Data/Puzzle_#3_test.txt"
TEST2 = "Data/Puzzle_#3_test2.txt"


class Puzzle3:

    def __init__(self, file_path):
        # defining the variables used
        self.data_len = int()
        self.data_list = list()
        self.sum = int()
        self.collector = 0
        self.collector_2 = 0
        self.file_path = file_path
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.numbers = [str(n) for n in numbers]
        self.non_symbol = self.numbers
        self.non_symbol.append(".")

        # calling the functions
        self.read_txt()
        self.part1()
        print(f"Output part1: {self.collector}")

        self.part2()
        print(f"Output part2: {self.collector_2}")

    def read_txt(self):
        with open(self.file_path) as file:
            for line in file:
                # self.data_list.append(line.replace("\n", ""))
                self.data_list.append(line.strip())
        self.data_len = len(self.data_list)

    def compare(self, list1, list2):
        for val in list1:
            if val in list2:
                return True
        return False

    def find_number_info(self, data):
        for j, c in enumerate(data):
            if c not in self.non_symbol:
                data = data.replace(c, ".")

        numbers = [c for c in data.split(".") if c.isdigit()]

        loc = list()
        for n in numbers:
            dummy = str()
            for _ in n:
                dummy += "."
            loc.append(data.find(n))
            data = data.replace(n, dummy, 1)

        loc_num = list()
        for j, n in enumerate(numbers):
            temp = list()
            for i in range(len(n)):
                temp.append(int(loc[j]) + i)
            loc_num.append(temp)
        return numbers, loc_num

    def find_ch_in_str(self,s,ch):
            return [i for i, ltr in enumerate(s) if ltr == ch]

    def find_symbol_info(self, data: list):
        loc_sym = list()
        for d in data:
            symbol = [c for c in d if c not in self.non_symbol]
            loc = list()
            for s in set(symbol):
                for j, c in enumerate(d):
                    if c == s:
                        loc.append(j)

            for j, s in enumerate(symbol):
                if loc[j] == 0:
                    loc_sym.append(loc[j])
                    loc_sym.append(loc[j] + 1)
                elif loc[j] == len(d)-1:
                    loc_sym.append(loc[j] - 1)
                    loc_sym.append(loc[j])
                else:
                    loc_sym.append(loc[j] - 1)
                    loc_sym.append(loc[j])
                    loc_sym.append(loc[j] + 1)

        return loc_sym

    def part1(self):
        for i in range(self.data_len):
            numbers, number_location = self.find_number_info(self.data_list[i])
            # print(self.data_list[i])
            if i == 0:
                symbol_locations = self.find_symbol_info(
                    [self.data_list[i],
                     self.data_list[i+1]])
            elif i == self.data_len - 1:
                symbol_locations = self.find_symbol_info(
                    [self.data_list[i-1],
                     self.data_list[i]])
            else:
                symbol_locations = self.find_symbol_info(
                    [self.data_list[i-1],
                     self.data_list[i],
                     self.data_list[i+1]])

            for j, k in enumerate(numbers):
                if self.compare(number_location[j], symbol_locations):
                    self.collector += int(numbers[j])
                    # print(f"added {int(numbers[j])}")
                else:
                    continue

    def find_gears(self, data):
        gear = [c for c in data if c == "*"]
        loc = list()
        for g in gear:
            loc.append(data.find(g))
            data = data.replace(g, ".", 1)
        r = list()
        for i in loc:
            loc_extend = list()
            if i == 0:
                loc_extend.append(i)
                loc_extend.append(i+1)
            elif i == len(data)-1:
                loc_extend.append(i-1)
                loc_extend.append(i)
            else:
                loc_extend.append(i-1)
                loc_extend.append(i)
                loc_extend.append(i+1)
            r.append(loc_extend)
        return r

    def part2(self):
        for i in range(self.data_len):
            data = self.data_list[i]
            print(self.data_list[i])
            gears = self.find_gears(self.data_list[i])
            if len(gears) == 0:
                continue

            if i == 0:
                n, l = self.find_number_info(self.data_list[i])
                nn, ll = self.find_number_info(self.data_list[i+1])
                num = n + nn
                loc = l + ll
                del l, ll, n, nn
            elif i == self.data_len - 1:
                n, l = self.find_number_info(self.data_list[i])
                nn, ll = self.find_number_info(self.data_list[i - 1])
                num = n + nn
                loc = l + ll
                del l, ll, n, nn
            else:
                n, l = self.find_number_info(self.data_list[i])
                nn, ll = self.find_number_info(self.data_list[i - 1])
                nnn, lll = self.find_number_info(self.data_list[i + 1])
                num = n + nn + nnn
                loc = l + ll + lll
                del l, ll, lll, n, nn, nnn

            for g in gears:
                temp = list()
                for j, l in enumerate(loc):
                    if self.compare(l,g):
                        temp.append(num[j])
                if len(temp) == 2:
                    self.collector_2 += int(temp[0]) * int(temp[1])


# Puzzle3(TEST)
# Puzzle3(EXAMPLE)
# Puzzle3(TEST2)
Puzzle3(DATA)
