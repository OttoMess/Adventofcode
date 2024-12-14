import time
import sympy as sym

EXAMPLE = "AoC_inputs/2024/day_13_example.txt"
INPUT = "AoC_inputs/2024/day_13.txt"


class Puzzle13:
    def __init__(self, path):
        start_time = time.time()

        self.file_path = path
        self.input = list()

        print(self.file_path)
        self.read_txt()

        print(f"output part one: {self.part1()}")
        print(f"output part two: {self.part2()}")
        print(f"Run time {round(time.time() - start_time, 4)} [sec]\n")

    def read_txt(self):
        data = list()
        with open(self.file_path) as file:
            for line in file:
                if "A" in line:
                    _, _, Ax, Ay = line.split()
                elif "B" in line:
                    _, _, Bx, By = line.split()
                elif "Prize:" in line:
                    _, Px, Py = line.split()
                    data.append(
                        {
                            "A": (int(Ax[2:-1]), int(Ay[2:])),
                            "B": (int(Bx[2:-1]), int(By[2:])),
                            "prize": (int(Px[2:-1]), int(Py[2:])),
                        }
                    )

        self.input = data

    def part1(self):
        return

    def part2(self):
        cost = 0
        for machine in self.input:
            Px = machine["prize"][0] + 10000000000000
            Py = machine["prize"][1] + 10000000000000
            Ax = machine["A"][0]
            Ay = machine["A"][1]
            Bx = machine["B"][0]
            By = machine["B"][1]
            An, Bn = sym.symbols("An Bn")
            eq1 = -Py + Ay * (Px - Bx * Bn) / Ax + By * Bn
            b_n = sym.solve(eq1, Bn)
            eq2 = -An + (Px - Bx * b_n[0]) / Ax
            a_n = sym.solve(eq2, An)

            A_n = int(a_n[0])
            B_n = int(b_n[0])
            if A_n > 0 and B_n > 0 and a_n[0] - A_n == 0 and b_n[0] - B_n == 0:
                cost += a_n[0] * 3 + b_n[0]
        return cost


Puzzle13(EXAMPLE)
Puzzle13(INPUT)
