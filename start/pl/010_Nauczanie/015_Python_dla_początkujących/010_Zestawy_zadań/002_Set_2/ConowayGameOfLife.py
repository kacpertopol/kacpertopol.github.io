import sys

# See: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# for more details. Or implementation will use a 20x20 grid
# of cells.

# The underscore _ means we are not interested in the value
# of the row or column.
state = {
            "finished" : False , 
            "iteration" : 0 , 
            "cells" : [[0 for _ in range(20)] for _ in range(20)]
        }

def updateCell(cells , i , j):
    # Updates a single cell at position i,j
    # in cell grid: cells.

    # Calculate the neighbours that are alive
    # notice we are using the modulo operation
    # returning the remainder of division.
    # Also notice that we can use \ to extend the command
    # to the next line.
    # Thanks to this we can connect the top to the bottom
    # and the left to the right of our cell grid:
    aliveNeighbours =   cells[(i + 1) % 20][(j + 1) % 20] + \
                        cells[(i + 0) % 20][(j + 1) % 20] + \
                        cells[(i - 1) % 20][(j + 1) % 20] + \
                        cells[(i + 1) % 20][(j - 1) % 20] + \
                        cells[(i + 0) % 20][(j - 1) % 20] + \
                        cells[(i - 1) % 20][(j - 1) % 20] + \
                        cells[(i + 1) % 20][(j + 0) % 20] + \
                        cells[(i - 1) % 20][(j + 0) % 20] 

    # Notice that 0 is like False and 1 is like True
    # so we can do:
    if(cells[i][j]):
        if(aliveNeighbours < 2):
            return 0
        elif(aliveNeighbours == 2 or aliveNeighbours == 3):
            return 1
        elif(aliveNeighbours > 3):
            return 0
    else:
        if(aliveNeighbours == 3):
            return 1
        else:
            return 0
    # Here it is important to return something and not None.
    # Just to make sure we add a final return statement:
    return 0

def iterateCells(s):
    # Updates all cells in cell grid: s["cells"]

    newCells = [[updateCell(s["cells"] , i , j) for i in range(20)] for j in range(20)]
    s["cells"] = newCells
    s["iteration"] += 1

def changeCell(s):
    # Change the state of a single cell from dead to alive or vice versa.

    # The % 20 at the end is to make sure i , j are inside the grid
    i = int(input("Please enter first coordinate of cell: ")) % 20
    j = int(input("Please enter second coordinate of cell: ")) % 20
    # turns 0 to 1 and 1 to 0:
    s["cells"][i][j] = (s["cells"][i][j] + 1) % 2

def endGame(s):
    # End the game.
    s["finished"] = True

# Some options for the user to chose from.
# Notice these are all names of functions:
alternatives =  {
                    "i" : iterateCells ,
                    "c" : changeCell ,
                    "q" : endGame
                }

def updateGameState(s):
    # Updates the state of the game. 
    # Used in the main game loop.
    whatToDo = input("i (to iterate), c (to change cell), q (to quit) ? ")
    # Use in to check if the dictionary has key
    if(whatToDo in alternatives):
        alternatives[whatToDo](s)
    else:
        print("Option not recognized.")

# For showing the state of the game using ASCI characters:
symbols =   {
                0 : "  " , # dead cell shows up as two empty spaces
                1 : "[]" # living cell shows up as []
            }

def showGameState(s):
    # Shows the state of the cell grid and
    # the iteration number.
    print("ITERATION : " , s["iteration"])
    for i in range(20):
        for j in range(20):
            sys.stdout.write(symbols[s["cells"][i][j]])
        sys.stdout.write("\n")

# Main game loop:
while(not state["finished"]):
    updateGameState(state)
    showGameState(state)


