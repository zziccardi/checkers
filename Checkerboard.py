# Ziccardi, Zachary; Donohue, Mark; Kasliwal, Mannan; and Suesser, Marc
# CS110 A52, A53, A53, and A53
# Project: Checkerboard

from tkinter import *
import checkersEvaluation

class Checkerboard(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.master.title("Checkerboard")
        self.grid()
        self.__redChecker = PhotoImage(file = "redChecker.gif")
        self.__whiteChecker = PhotoImage(file = "whiteChecker.gif")
        self.__whiteBlank = PhotoImage(file = "whiteBlank.gif")
        self.__blackBlank = PhotoImage(file = "blackBlank.gif")

        spaceContents = checkersEvaluation.getSpaces()

        for i in range(64):
            r = (i // 8) + 1
            c = (i % 8) + 1
            space = (r, c)
            
            checker = spaceContents.get(space, 0)

            if r % 2:
                if c % 2 and checker:
                    if checker.getTeam() == 1:
                        color = "Yellow"
                    else:
                        color = "Blue"
                elif checker:
                    if checker.getTeam() == 1:
                        color = "Yellow"
                    else:
                        color = "Blue"
                elif c % 2:
                    color = "Red"
                else:
                    color = "Black"
            else:
                if c % 2 and checker:
                    if checker.getTeam() == 1:
                        color = "Yellow"
                    else:
                        color = "Blue"
                elif checker:
                    if checker.getTeam() == 1:
                        color = "Yellow"
                    else:
                        color = "Blue"
                elif c % 2:
                    color = "Black"
                else:
                    color = "Red"
                    
            self.__button = Button(self,
                                   height=4,
                                   width=8,
                                   command=lambda widget=space: \
                                   self.__activated(widget),
                                   bg=color,
                                   fg=color,
                                  )

            self.__button.grid(row=r, column=c)
            
    def __activated(self, space):
        checkersEvaluation.spaceClicked(self, space)
        print(space)
