## Kasliwal, Mannan, Ziccardi, Zach, Suesser, Marc, Donohue, Mark
## CS110 Sections A53, A52, A53, A53
## Project: Checker

class Checker:
    def __init__(self, isKing, space, team):
        self.__isKing = isKing
        self.__space = space
        self.__team = team

    #Narrative: Changes the value of the checker's king status
    #Precondition: Must be called, takes boolean as argument
    #Postcondition: Sets king status to the passed-in value of T/F
    def setIsKing(self, isKing):
        self.__isKing = isKing
        
    #Narrative: Changes the value of the checker's space
    #Precondition: Must be called, takes space value as argument, which must
    #              be a tuple of format (row, column)
    #Postcondition: Sets space to the passed-in value
    def setSpace(self, space):
        self.__space = space

    #Narrative: Changes the value of the checker's team
    #Precondition: Must be called, takes team value as argument
    #Postcondition: Sets team value to the passed-in value
    def setTeam(self, team):
        self.__team = team

    #Narrative: Retrieves the value indicating whether or not checker is kinged
    #Precondition: Must be called
    #Postcondition: Returns T/F depending on king status
    def getIsKing(self):
        return self.__isKing

    #Narrative: Retrieves the value of the checker's space
    #Precondition: Must be called
    #Postcondition: Returns the space value the checker occupies on board
    def getSpace(self):
        return self.__space

    #Narrative: Retrieves the value of the checker's team
    #Precondition: Must be called
    #Postcondition: Returns the team value
    def getTeam(self):
        return self.__team

    def __str__(self):
        return "King?: " + str(self.__isKing) + \
               "\nRow: " + str(self.__space[0]) + \
               "\nColumn: " + str(self.__space[1]) + \
               "\nTeam: " + str(self.__team)
