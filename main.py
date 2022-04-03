from puzzle import Puzzle
import time

# Main Program

print()
print("=====WELCOME TO 15 PUZZLE SOLVER!=====")
print()
print("*** DO YOU WANT TO USE INPUT FILE? (Y/N)")

# Asumsi input user selalu benar
inputUser = input()

puzzle = Puzzle()

if (inputUser == "Y"):
    inputFile = input("*** INPUT THE FILE NAME (with .txt): ")
    puzzle.readFile(inputFile)
else:
    puzzle.random()

print()
print("=====PUZZLE's INITIAL STATE=====")
puzzle.print()
print()

if (puzzle.isSolvable()):
    startTime = time.time()
    puzzle.generated.append(puzzle.puzzle)
    print (puzzle.generated)
    while(not puzzle.isSolution()):
        puzzle.solvePuzzle()

    endTime = time.time()    
    print(puzzle.path)
    puzzle.printPath()

    print("PUZZLE IS SOLVED!")
    print("TOTAL NODE GENERATED: ", Puzzle.node)
    print("TIME TAKEN: ",endTime - startTime,"s")

else:
    print("PUZZLE IS NOT SOLVABLE :(")