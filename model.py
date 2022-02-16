class Model:
    def __init__(self, lives):
        f = open("new.txt", "r")
        self.__words = f.read().split("\n")
        self.__lives = lives
        self.newGame()
    
    def newGame(self):
        from random import choice
        self.__word = choice(self.__words)
        print(self.__word)
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.__visible = list(len(self.__word) * "*")
        self.penalty = 0
        return self.__visible
    
    def getLives(self):
        return self.__lives - self.penalty

    def turn(self, char):
        if char not in self.alphabet:
            return 0
        self.alphabet = self.alphabet.replace(char, "")
        penalty = 1
        for i in range(len(self.__word)):
            if self.__word[i] == char:
                self.__visible[i] = char
                penalty = 2
        if penalty == 1:
            self.penalty += 1
        return penalty
    
    def __str__(self):
        return "".join(self.__visible)
    
    def getVisible(self):
        if self.__lives - self.penalty == 0:
            return self.__word        
        return str(self)

    def checkWin(self):
        return "*" not in self.__visible


if __name__ == "__main__":
    game = Model(8)
    print("New game!")
    while game.getLives() > 0 and not game.checkWin():
        print(game)
        res = game.turn(input("Give me letter: "))
        if res == 1:
            print("Miss! Lives:", game.getLives())
    if game.getLives() == 0:
        print("Word was: " + str(game))
        print("you lose!")

    else:
        print(game)
        print("you win!")
        