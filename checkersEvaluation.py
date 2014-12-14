# Ziccardi, Zachary; Donohue, Mark; Kasliwal, Mannan; and Suesser, Marc
# CS110 A52, A53, A53, and A53
# Project: checkersEvaluation

import tkinter.messagebox as tk
from Checker import *
import Checkerboard

#this function is for debugging only
def invalidMoveMessage(num):
    print("Error:", num)

#Narrative: Changes the turn 
#Precondition: Global variable turn is required
#Postcondition: Toggles turn variable between 1 and 2, resets current checker
def nextTurn(frame):
    print('next turn')

    if frame.getTurn() == 1:
        frame.setTurn(2)
    else:
        frame.setTurn(1)

    frame.setCurChecker(0)

#Narrative: Returns the contents of a given space
#Precondition: Takes argument to check dictionary, preferably a tuple of 2 ints
#Postcondition: Returns the contents of dictionary at given key, 0 if DNE
def checkSpace(frame, space):
    return frame.getSpaceContents().get(space, 0)

def isValidSpace(space):
    return space[0] > 0 and space[0] < 9 and space[1] > 0 and space[1] < 9

def isCorrectDirection(current, destination, turn):
    #team 1 can move south
    #team 2 can move north
    rowDifference = destination[0] - current[0]
    
    return (((rowDifference) >= 0 and (turn == 1)) or \
            ((rowDifference) <= 0 and (turn == 2)))
    

def updateBoard(frame):
    turn = frame.getTurn()
    curChecker = frame.getCurChecker()
    spaceContents = frame.getSpaceContents()
    frame.destroy()
    
    new_frame = Checkerboard.Checkerboard(turn, curChecker, spaceContents)
    new_frame.mainloop()

def checkWin(frame):
    spaceContents = frame.getSpaceContents()
    
    ctr = 1
    row = 1
    column = 1

    teamOneOccurance = False
    teamTwoOccurance = False

    while (not (teamOneOccurance and teamTwoOccurance)) and ctr <= 64:
        space = (row, column)
        checker = checkSpace(frame, space)

        if checker:
            if checker.getTeam() == 1:
                teamOneOccurance = True
            else:
                teamTwoOccurance = True

        row = ctr % 8 + 1
        column = ctr // 8 + 1
        ctr += 1
    
    return teamOneOccurance != teamTwoOccurance

def endGame(frame):
    frame.destroy()
    tk.showinfo("End Of Game", "The game is over!")

#Narrative: 
#Precondition: 
#Postcondition: 
def moveChecker(frame, checker, space):
    spaceContents = frame.getSpaceContents()
    
    del spaceContents[checker.getSpace()]

    if space:
        # checker is being moved, not deleted
        spaceContents[space] = checker
        checker.setSpace(space)

        row = space[0]
        team = checker.getTeam()

        if (row == 8 and team == 1) or (row == 1 and team == 2):
                checker.setIsKing(True)

def buttonCreated(frame, button):
    spaceContents = frame.getSpaceContents()

    spaceContents[button.getSpace()] = button
    
    frame.setSpaceContents(spaceContents)

#Narrative: Called whenever a space is clicked, does all evaluations necessary
#           to determine whether the attempted move is valid or not
#Precondition: Takes in val, which is a tuple value of 2 integers, (row, col)
#Postcondition: Makes the move if it is valid, invalid move message if not
def spaceClicked(frame, val):
    curChecker = frame.getCurChecker()
    turn = frame.getTurn()

    # If a checker is not currently selected by the player:
    if not curChecker:
        spaceContent = checkSpace(frame, val)
        
        if spaceContent:
            # If the checker on the clicked space is the same team as the player
            # whose turn it is, assign it to the player
            if spaceContent.getTeam() == turn:
                frame.setCurChecker(spaceContent)
                print("curChecker assigned.")

                # Make curChecker light up, either change image or highlight
                # button

    # If a checker has been selected, but a move hasn't yet been made.
    elif curChecker == checkSpace(frame, val):
        frame.setCurChecker(0)
        print("The previously selected checker is now deselected.")
    else:
        curSpace = curChecker.getSpace()
        r = val[0]
        c = val[1]
        cur_r = curSpace[0]
        cur_c = curSpace[1]

        if not checkSpace(frame, val):
            #there is not a checker currently occupying the destination
            
            if not abs(c - cur_c) in [3, 5, 7]:
                #valid column move
                
                if curChecker.getIsKing() or isCorrectDirection(curSpace, val, turn):
                    #valid row move

                    if abs(r - cur_r) == abs(c - cur_c):
                        #valid move
                        if abs(r - cur_r) == 1:
                            nextTurn(frame)
                            moveChecker(frame, curChecker, val)
                            updateBoard(frame)

                        else:
                            space = ((r + cur_r) / 2, (c + cur_c) / 2)
                            jumped = checkSpace(frame, space)

                            if not jumped:
                                invalidMoveMessage(1)
                            elif jumped.getTeam() == turn:
                                invalidMoveMessage(2)
                                print(abs(r - cur_r))
                                print("r:", r)
                                print("cur_r:", cur_r)
                            else:
                                #nextTurn(frame)
                                moveChecker(frame, jumped, 0)
                                moveChecker(frame, curChecker, val)

                                if checkWin(frame):
                                    endGame(frame)
                                else:
                                    #check all four possible jump spaces around
                                    #the checker here, if none are open with an
                                    #opposing checker between, then in the else
                                    #statement, do nextTurn(frame)

                                    possibleJump = False

                                    for i in range(-1, 2, 2):
                                        for x in range(-1, 2, 2):
                                            test = (r + 2 * x, c + 2 * i)
                                            print("Testing:", test)
                                            
                                            if checkSpace(frame, test) == 0 and isValidSpace(test) and \
                                            (curChecker.getIsKing() or isCorrectDirection(val, test, turn)):
                                                midpoint = (int((r + test[0]) / 2),
                                                            int((c + test[1]) / 2))

                                                occupying_mid = checkSpace(frame, midpoint)

                                                if occupying_mid and \
                                                   not occupying_mid.getTeam() == turn:
                                                    possibleJump = True
                                                    print("Midpoint found:", midpoint)

                                    #still bugs, but above logic works - bang bang
                                                    
                                    if not possibleJump:
                                        print("No possible jump")
                                        nextTurn(frame)

                                    updateBoard(frame)

                    else:
                        invalidMoveMessage(3)
                        print("r:", r)
                        print("cur_r:", cur_r)
                else:
                    invalidMoveMessage(4)
                    print("r:", r)
                    print("cur_r:", cur_r)
            else:
                invalidMoveMessage(5)
                print("r:", r)
                print("cur_r:", cur_r)
        else:
            invalidMoveMessage(6)
            print("r:", r)
            print("cur_r:", cur_r)
