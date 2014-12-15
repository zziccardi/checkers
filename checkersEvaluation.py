# Ziccardi, Zachary; Donohue, Mark; Kasliwal, Mannan; and Suesser, Marc
# CS110 A52, A53, A53, and A53
# Project: checkersEvaluation

import tkinter.messagebox as tk
from Checker import *
import Checkerboard

#Narrative: Returns the contents of a given space
#Precondition: Takes argument to check dictionary
#Postcondition: Returns the contents of dictionary at given key, 0 if DNE
def checkSpace(board, space):
    return board.getSpaceContents().get(space, 0)

#Narrative: Returns whether or not the given space is on an 8x8 board
#Precondition: Takes space as an argument, a tuple of 2 integers
#Postcondition: If 0 and 1 index are both >= 0 and <= 8, returns true, false if
#               they are not
def isValidSpace(space):
    return space[0] > 0 and space[0] < 9 and space[1] > 0 and space[1] < 9

#Narrative: Returns whether or not the team can move in the given direction
#Precondition: Takes in current location, destination, and current turn as
#              arguments
#Postcondition: If the move is south, returns true for team 1. North for team 2
def isCorrectDirection(current, destination, turn):
    #team 1 can move south
    #team 2 can move north
    rowDifference = destination[0] - current[0]
    
    return (((rowDifference) >= 0 and (turn == 1)) or \
            ((rowDifference) <= 0 and (turn == 2)))

#Narrative: Checks whether or not one team has won
#Precondition: Requires a reference to the board to be passed in as argument
#Postcondition: Returns true if one team does not have any pieces, false if
#               both teams still have checkers on the board
def checkWin(board):
    spaceContents = board.getSpaceContents()
    
    ctr = 1
    row = 1
    column = 1

    teamOneOccurance = False
    teamTwoOccurance = False

    while (not (teamOneOccurance and teamTwoOccurance)) and ctr <= 64:
        space = (row, column)
        checker = checkSpace(board, space)

        if checker:
            if checker.getTeam() == 1:
                teamOneOccurance = True
            else:
                teamTwoOccurance = True

        row = ctr % 8 + 1
        column = ctr // 8 + 1
        ctr += 1
    
    return teamOneOccurance != teamTwoOccurance

#Narrative: Ends the game and displays a messagebox
#Precondition: Requires a reference to the board to be passed in as argument
#Postcondition: Destroys the board, displays messagebox to user
def endGame(board):
    board.destroy()
    tk.showinfo("End of Game", "The game is over!")

#Narrative: Moves a checker from one spot to another or deletes it
#Precondition: Requires a reference to the board to be passed in, reference to
#              the checker being moved, and space to be moved to (0 to remove)
#Postcondition: Moves checker to requested space, updates info in the board's
#               dictionary and individual checker object, makes checker a
#               king if it reaches the opposite side of board
def moveChecker(board, checker, space):
    spaceContents = board.getSpaceContents()
    
    del spaceContents[checker.getSpace()]

    if space:
        # checker is being moved, not deleted
        spaceContents[space] = checker
        checker.setSpace(space)

        row = space[0]
        team = checker.getTeam()

        if (row == 8 and team == 1) or (row == 1 and team == 2):
                checker.setIsKing(True)

#Narrative: Called whenever a space is clicked, does all evaluations necessary
#           to determine whether the attempted move is valid or not
#Precondition: Takes in reference to the board, and val which is a tuple value
#              of 2 integers, (row, col)
#Postcondition: Makes the move if it is valid, invalid move message if not
def spaceClicked(board, val):
    curChecker = board.getCurChecker()
    turn = board.getTurn()

    # If a checker is not currently selected by the player:
    if not curChecker:
        spaceContent = checkSpace(board, val)
        
        if spaceContent:
            # If the checker on the clicked space is the same team as the player
            # whose turn it is, assign it to the player
            if spaceContent.getTeam() == turn:
                board.setCurChecker(spaceContent)
                board.updateAnalysisValue("A checker has been selected.")
                board.updateBoard()
                # Make curChecker light up, either change image or highlight
                # button

    # If a checker has been selected, but a move hasn't yet been made.
    elif curChecker == checkSpace(board, val):
        board.setCurChecker(0)
        board.updateAnalysisValue("The checker has been deselected.")
        board.updateBoard()
    else:
        curSpace = curChecker.getSpace()
        r = val[0]
        c = val[1]
        cur_r = curSpace[0]
        cur_c = curSpace[1]

        if not checkSpace(board, val):
            #there is not a checker currently occupying the destination
            
            if not abs(c - cur_c) in [3, 5, 7]:
                #valid column move
                
                if curChecker.getIsKing() or isCorrectDirection(curSpace, \
                                                                val, turn):
                    #valid row move

                    if abs(r - cur_r) == abs(c - cur_c):
                        #valid move
                        if abs(r - cur_r) == 1:
                            moveChecker(board, curChecker, val)
                            board.updateAnalysisValue("The checker has " + \
                                                      "advanced one space.")
                            board.nextTurn()
                            board.updateBoard()

                        else:
                            space = ((r + cur_r) / 2, (c + cur_c) / 2)
                            jumped = checkSpace(board, space)

                            if not jumped:
                                board.updateAnalysisValue("Invalid move!")
                            elif jumped.getTeam() == turn:
                                board.updateAnalysisValue("Invalid move!")
                            else:
                                #nextTurn(board)
                                moveChecker(board, jumped, 0)
                                moveChecker(board, curChecker, val)

                                if checkWin(board):
                                    endGame(board)
                                else:
                                    #check all four possible jump spaces around
                                    #the checker here, if none are open with an
                                    #opposing checker between, then in the else
                                    #statement, do nextTurn(board)
                                    possibleJump = False

                                    for i in range(-1, 2, 2):
                                        for x in range(-1, 2, 2):
                                            test = (r + 2 * x, c + 2 * i)
                                            
                                            if checkSpace(board, test) == 0 \
                                               and isValidSpace(test) and \
                                            (curChecker.getIsKing() or \
                                             isCorrectDirection(val, test, \
                                                                turn)):
                                                midpoint = (int((r + test[0]) \
                                                                / 2),
                                                            int((c + test[1]) \
                                                                / 2))

                                                occupying_mid = checkSpace\
                                                                (board, \
                                                                 midpoint)

                                                if occupying_mid and \
                                                   not occupying_mid.getTeam() \
                                                   == turn:
                                                    possibleJump = True
                                                    
                                    if not possibleJump:
                                        board.updateAnalysisValue("Nice!")
                                        board.nextTurn()
                                    else:
                                        board.updateAnalysisValue("A double" +
                                                                  " jump is" +
                                                                  " available!")

                                    board.updateBoard()

                    else:
                        board.updateAnalysisValue("Invalid move!")
                else:
                    board.updateAnalysisValue("Invalid move!")
            else:
                board.updateAnalysisValue("Invalid move!")
        else:
            board.updateAnalysisValue("Invalid move!")
