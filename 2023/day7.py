import time
from dataclasses import dataclass

EXAMPLE = "data/day7_example.txt"
DATA = "data/day7.txt"
TEST = "data/day7_test.txt"

"""
A score will be build based on the type of hand and the card within the hand.
the score is a single number which than can be used to easily sort the hands played.

score = xaabbccddee
x= is 1 to 7 depending on the type 
aa,bb,cc,dd,ee = 1 to 13 based on the card type ('aa' first card 'ee' last)

"""


class Puzzle7:

    def __init__(self, path):
        start_time = time.time()
        self.plays = list()
        self.collector = int()

        self.lookup_part1 = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9,
                             '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

        self.lookup_part2 = {'A': 13, 'K': 12, 'Q': 11, 'J': 1, 'T': 10, '9': 9,
                             '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

        self.file_path = path

        # part 1
        self.read_txt()
        self.sort_hands()
        self.score_card_in_hand_part1()
        self.ranked_points()

        print(f"for {path}:")
        print(f"Output of part 1= {self.collector}")
        print(f"Time {round(time.time()-start_time, 4)} [sec]")

        # part 22
        self.read_txt()
        self.score_card_in_hand_part2()
        self.sort_hands_part2()
        self.ranked_points()

        print(f"Output of part 2= {self.collector}")
        print(f"Time {round(time.time()-start_time, 4)} [sec]")

    def ranked_points(self):
        self.collector = 0
        self.plays.sort(key=Puzzle7.get_score)
        for j, _ in enumerate(self.plays):
            self.plays[j].rank_points = self.plays[j].bid * (j+1)
            self.collector += self.plays[j].bid * (j + 1)

    @staticmethod
    def get_score(d):
        return d.score

    def score_card_in_hand_part1(self):
        for j, _ in enumerate(self.plays):
            i = self.plays[j].play
            self.plays[j].score += self.lookup_part1[i[0]] * int(1e8)
            self.plays[j].score += self.lookup_part1[i[1]] * int(1e6)
            self.plays[j].score += self.lookup_part1[i[2]] * int(1e4)
            self.plays[j].score += self.lookup_part1[i[3]] * int(1e2)
            self.plays[j].score += self.lookup_part1[i[4]]

    def score_card_in_hand_part2(self):
        for j, _ in enumerate(self.plays):
            i = self.plays[j].play
            self.plays[j].score += self.lookup_part2[i[0]] * int(1e8)
            self.plays[j].score += self.lookup_part2[i[1]] * int(1e6)
            self.plays[j].score += self.lookup_part2[i[2]] * int(1e4)
            self.plays[j].score += self.lookup_part2[i[3]] * int(1e2)
            self.plays[j].score += self.lookup_part2[i[4]]

    def read_txt(self):
        raw = list()
        with open(self.file_path) as file:
            for line in file:
                raw.append(line.strip())
        data = [i.split(" ") for i in raw]
        self.plays = list()
        for d in data:
            self.plays.append(Hand(d[0], int(d[1])))

    def sort_hands(self):
        offset = int(1e10)
        for j, i in enumerate(self.plays):
            current = i.play
            current_set = list(set(current))
            if len(current_set) == 1:
                self.plays[j].type = "five of a kind"
                self.plays[j].score += 7 * offset
            elif len(current_set) == 2:
                if current.count(current_set[0]) == 4 or current.count(current_set[0]) == 1:
                    self.plays[j].type = "four of a kind"
                    self.plays[j].score += 6 * offset
                else:
                    self.plays[j].type = "full house"
                    self.plays[j].score += 5 * offset
            elif len(current_set) == 3:
                if (current.count(current_set[0]) == 3
                        or current.count(current_set[1]) == 3
                        or current.count(current_set[2]) == 3):
                    self.plays[j].type = "three of a kind"
                    self.plays[j].score += 4 * offset
                else:
                    self.plays[j].type = "two pairs"
                    self.plays[j].score += 3 * offset
            elif len(current_set) == 4:
                self.plays[j].type = "pair"
                self.plays[j].score += 2 * offset
            else:
                self.plays[j].type = "high card"
                self.plays[j].score += 1 * offset

    def sort_hands_part2(self):
        offset = int(1e10)
        for j, i in enumerate(self.plays):
            current = i.play
            current_set = list(set(current))
            js = current.count("J")

            if len(current_set) == 1:
                self.plays[j].type = "five of a kind"
                self.plays[j].score += 7 * offset

            elif len(current_set) == 2:
                if js == 0:
                    if (current.count(current_set[0]) == 4
                            or current.count(current_set[0]) == 1):
                        self.plays[j].type = "four of a kind"
                        self.plays[j].score += 6 * offset
                    else:
                        self.plays[j].type = "full house"
                        self.plays[j].score += 5 * offset
                if js > 0:
                    self.plays[j].type = "five of a kind"
                    self.plays[j].score += 7 * offset

            elif len(current_set) == 3:
                if js == 0:
                    if (current.count(current_set[0]) == 3
                            or current.count(current_set[1]) == 3
                            or current.count(current_set[2]) == 3):
                        self.plays[j].type = "three of a kind"
                        self.plays[j].score += 4 * offset
                    else:
                        self.plays[j].type = "two pairs"
                        self.plays[j].score += 3 * offset

                elif js == 1:
                    if (current.count(current_set[0]) == 3
                            or current.count(current_set[1]) == 3
                            or current.count(current_set[2]) == 3):
                        self.plays[j].type = "four of a kind"
                        self.plays[j].score += 6 * offset
                    elif (current.count(current_set[0]) == 2
                            or current.count(current_set[1]) == 2
                            or current.count(current_set[2]) == 2):
                        self.plays[j].type = "full house"
                        self.plays[j].score += 5 * offset

                elif js == 2:
                    if (current.count(current_set[0]) == 3
                            or current.count(current_set[1]) == 3
                            or current.count(current_set[2]) == 3):
                        self.plays[j].type = "five of a kind"
                        self.plays[j].score += 7 * offset
                    elif (current.count(current_set[0]) == 2
                            or current.count(current_set[1]) == 2
                            or current.count(current_set[2]) == 2):
                        self.plays[j].type = "four of a kind"
                        self.plays[j].score += 6 * offset

                elif js == 3:
                    self.plays[j].type = "four of a kind"
                    self.plays[j].score += 6 * offset

            elif len(current_set) == 4:
                if js == 0:
                    self.plays[j].type = "pair"
                    self.plays[j].score += 2 * offset
                else:
                    self.plays[j].type = "three of a kind"
                    self.plays[j].score += 4 * offset

            elif len(current_set) == 5:
                if js == 0:
                    self.plays[j].type = "high card"
                    self.plays[j].score += 1 * offset
                else:
                    self.plays[j].type = "pair"
                    self.plays[j].score += 2 * offset


@dataclass
class Hand:
    play: str
    bid: int
    score: int = 0
    rank_points: int = 0
    type: str = None


Puzzle7(EXAMPLE)
Puzzle7(DATA)
