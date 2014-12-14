# Ziccardi, Zachary; Donohue, Mark; Kasliwal, Mannan; and Suesser, Marc
# CS110 A52, A53, A53, and A53
# Project: main

from Checkerboard import *
from Checker import *

#Narrative: Creates a dict of checkers in default positions for start of game
#Precondition: Must be called
#Postcondition: Returns a dictionary containing 24 checkers, 12 on each team
def createCheckers():
    checkerDict = {}
    listRows = [1, 2, 3, 6, 7, 8]

    # Creating 24 checkers
    for i in range(24):
        if (i // 4) % 2:
            # row value: every set of four iterations takes one of the values
            #            from listRows
            # col value: spaced by two, shifted by one on every other row to
            #            create the checkerboard effect
            space = (listRows[i // 4], ((i * 2) % 8) + 2)
        else:
            space = (listRows[i // 4], ((i * 2) % 8) + 1)

        # Creates the checker with the calculate space value, team 1 for the
        # first 12 checkers and team 2 for the final 12
        checkerDict[space] = Checker(False, space, (i // 12) + 1)

    return checkerDict

def main():
    board = Checkerboard(1, createCheckers())
    board.updateAnalysisValue("Let the game begin!")
    board.mainloop()

main()
