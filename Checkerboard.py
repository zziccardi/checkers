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

        # New Frame for menu title
        self.__titleFrame = Frame(self)
        self.__titleFrame.grid(column = 9, row = 1)

        # New Frame for Names
        self.__nameFrame = Frame(self)
        self.__nameFrame.grid(column = 9, row = 2, padx = 20)

        # New Frame for Turn
        self.__turnFrame = Frame(self)
        self.__turnFrame.grid(column = 9, row = 3)

        
        # Label for the 'title' of the menu
        self.__startGameLabel = Label(self.__titleFrame, \
                                      text = "Let's play Checkers!")

        # Player name labels, Player name entries,
        # Submit buttons
        self.__redPlayerLabel = Label(self.__nameFrame, \
                                      text = "Red Team Player Name:")
        self.__redNameEntry = Entry(self.__nameFrame, \
                                    width = 10)
        self.__redOKButton = Button(self.__nameFrame, \
                                        text = "OK", \
                                        command = self.__setRedName)                                         
        self.__whitePlayerLabel = Label(self.__nameFrame, \
                                        text = "White Team Player Name:")
        self.__whiteNameEntry = Entry(self.__nameFrame, \
                                      width = 10)
        self.__whiteOKButton = Button(self.__nameFrame, \
                                      text = "OK", \
                                      command = self.__setWhiteName)


        # Updating label that displays who's turn it is
        self.__turnLabel = Label(self.__turnFrame, \
                                 text = "Your Turn:")
        '''Code to make the turn label change with each move'''
        self.__turnValue = StringVar()
        self.__displayTurn = Label(self.__turnFrame, \
                                   textvariable = self.__turnValue)
        

        # Updating label that tells user if their move was valid or invalid
        self.__moveAnalysisLabel = Label(self.__turnFrame, \
                                         text = "Move Analysis:")
        '''Code to make the move analysis label change with each move'''
        self.__analysisValue = StringVar()
        self.__displayAnalysis = Label(self.__turnFrame, \
                                       textvariable = self.__analysisValue)

        # Organize titleFrame
        self.__startGameLabel.grid(   column = 0, row = 0)

        # Organize nameFrame
        self.__redPlayerLabel.grid(   column = 0, row = 1)
        self.__redNameEntry.grid(     column = 1, row = 1)
        self.__redOKButton.grid(      column = 2, row = 1)
        self.__whitePlayerLabel.grid( column = 0, row = 2)
        self.__whiteNameEntry.grid(   column = 1, row = 2)
        self.__whiteOKButton.grid(    column = 2, row = 2)

        # Organize turnFrame
        self.__turnLabel.grid(        column = 0, row = 0)
        self.__displayTurn.grid(      column = 1, row = 0)
        self.__moveAnalysisLabel.grid(column = 0, row = 1)
        self.__displayAnalysis.grid(  column = 1, row = 1)
        
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

        #Will hold the contents of each space by using the space as a key, with
        #data type being a tuple of integer, corresponding to (row, column).
        # Value of each key will contain a reference to the checker occupying
        #the space if it exists
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
                               image = self.__redChecker, \
                               activebackground = "yellow")
        
        self.__button.grid(row=r, column=c)

    def makeWhiteChecker(self, space, r, c):
        self.__button = Button(self, command=lambda widget=space: \
                               self.__activated(widget), \
                               image = self.__whiteChecker, \
                               activebackground = "yellow")
        
        self.__button.grid(row=r, column=c)

    def makeRedKing(self, space, r, c):
        self.__button = Button(self, command=lambda widget=space: \
                               self.__activated(widget), \
                               image = self.__redKing, \
                               activebackground = "yellow")
        
        self.__button.grid(row=r, column=c)

    def makeWhiteKing(self, space, r, c):
        self.__button = Button(self, command=lambda widget=space: \
                               self.__activated(widget), \
                               image = self.__whiteKing, \
                               activebackground = "yellow")
        
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

    def __setRedName(self):
        redName = self.__redNameEntry.get()

    def __setWhiteName(self):
        whiteName = self.__whiteNameEntry.get()

    def updateTurnValue(self):
        if self.__turn == 1:
            self.__turnValue.set(redName)
        else:
            self.__turnValue.set(whiteName)

    def updateAnalysisValue(self):
#        if checkersEvaluation.invalidMoveMessage():
        self.__analysisValue.set("Invalid Move!")
#        else:
#            self.__analysisValue.set("Nice move, bro")
