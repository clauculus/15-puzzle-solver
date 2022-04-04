import random
import copy

class Puzzle: 
    node = 0

    # cctor
    def __init__(self) -> None:
        self.puzzle = [0 for i in range(16)]
        self.queue = []
        self.generated = []
        self.path = []
        self.depth = 0

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

    def printup(self):
        idx = self.find16()
        if (idx > 3):
            self.puzzle[idx] = self.puzzle[idx - 4]
            self.puzzle[idx - 4] = 16 
        print('up')
        self.print()
        print()

    def printdown(self):
        idx = self.find16()
        if (idx < 12):
            self.puzzle[idx] = self.puzzle[idx + 4]
            self.puzzle[idx + 4] = 16
        print('down')
        self.print()
        print()

    def printleft(self):
        idx = self.find16()
        if (idx % 4 != 0):
            self.puzzle[idx] = self.puzzle[idx - 1]
            self.puzzle[idx - 1] = 16
        print('left')
        self.print()
        print()        

    def printright(self):
        idx = self.find16()
        if ( idx % 4 != 3):
            self.puzzle[idx] = self.puzzle[idx + 1]
            self.puzzle[idx + 1] = 16
        print('right')
        self.print()
        print()        
            
    # to count the number of misplaced puzzle
    def misplaced(self, puz):
        count = 0
        for i in range(16):
            if (puz[i] != (i + 1)):
                if (puz[i] != 16):
                    count += 1
        return count


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
        x = False
        for i in idx:
            if (self.puzzle[i] == 16):
                x = True
                total += 1

        if (x):
            print("X = 1")
        else:
            print("X = 0")

        print("SIGMA of KURANG(i) + X = ", total)
        print()
        print("Loading...")
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

    # return the index of 16 (blank space)
    def find16(self):
        i = 0
        while (self.puzzle[i] != 16):
            i += 1

        return i

    # check is it possible to move up
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
        if (idx > 3):
            upPuzzle[idx] = upPuzzle[idx - 4]
            upPuzzle[idx - 4] = 16
        return upPuzzle

    # check is it possible to move down
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
        if (idx < 12):
            downPuzzle[idx] = downPuzzle[idx + 4]
            downPuzzle[idx + 4] = 16
        return downPuzzle

    # check is it possible to move left    
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
    
    # check is it possible to move right
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
    
    # branch and bound
    def solvePuzzle(self):
        
        self.depth += 1

        # check if it is possible to move up
        if (self.isUp()):
            upPuzzle = self.up()     
            # if the state has not been generated before
            if (not self.isGenerated(upPuzzle)):
                path = copy.deepcopy(self.path)
                path.append('up')
                self.generated.append(upPuzzle)
                self.queue.insert(0,[self.misplaced(upPuzzle) + self.depth, upPuzzle, path, self.depth])
                Puzzle.node += 1 

        # check if it is possible to move right
        if (self.isRight()):
            rightPuzzle = self.right() 
            # if the state has not been generated before
            if (not self.isGenerated(rightPuzzle)):
                path = copy.deepcopy(self.path)
                path.append('right')
                self.generated.append(rightPuzzle)
                self.queue.insert(0,[self.misplaced(rightPuzzle) + self.depth, rightPuzzle, path, self.depth])
                Puzzle.node += 1          

        # check if it is possible to move down
        if (self.isDown()):
            downPuzzle = self.down()   
            # if the state has not been generated before
            if (not self.isGenerated(downPuzzle)):
                path = copy.deepcopy(self.path)
                path.append('down')
                self.generated.append(downPuzzle)
                self.queue.insert(0,[self.misplaced(downPuzzle) + self.depth, downPuzzle, path, self.depth])
                Puzzle.node += 1    

        # check if it is possible to move left
        if (self.isLeft()):
            leftPuzzle = self.left()
            # if the state has not been generated before
            if (not self.isGenerated(leftPuzzle)):
                path = copy.deepcopy(self.path)
                path.append('left')
                self.generated.append(leftPuzzle)
                self.queue.insert(0,[self.misplaced(leftPuzzle) + self.depth, leftPuzzle, path, self.depth])
                Puzzle.node += 1     

        self.queue.sort()

        current = self.queue.pop(0)

        self.puzzle = current[1]
        self.path = current[2]
        self.depth = current[3]

