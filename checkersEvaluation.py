# Ziccardi, Zachary; Donohue, Mark; Kasliwal, Mannan; and Suesser, Marc
# CS110 A52, A53, A53, and A53
# Project: checkersEvaluation

from Checker import *
import Checkerboard

#Team 1 can move south
#Team 2 can move north
turn = 1

#Will hold the contents of each space by using the space as a key, with data
#type being a tuple of integer, corresponding to (row, column). Value of each
#key will contain a reference to the checker occupying the space if it exists
spaceContents = {}

#Reference to the checker currently chosen by the player whose turn it
#currently is, 0 if no checker is currently chosen
curChecker = 0

def invalidMoveMessage():
    print("Can't make that move!")
    #replace with message box eventually

#Narrative: Changes the turn 
#Precondition: Global variable turn is required
#Postcondition: Toggles turn variable between 1 and 2, resets current checker
def nextTurn():
    if turn == 1:
        turn = 2
    else:
        turn = 1

    curChecker = 0

#Narrative: Returns the contents of a given space
#Precondition: Takes argument to check dictionary, preferably a tuple of 2 ints
#Postcondition: Returns the contents of dictionary at given key, 0 if DNE
def checkSpace(space):
    return spaceContents.get(space, 0)

#Narrative: 
#Precondition: 
#Postcondition: 
def moveChecker(frame, checker, space):
    del spaceContents[checker.getSpace()]

    if space:
        spaceContents[space] = checker

    #redraw the board
    frame.destroy()
    Checkerboard.Checkerboard().mainloop()

def buttonCreated(button):
    spaceContents[button.getSpace()] = button

def getSpaces():
    return spaceContents

#Narrative: Called whenever a space is clicked, does all evaluations necessary
#           to determine whether the attempted move is valid or not
#Precondition: Takes in val, which is a tuple value of 2 integers, (row, col)
#Postcondition: Makes the move if it is valid, invalid move message if not
def spaceClicked(frame, val):
    global curChecker

    # If a checker is not currently selected by the player:
    if not curChecker:
        spaceContent = checkSpace(val)
        
        if spaceContent:

            # If the checker on the clicked space is the same team as the player
            # whose turn it is, assign it to the player
            if spaceContent.getTeam() == turn:
                curChecker = spaceContent
                print("curChecker assigned.")

                # Make curChecker light up, either change image or highlight
                # button
    elif curChecker == checkSpace(val):
        curChecker = 0
    else:
        r = val[0]
        c = val[1]
        cur_r = curChecker.getSpace()[0]
        cur_c = curChecker.getSpace()[1]

        if not checkSpace(val):
            #there is not a checker currently occupying the destination
            
            if not abs(c - cur_c) in [3, 5, 7]:
                #valid column move
                
                if curChecker.getIsKing() or \
                   (((r - cur_r) >= 0 and (turn == 1)) or \
                   ((r - cur_r) <= 0 and (turn == 2))):
                    #valid row move

                    if abs(r - cur_r) == abs(c - cur_c):
                        #valid move
                        if abs(r - cur_r) == 1:
                            moveChecker(frame, curChecker, val)
                            #make the move

                        else:
                            space = ((r + cur_r) / 2, (c + cur_c) / 2)
                            jumped = checkSpace(space)

                            if not jumped:
                                invalidMoveMessage()
                            elif jumped.getTeam() == turn:
                                invalidMoveMessage()
                            else:
                                moveChecker(frame, jumped, 0)
                                moveChecker(frame, curChecker, val)

                    else:
                        invalidMoveMessage()
                else:
                    invalidMoveMessage()
            else:
                invalidMoveMessage()
        else:
            invalidMoveMessage()
