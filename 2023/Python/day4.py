EXAMPLE = "2023/data/day4_example.txt"
DATA = "2023/data/day4.txt"


class Puzzle4:

    def __init__(self, file_path):
        # defining the variables used
        self.data_len = int()
        self.data_list = list()
        self.file_path = file_path
        self.card_id = list()
        self.win_num = list()
        self.play_num = list()
        self.collector = 0

        self.card_count = list()
        # calling the functions
        self.read_txt()
        self.split_data()
        self.find_points_part1()
        self.find_points_part2()
        print(f"Output part1: {self.collector}")

        print(f"Output part2: {sum(self.card_count)}")

    def read_txt(self):
        with open(self.file_path) as file:
            for line in file:
                self.data_list.append(line.replace("\n", ""))
        self.data_len = len(self.data_list)

    def split_data(self):
        temp = [card.split(":") for card in self.data_list]
        self.card_id = [c[0] for c in temp]
        temp_num = [c[1] for c in temp]
        self.win_num = [c.split("|")[0].split(" ") for c in temp_num]
        self.play_num = [c.split("|")[1].split(" ") for c in temp_num]

        for j, _ in enumerate(self.card_id):
            self.win_num[j] = [c for c in self.win_num[j] if c.isdigit()]
            self.play_num[j] = [c for c in self.play_num[j] if c.isdigit()]

        self.card_count = [1] * self.data_len

    def find_points_part1(self):
        for j, _ in enumerate(self.card_id):
            temp = 0
            for n in self.win_num[j]:
                if n in self.play_num[j]:
                    if temp == 0:
                        temp = 1
                    else:
                        temp = temp * 2
            self.collector += temp
            # print(self.card_id[j], temp)

    def find_points_part2(self):
        for j, _ in enumerate(self.card_id):
            temp = 0
            for n in self.win_num[j]:
                if n in self.play_num[j]:
                    temp += 1
            count = self.card_count[j]
            if temp == 0:
                continue
            else:
                for i in range(1,temp+1):
                    self.card_count[j+i] += 1 * count

        # print(self.card_count)


Puzzle4(EXAMPLE)
Puzzle4(DATA)
