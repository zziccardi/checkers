# Ziccardi, Zachary; Donohue, Mark; Kasliwal, Mannan; and Suesser, Marc
# CS110 A52, A53, A53, and A53
# Project: Checkerboard

from tkinter import *
import checkersEvaluation

class Checkerboard(Frame):
    def __init__(self, turn, spaceContents):
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
        self.__redNameEntryVar = StringVar()
        self.__redNameEntryVar.set("Red Player")
        self.__redNameEntry = Entry(self.__nameFrame, \
                                    width = 15,
                                    textvariable = self.__redNameEntryVar)        
        self.__whitePlayerLabel = Label(self.__nameFrame, \
                                        text = "White Team Player Name:")
        self.__whiteNameEntryVar = StringVar()
        self.__whiteNameEntryVar.set("White Player")
        self.__whiteNameEntry = Entry(self.__nameFrame, \
                                      width = 15,
                                      textvariable = self.__whiteNameEntryVar)

        self.__turnLabel = Label(self.__turnFrame, \
                                 text = "Your Turn:")
        self.__turnVar = StringVar()
        self.__turnVar.set(self.__redNameEntryVar.get())
        self.__displayTurn = Label(self.__turnFrame, \
                                   textvariable = self.__turnVar)
        

        # Updating label that tells user if their move was valid or invalid
        self.__moveAnalysisLabel = Label(self.__turnFrame, \
                                         text = "Move Analysis:")
        '''Code to make the move analysis label change with each move'''
        self.__analysisValue = StringVar()
        self.__displayAnalysis = Label(self.__turnFrame, \
                                       textvariable = self.__analysisValue)

        # Organize titleFrame
        self.__startGameLabel.grid(   column = 1, row = 1)

        # Organize nameFrame
        self.__redPlayerLabel.grid(   column = 1, row = 2)
        self.__redNameEntry.grid(     column = 2, row = 2)
        self.__whitePlayerLabel.grid( column = 1, row = 3)
        self.__whiteNameEntry.grid(   column = 2, row = 3)

        # Organize turnFrame
        self.__turnLabel.grid(        column = 1, row = 1)
        self.__displayTurn.grid(      column = 2, row = 1)
        self.__moveAnalysisLabel.grid(column = 1, row = 2)
        self.__displayAnalysis.grid(  column = 2, row = 2)

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

        #Will hold the contents of each space by using the space as a key, with
        #data type being a tuple of integer, corresponding to (row, column).
        # Value of each key will contain a reference to the checker occupying
        #the space if it exists
        self.__spaceContents = spaceContents

        #Reference to the checker currently chosen by the player whose turn it
        #currently is, 0 if no checker is currently chosen
        self.__curChecker = 0

        for i in range(64):
            r = (i // 8) + 1
            c = (i % 8) + 1
            space = (r, c)

            photoFile = self.__getImageFile(space)

            self.__buttons[space] = Button(self, command=lambda widget=space: \
                                   self.__activated(widget), \
                                   image = self.__images[photoFile])
        
            self.__buttons[space].grid(row=r, column=c)

    #Narrative: Retrieves the value of the current turn
    #Precondition: Must be called
    #Postcondition: Returns integer value of turn, 1 or 2
    def getTurn(self):
        return self.__turn

    #Narrative: Changes the turn value to given argument
    #Precondition: Must be called, takes turn as argument (1 or 2)
    #Postcondition: Sets turn to the given value
    def setTurn(self, turn):
        self.__turn = turn

    #Narrative: Retrieves the reference to the currently selected checker
    #Precondition: Must be called
    #Postcondition: Returns reference to the checker, 0 if none
    def getCurChecker(self):
        return self.__curChecker

    #Narrative: Changes the currently assigned checker
    #Precondition: Must be called, takes checker or 0 as an argument
    #Postcondition: Sets currently assigned checker to new checker or 0 (none)
    def setCurChecker(self, curChecker):
        self.__curChecker = curChecker

    #Narrative: Retrieves the dictionary containing all spaces
    #Precondition: Must be called
    #Postcondition: Returns integer value of turn, 1 or 2
    def getSpaceContents(self):
        return self.__spaceContents

    #Narrative: Changes dictionary referring to spaces and their contents
    #Precondition: Must be called, takes spaceContents as argument (dictionary)
    #Postcondition: Changes the value of dictionary containing space contents
    def setSpaceContents(self, spaceContents):
        self.__spaceContents = spaceContents

    #Narrative: Updates label to reflect the move previously made
    #Precondition: Must be called, takes string value message as argument
    #Postcondition: Sets label to given message argument
    def updateAnalysisValue(self, message):
        self.__analysisValue.set(message)

    #Narrative: Adds a checker to the board
    #Precondition: Takes a reference to the checker as an argument
    #Postcondition: Adds checker to the dictionary containing all checkers
    def checkerCreated(self, checker):
        self.__spaceContents[checker.getSpace()] = checker

    #Narrative: Changes the turn values and resets curChecherk
    #Precondition: Reference to the checker board must be passed as an argument
    #Postcondition: Toggles turn attribute on board, resets curChecker and updates
    #               label to reflect changes
    def nextTurn(self):
        if self.__turn == 1:
            self.__turn = 2
            self.__turnVar.set(self.__whiteNameEntryVar.get())
        else:
            self.__turn = 1
            self.__turnVar.set(self.__redNameEntryVar.get())

        self.__curChecker = 0

    #Narrative: Sends the space value to evaluations module to evaluate how event
    #           should be handled within the rules of checkers
    #Precondition: Button must be pressed on the checkerboard
    #Postcondition: Passes space as argument to find how to proceed
    def __activated(self, space):
        checkersEvaluation.spaceClicked(self, space)

    #Narrative: Gets corresponding image reference for a space's conditions
    #Precondition: Must be called and given the space as argument, which is
    #              a tuple of format (row, column)
    #Postcondition: Returns a string value that can be used in the dict of image
    #               files to reference the correct image based on conditions
    #               at that space
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

    #Narrative: Updates images on the checkerboard to refleect changes
    #Precondition: Must be called
    #Postcondition: Gets correct image name for given conditions in each space
    #               then changes the button's image
    def updateBoard(self):
        for i in range(64):
            r = (i // 8) + 1
            c = (i % 8) + 1
            space = (r, c)

            self.__buttons[space].config(image = self.__images[self.__getImageFile(space)])
