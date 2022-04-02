from puzzle import Puzzle
# Main Program

print("Welcome to 15 puzzle solver")
print()
print("DO YOU WANT TO USE INPUT FILE? (Y/N)")

inputyes = input()

puzzle = Puzzle()

if (inputyes == "Y"):
    inputFile = input("Masukkan nama file (dengan .txt): ")
    puzzle.readFile(inputFile)
else:
    print("random puzzle")
    puzzle.random()

puzzle.print()