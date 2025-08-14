from .Dice import Dice

class DiceSet:
    def __init__(self, number_of_dices):
        self.__dices = [Dice() for _ in range(number_of_dices)]

    def rollAllDices(self):
        return [die.rollDice() for die in self.__dices]

    def printAllDices(self):
        for die in self.__dices:
            die.printDice()