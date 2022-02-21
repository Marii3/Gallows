from model import *
from view import *

def turn(letter):
    if model.getLives() > 0 and not model.checkWin():
        res = model.turn(letter)
        print(res, letter)
        if res == 0:
            return
        if res == 1:
            view.background(model.penalty)
        view.drawWords(model.getVisible())
        return
    if model.getLives():
        view.printSign()
    else:
        view.printSign(False)


    
def sign(x, y):
    model.newGame()
    view.newGame(model.getVisible())
    
    

view = View(turn, sign)
model = Model(7)
view.newGame(model.getVisible())

view.run()