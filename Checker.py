## Kasliwal, Mannan, Ziccardi, Zach, Suesser, Marc, Donohue, Mark
## CS110 Sections A53, A52, A53, A53
## Project: Checker

class Checker:
    def __init__(self, isKing, space, team):
        self.__isKing = isKing
        self.__space = space
        self.__team = team

    def setIsKing(self, isKing):
        self.__isKing = isKing

    def setSpace(self, space):
        self.__space = space

    def setTeam(self, team):
        self.__team = team

    def getIsKing(self):
        return self.__isKing

    def getSpace(self):
        return self.__space

    def getTeam(self):
        return self.__team

    def __str__(self):
        return "King?: " + str(self.__isKing) + \
               "\nRow: " + str(self.__space[0]) + \
               "\nColumn: " + str(self.__space[1]) + \
               "\nTeam:: " + str(self.__team)

##def main():
##    piece = Checker(False, "B1", "1")
##    print(piece)
##
##main()
