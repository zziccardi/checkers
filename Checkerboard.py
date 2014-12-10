# Ziccardi, Zachary; Donohue, Mark; Kasliwal, Mannan; and Suesser, Marc
# CS110 A52, A53, A53, and A53
# Project: Checkerboard

from tkinter import *
import checkersEvaluation

class Checkerboard(Frame):
    def __init__(self, turn, checker, spaceContents):
        Frame.__init__(self)
        self.master.title("Checkerboard")
        self.grid()
        
        self.__redChecker = PhotoImage(file = "redChecker.gif")
        self.__whiteChecker = PhotoImage(file = "whiteChecker.gif")
        self.__blackBlank = PhotoImage(file = "blackBlank.gif")
        self.__whiteBlank = PhotoImage(file = "whiteBlank.gif")
        self.__redKing = PhotoImage(file = "redCheckerKing.gif")
        self.__whiteKing = PhotoImage(file = "whiteCheckerKing.gif")

        #Team 1 can move south
        #Team 2 can move north
        self.__turn = turn

        #Reference to the checker currently chosen by the player whose turn it
        #currently is, 0 if no checker is currently chosen
        self.__curChecker = checker

        #Will hold the contents of each space by using the space as a key, with data
        #type being a tuple of integer, corresponding to (row, column). Value of each
        #key will contain a reference to the checker occupying the space if it exists
        self.__spaceContents = spaceContents

        for i in range(64):
            r = (i // 8) + 1
            c = (i % 8) + 1
            space = (r, c)

            checker = spaceContents.get(space, 0)

            if r % 2:
                if c % 2 and checker:
                    if checker.getTeam() == 1:
                        if checker.getIsKing():
                            self.makeRedKing(space, r, c)
                        else:
                            self.makeRedChecker(space, r, c) 
                        
                    else:
                        if checker.getIsKing():
                            self.makeWhiteKing(space, r, c)
                        else:
                            self.makeWhiteChecker(space, r, c)
                        
                elif checker:
                    if checker.getTeam() == 1:
                        if checker.getIsKing():
                            self.makeRedKing(space, r, c)
                        else:
                            self.makeRedChecker(space, r, c)
                        
                    else:
                        if checker.getIsKing():
                            self.makeWhiteKing(space, r, c)
                        else:
                            self.makeWhiteChecker(space, r, c)
                        
                elif c % 2:
                    self.makeBlackBlank(space, r, c)
                    
                else:
                    self.makeWhiteBlank(space, r, c)
                    
            else:
                if c % 2 and checker:
                    if checker.getTeam() == 1:
                        if checker.getIsKing():
                            self.makeRedKing(space, r, c)
                        else:
                            self.makeRedChecker(space, r, c)
                    else:
                        if checker.getIsKing():
                            self.makeWhiteKing(space, r, c)
                        else:
                            self.makeWhiteChecker(space, r, c)
                        
                elif checker:
                    if checker.getTeam() == 1:
                        if checker.getIsKing():
                            self.makeRedKing(space, r, c)
                        else:
                            self.makeRedChecker(space, r, c)
                        
                    else:
                        if checker.getIsKing():
                            self.makeWhiteKing(space, r, c)
                        else:
                            self.makeWhiteChecker(space, r, c)
                        
                elif c % 2:
                    self.makeWhiteBlank(space, r, c)
               
                else:
                    self.makeBlackBlank(space, r, c)

    def makeRedChecker(self, space, r, c):
        self.__button = Button(self, command=lambda widget=space: \
                               self.__activated(widget), \
                               image = self.__redChecker)
        
        self.__button.grid(row=r, column=c)

    def makeWhiteChecker(self, space, r, c):
        self.__button = Button(self, command=lambda widget=space: \
                               self.__activated(widget), \
                               image = self.__whiteChecker)
        
        self.__button.grid(row=r, column=c)

    def makeRedKing(self, space, r, c):
        self.__button = Button(self, command=lambda widget=space: \
                               self.__activated(widget), \
                               image = self.__redKing)
        
        self.__button.grid(row=r, column=c)

    def makeWhiteKing(self, space, r, c):
        self.__button = Button(self, command=lambda widget=space: \
                               self.__activated(widget), \
                               image = self.__whiteKing)
        
        self.__button.grid(row=r, column=c)

    def makeBlackBlank(self, space, r, c):
        self.__button = Button(self, command=lambda widget=space: \
                               self.__activated(widget), \
                               image = self.__blackBlank)
        
        self.__button.grid(row=r, column=c)

    def makeWhiteBlank(self, space, r, c):
        self.__button = Button(self, command=lambda widget=space: \
                               self.__activated(widget), \
                               image = self.__whiteBlank)
        
        self.__button.grid(row=r, column=c)

    def getTurn(self):
        return self.__turn

    def setTurn(self, turn):
        self.__turn = turn

    def getCurChecker(self):
        return self.__curChecker

    def setCurChecker(self, curChecker):
        self.__curChecker = curChecker

    def getSpaceContents(self):
        return self.__spaceContents

    def setSpaceContents(self, spaceContents):
        self.__spaceContents = spaceContents

    def __activated(self, space):
        checkersEvaluation.spaceClicked(self, space)
        print(space)
