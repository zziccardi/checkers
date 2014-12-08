#test

#Ziccardi, Donohue, Kasliwal, Suesser
#CS110 A53
#Project: Checkerboard

from tkinter import *
import checkersEvaluation

class Checkerboard(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Checkerboard")
        self.grid()

        self.__redChecker = PhotoImage(file = "redChecker.gif")
        self.__whiteChecker = PhotoImage(file = "whiteChecker.gif")
        self.__blackBlank = PhotoImage(file = "blackBlank.gif")
        self.__whiteBlank = PhotoImage(file = "whiteBlank.gif")

        spaceContents = checkersEvaluation.getSpaces()

        for i in range(64):
            r = (i // 8) + 1
            c = (i % 8) + 1
            space = (r, c)

            checker = spaceContents.get(space, 0)

            if r % 2:
                if c % 2 and checker:
                    if checker.getTeam() == 1:
                        self.makeRedChecker(space, r, c) 
                        
                    else:
                        self.makeWhiteChecker(space, r, c)
                        
                elif checker:
                    if checker.getTeam() == 1:
                        self.makeRedChecker(space, r, c)
                        
                    else:
                        self.makeWhiteChecker(space, r, c)
                        
                elif c % 2:
                    self.makeBlackBlank(space, r, c)
                    
                else:
                    self.makeWhiteBlank(space, r, c)
                    
            else:
                if c % 2 and checker:
                    if checker.getTeam() == 1:
                        self.makeRedChecker(space, r, c)
                    else:
                        self.makeWhiteChecker(space, r, c)
                        
                elif checker:
                    if checker.getTeam() == 1:
                        self.makeRedChecker(space, r, c)
                        
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

    def __activated(self, space):
        checkersEvaluation.spaceClicked(self, space)
        print(space)
