from puzzle import Puzzle
import time
import copy

# Main Program

print()
print("========================================")
print("======WELCOME TO 15 PUZZLE SOLVER!======")
print("========================================")
print()

print("*** DO YOU WANT TO USE INPUT FILE? (Y/N)")

# Asumsi input user selalu benar
inputUser = input()
print()

puzzle = Puzzle()

if (inputUser == "Y"):
    inputFile = input("*** INPUT THE FILE NAME (with .txt): ")
    puzzle.readFile(inputFile)
else:
    puzzle.random()

printpuzzle = copy.deepcopy(puzzle)

print()
print("========PUZZLE's INITIAL STATE==========")
puzzle.print()
print()

if (puzzle.isSolvable()):

    startTime = time.time()

    puzzle.generated.append(puzzle.puzzle)

    while(not puzzle.isSolution()):
       puzzle.solvePuzzle()

    endTime = time.time()    
    n = len(puzzle.path)

    for path in puzzle.path:
        if (path == 'up'):
            printpuzzle.printup()
        elif (path == 'down'):
            printpuzzle.printdown()
        elif (path == 'left'):
            printpuzzle.printleft()
        else:
            printpuzzle.printright()


    print("PUZZLE IS SOLVED!")
    print("TOTAL STEPS : ", n)
    print("TOTAL NODE GENERATED: ", Puzzle.node)
    print("TIME TAKEN: ",endTime - startTime,"s")

else:
    print("PUZZLE IS NOT SOLVABLE :(")