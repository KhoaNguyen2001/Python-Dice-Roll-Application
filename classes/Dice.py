import random

class Dice:
    def __init__(self):
        self.__sides = 6
        self.__value = 1

    def rollDice(self):
        self.__value = random.randint(1, self.__sides)
        return self.__value

    def __getattribute__(self, name):
        if name == "sides":
            return self.__sides
        elif name == "value":
            return self.__value
        else:
            return super().__getattribute__(name)

    def printDice(self) -> None:
        layout = {
            1: [(1, 1)],
            2: [(0, 0), (2, 2)],
            3: [(0, 0), (1, 1), (2, 2)],
            4: [(0, 0), (0, 2), (2, 0), (2, 2)],
            5: [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
            6: [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
        }
        grid = [[" "] * 7 for _ in range(7)]
        for i in range(7):
            grid[0][i] = grid[6][i] = "-"
            grid[i][0] = grid[i][6] = "|"
        grid[0][0] = grid[0][6] = grid[6][0] = grid[6][6] = "+"
        pos_map = {0: 2, 1: 3, 2: 4}
        for r, c in layout[self.__value]:
            grid[pos_map[r]][pos_map[c]] = "•"
        print("\n".join("".join(row) for row in grid))
