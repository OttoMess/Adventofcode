import time

EXAMPLE = "Data/Puzzle_#7_example.txt"
DATA = "Data/Puzzle_#7.txt"
TEST = "Data/Puzzle_#7_test.txt"
TEST2 = "Data/Puzzle_#7_test2.txt"


class Puzzle7:

    def __init__(self, path):
        self.plays = None
        self.data = list()
        self.time = None
        self.distance = None

        self.file_path = path
        self.collector_1 = 1
        self.collector_2 = 0
        self.collector_3 = 0
        self.collector_4 = 0

        self.read_txt()
        self.sort_hands()
        # print("test")
 
    def read_txt(self):
        with open(self.file_path) as file:
            for line in file:
                self.data.append(line.strip())
        data = [i.split(" ") for i in self.data]
        hands = [i[0] for i in data]
        bids = [i[1] for i in data]
        self.plays = dict()
        for j, _ in enumerate(hands):
            self.plays[hands[j]] = bids[j]
        
    def sort_hands(self):
        hands = list(self.plays.keys())
        five_of_a_kind = list()
        four_of_a_kind = list()
        full_house = list()
        Three_of_a_kind = list()
        two_pairs = list()
        pair = list()
        high_card = list()
        for i in range(len(hands)-1):
            current = hands[i]
            current_set = set(current)
            if len(current_set) == 1:
                five_of_a_kind.append(current)
            elif len(current_set) == 2:
                for c in current_set:
                    reg = current.count(c)



Puzzle7(TEST)
