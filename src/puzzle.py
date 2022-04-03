import random
import copy
from turtle import right

class Puzzle: 
    depth = 0
    node = 0

    # cctor
    def __init__(self) -> None:
        self.puzzle = [0 for i in range(16)]
        self.queue = []
        self.generated = []

    # to randomize puzzle
    def random(self):
        number = list(range(1, 17))
        random.shuffle(number)
        for i in range (16):
            self.puzzle[i] = number[i]

    # to read puzzle from a txt file
    def readFile(self, fileName):
        f = open(fileName , 'r')
        stringPuzzle = f.read().replace('\n', ' ').split(" ")
        f.close()
        for i in range (16):
            self.puzzle[i] = int(stringPuzzle[i])

    # to print puzzle
    def print(self):
        for i in range(16):
            print(self.puzzle[i], end=" ")
            if (i % 4 == 3):
                print()

    # to count the number of misplaced puzzle
    def misplaced(self, puz):
        count = 0
        for i in range(16):
            if (puz[i] != (i + 1)):
                if (puz[i] != 16):
                    count += 1
        return count
    
    # to count the cost
    def cost(self, puz):
        #print("Depth adalah ", Puzzle.depth)
        #print("Banyak misplaced ", self.misplaced(puz))
        return Puzzle.depth + self.misplaced(puz)

    # to find KURANG (i)
    def kurang(self, i):
        count = 0
        for j in range (i + 1, 16):
            if (self.puzzle[j] < self.puzzle[i]):
                if (self.puzzle[j] != 0):
                    count += 1 
        return count

    # to check if a puzzle is solvable or not
    def isSolvable(self):
        total = 0
        kurang = [0 for i in range (16)]
        for i in range (16):
            kurang[self.puzzle[i] - 1] = self.kurang(i)
            total += self.kurang(i)

        for i in range (16):
            print("KURANG (" + str(i + 1) + ") = "+ str(kurang[i]))
            
        idx = [1, 3, 4, 6, 9, 11, 12, 14]
        for i in idx:
            if (self.puzzle[i] == 16):
                print("X = 1")
                total += 1

        print("SIGMA of KURANG(i) + X = ", total)
        print()
        
        if (total % 2 == 0):
            return True
        else:
            return False

    # to check if it is already the final state
    def isSolution(self):
        solution = True
        for i in range (16):
            if (self.puzzle[i] != (i + 1)):
                solution = False

        return solution

    # return index of 16 (blank space)
    def find16(self):
        i = 0
        while (self.puzzle[i] != 16):
            i += 1

        return i

    def isUp(self):
        idx = self.find16()
        if ( idx > 3):
            return True
        else:
            return False
        
    # move up
    def up(self):
        upPuzzle = copy.deepcopy(self.puzzle)
        idx = self.find16()
        if ( idx > 3):
            upPuzzle[idx] = upPuzzle[idx - 4]
            upPuzzle[idx - 4] = 16
        return upPuzzle

    def isDown(self):
        idx = self.find16()
        if ( idx < 12):
            return True
        else:
            return False

    # move down
    def down(self):
        downPuzzle = copy.deepcopy(self.puzzle)
        idx = self.find16()
        if ( idx < 12):
            downPuzzle[idx] = downPuzzle[idx + 4]
            downPuzzle[idx + 4] = 16
        return downPuzzle
    
    def isLeft(self):
        idx = self.find16()
        if (idx % 4 != 0):
            return True
        else:
            return False

    # move left
    def left(self):
        leftPuzzle = copy.deepcopy(self.puzzle)
        idx = self.find16()
        if (idx % 4 != 0):
            leftPuzzle[idx] = leftPuzzle[idx - 1]
            leftPuzzle[idx - 1] = 16
        return leftPuzzle 
    
    def isRight(self):
        idx = self.find16()
        if (idx % 4 != 3):
            return True
        else:
            return False

    # move right
    def right(self):
        rightPuzzle = copy.deepcopy(self.puzzle)
        idx = self.find16()
        if ( idx % 4 != 3):
            rightPuzzle[idx] = rightPuzzle[idx + 1]
            rightPuzzle[idx + 1] = 16
        return rightPuzzle

    # to check if current puzzle has been generated before
    def isGenerated(self, puzzle):
        if puzzle in self.generated:
            return True
        else:
            return False
    
    def solvePuzzle(self):
        if (self.isUp()):
            upPuzzle = self.up()     
            if (not self.isGenerated(upPuzzle)):
                self.generated.append(upPuzzle)
                self.queue.append([self.cost(upPuzzle), upPuzzle, 'up'])
                Puzzle.node += 1 

        if (self.isRight()):
            rightPuzzle = self.right() 
            if (not self.isGenerated(rightPuzzle)):
                self.generated.append(rightPuzzle)
                self.queue.append([self.cost(rightPuzzle), rightPuzzle, 'right'])
                Puzzle.node += 1          

        if (self.isDown()):
            downPuzzle = self.down()   
            if (not self.isGenerated(downPuzzle)):
                self.generated.append(downPuzzle)
                self.queue.append([self.cost(downPuzzle), downPuzzle, 'down'])
                Puzzle.node += 1    

        if (self.isLeft()):
            leftPuzzle = self.left()
            if (not self.isGenerated(leftPuzzle)):
                self.generated.append(leftPuzzle)
                self.queue.append([self.cost(leftPuzzle), leftPuzzle, 'left'])
                Puzzle.node += 1     

        self.queue.sort()

        current = self.queue.pop(0)

        self.puzzle = current[1]
        print(current[2])
        self.print()
        print()
      









