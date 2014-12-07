# Ziccardi, Zachary; Donohue, Mark; Kasliwal, Mannan; and Suesser, Marc
# CS110 A52, A53, A53, and A53
# Project: main

import Checkerboard, Checker, checkersEvaluation

def createCheckers():
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
        checkersEvaluation.buttonCreated(Checker.Checker(False, \
                                                         space, (i // 12) + 1))

def main():
    createCheckers()

    Checkerboard.Checkerboard().mainloop()

main()
