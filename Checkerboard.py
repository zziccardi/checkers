# Ziccardi, Zachary; Donohue, Mark; Kasliwal, Mannan; and Suesser, Marc
# CS110 A52, A53, A53, and A53
# Project: Checkerboard

from tkinter import *
import checkersEvaluation

class Checkerboard(Frame):
    def __init__(self, turn, checker, spaceContents, redName="", whiteName=""):
        Frame.__init__(self)
        self.master.title("Checkerboard")
        self.grid()

        # New Frame for menu title
        self.__titleFrame = Frame(self)
        self.__titleFrame.grid(column = 9, row = 1)

        # New Frame for Names
        self.__nameFrame = Frame(self)
        self.__nameFrame.grid(column = 9, row = 2, padx = 30)

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
                                    width = 15)
        self.__redNameEntry.insert(0, "Red Player")
        
        self.__whitePlayerLabel = Label(self.__nameFrame, \
                                        text = "White Team Player Name:")
        self.__whiteNameEntry = Entry(self.__nameFrame, \
                                      width = 15)
        self.__whiteNameEntry.insert(0, "White Player")

        self.__turnLabel = Label(self.__turnFrame, \
                                 text = "Your Turn:")
        
        self.__displayTurn = Label(self.__turnFrame, \
                                   text = self.__redNameEntry.get())
        

        # Updating label that tells user if their move was valid or invalid
        self.__moveAnalysisLabel = Label(self.__turnFrame, \
                                         text = "Move Analysis:")
        '''Code to make the move analysis label change with each move'''
        self.__analysisValue = StringVar()
        self.__displayAnalysis = Label(self.__turnFrame, \
                                       textvariable = self.__analysisValue, \
                                       justify = LEFT)

        # Organize titleFrame
        self.__startGameLabel.grid(   column = 0, row = 0)

        # Organize nameFrame
        self.__redPlayerLabel.grid(   column = 0, row = 1)
        self.__redNameEntry.grid(     column = 1, row = 1)
        self.__whitePlayerLabel.grid( column = 0, row = 2)
        self.__whiteNameEntry.grid(   column = 1, row = 2)

        # Organize turnFrame
        self.__turnLabel.grid(        column = 0, row = 0)
        self.__displayTurn.grid(      column = 1, row = 0)
        self.__moveAnalysisLabel.grid(column = 0, row = 1)
        self.__displayAnalysis.grid(  column = 1, row = 1)

        self.__images = {}
        self.__images["red"] = PhotoImage(file = "redChecker.gif")
        self.__images["redKing"] = PhotoImage(file = "redCheckerKing.gif")
        self.__images["redHighlighted"] = \
                            PhotoImage(file = "redCheckerHighlighted.gif")
        self.__images["redKingHighlighted"] = \
                            PhotoImage(file = "redCheckerKingHighlighted.gif")
        self.__images["white"] = PhotoImage(file = "whiteChecker.gif")
        self.__images["whiteKing"] = PhotoImage(file = "whiteCheckerKing.gif")
        self.__images["whiteHighlighted"] = \
                            PhotoImage(file = "whiteCheckerHighlighted.gif") 
        self.__images["whiteKingHighlighted"] = \
                            PhotoImage(file = "whiteCheckerKingHighlighted.gif")
        self.__images["blackBlank"] = PhotoImage(file = "blackBlank.gif")
        self.__images["whiteBlank"] = PhotoImage(file = "whiteBlank.gif")

        self.__buttons = {}

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

            photoFile = self.__getImageFile(space)

            self.__buttons[space] = Button(self, command=lambda widget=space: \
                                   self.__activated(widget), \
                                   image = self.__images[photoFile])
        
            self.__buttons[space].grid(row=r, column=c)

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

    def updateTurnValue(self):
        if self.__turn == 1:
            self.__turnLabel = self.__redNameEntry.get()
        else:
            self.__turnLabel = self.__whiteNameEntry.get()

    def updateAnalysisValue(self, message):
        self.__analysisValue.set(message)

    def __activated(self, space):
        checkersEvaluation.spaceClicked(self, space)
        print(space)
        
    def __getImageFile(self, space):
        r = space[0]
        c = space[1]
        checker = self.__spaceContents.get(space, 0)

        photoFile = ""

        if checker:
            if checker.getTeam() == 1:
                photoFile += "red"
            else:
                photoFile += "white"

            if checker.getIsKing():
                photoFile += "King"

            if checker == self.__curChecker:
                photoFile += "Highlighted"
        else:
            if r % 2:
                if c % 2:
                    photoFile += "blackBlank"
                else:
                    photoFile += "whiteBlank"
            else:
                if c % 2:
                    photoFile += "whiteBlank"
                else:
                    photoFile += "blackBlank"

        return photoFile
        
    def updateBoard(self):
        for i in range(64):
            r = (i // 8) + 1
            c = (i % 8) + 1
            space = (r, c)

            self.__buttons[space].config(image = self.__images[self.__getImageFile(space)])
