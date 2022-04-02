import random

class Puzzle: 
    def __init__(self) -> None:
        self.puzzle = [0 for i in range(16)]

    def random(self):
        number = list(range(0, 16))
        random.shuffle(number)
        for i in range (16):
            self.puzzle[i] = number[i]

    def readFile(self, fileName):
        f = open(fileName , 'r')
        stringPuzzle = f.read().replace('\n', ' ').split(" ")
        f.close()
        for i in range (16):
            self.puzzle[i] = int(stringPuzzle[i])

    def print(self):
        for i in range(16):
            print(self.puzzle[i], end=" ")
            if (i % 4 == 3):
                print()



