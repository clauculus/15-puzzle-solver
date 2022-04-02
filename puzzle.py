import random

class Puzzle: 
    depth = 0

    def __init__(self) -> None:
        self.puzzle = [0 for i in range(16)]

    def random(self):
        number = list(range(1, 17))
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

    def misplaced(self):
        count = 0
        for i in range(16):
            if (self.puzzle[i] != (i + 1)):
                if (self.puzzle[i] != 16):
                    count += 1
        return count
    
    def cost(self):
        return Puzzle.depth + self.misplaced()

    def kurang(self, i):
        count = 0
        for j in range (i + 1, 16):
            if (self.puzzle[j] < self.puzzle[i]):
                if (self.puzzle[j] != 0):
                    count += 1 
        return count

    def isSolvable(self):
        total = 0
        for i in range (15):
            print("Kurang (" + str(self.puzzle[i]) + "): "+ str(self.kurang(i)))
            total += self.kurang(i)
            
        idx = [1, 3, 4, 6, 9, 11, 12, 14]
        for i in idx:
            if (self.puzzle[i] == 0):
                total += 1

        print("Nilai Kurang(i) + X adalah:", total)
        
        if (total % 2 == 0):
            return True
        else:
            return False

    def isSolution(self):
        solution = True
        for i in range (16):
            if (self.puzzle[i] != (i + 1)):
                solution = False

        return solution






