from turtle import *
setup(1250, 400 )
width(3)
speed(0)
delay(0)
btnSize = 50
btnSize_withDstns = int(btnSize * 1.3)
distance = btnSize_withDstns - btnSize
font = int(btnSize / 3.3)
x_alph = int(btnSize / 2.3)
y_alph = int(btnSize / 3.1)

al= "abcdefghijklmnopqrstuvwxyz"
x = -245
y = -100
tt2 = Turtle()
tt2.speed(0)
tt2.ht()
ht()
title("Gallows")

def goToCoords(word):
    center = (11 - len(word)) // 2
    up()
    x_cell = x + btnSize_withDstns * center
    y_cell = y + btnSize_withDstns * 3
    goto(x_cell, y_cell)
    down()

class View:
    def __init__(self, sendCharFunc, newGameFunc):
        self.sendCharFunc = sendCharFunc
        self.newGameFunc = newGameFunc

    def run(self):
        done()

    def newGame(self, word):
        clear()
        self.keyboard(x, y)
        self.background(0)
        self.drawCell(word)
        self.drawWords(word)
        onscreenclick(self.btnclick)

    def keyboard(self, x, y):
        color("black")
        count = 0
        for w in range(2):
            up()
            goto(x, y - (btnSize_withDstns * w))
            down()
            for l in range(13):
                for i in range(4):
                    forward(btnSize)
                    left(90)
                tempx = xcor()
                tempy = ycor()
                up()
                goto(tempx + x_alph, tempy + y_alph)
                write(al[count], font=("Arial", font, "normal"))
                goto(tempx, tempy)
                forward(65)
                down()
                count += 1

    def drawCell(self, word):
        if len(word) > 11:
            bbt_s = 40
            center = (11 * btnSize) - (len(word) * bbt_s)
            up()
            x_cell = x + center
            y_cell = y + btnSize_withDstns * 3
            goto(x_cell, y_cell)
            down()
        else:
            goToCoords(word)
            bbt_s = 65
        for i in range(len(word)):
            for j in range(4):
                forward(bbt_s)
                left(90)
            up()
            forward(bbt_s)
            down()

    def btnclick(self, xclick, yclick):
        if xclick < x or xclick > x + (13* btnSize_withDstns) - distance:
            return
        dx = abs(xclick - x)
        if dx % btnSize_withDstns > btnSize:
            return

        if yclick > y + btnSize or yclick < yclick < y - btnSize_withDstns:
            return
        dy = abs(yclick - (y + btnSize))
        if dy % btnSize_withDstns > btnSize:
            return

        x1 = int(dx // btnSize_withDstns)
        y1 = int(dy // btnSize_withDstns)

        res = 13 * y1 + x1

        Grayed_Out_X = x + x1 * btnSize_withDstns
        Grayed_Out_Y = y - y1 * btnSize_withDstns
        # print(Grayed_Out_X, Grayed_Out_Y)
        up()
        goto(Grayed_Out_X, Grayed_Out_Y)
        down()
        color("black", "grey")
        begin_fill()
        for i in range(4):
            forward(btnSize)
            left(90)
        end_fill()
        up()
        goto(Grayed_Out_X + x_alph, Grayed_Out_Y + y_alph)
        down()
        write(al[res], font=("Arial", font, "normal"))
        up()
        goto(Grayed_Out_X, Grayed_Out_Y)
        self.sendCharFunc(al[res])
        # if penalty == 0:
        # bgpic("giphy/0.gif")
        # while penalty != 7:
        # penalty =+1
        # bgpic(f"giphy/[penalty].gif")

    def drawWords(self, word):
        tt2.clear()
        if len(word) > 11:
            bbt_s = 40
            center = (11 * btnSize) - (len(word) * bbt_s)
            x_cell = x + center
            y_cell = y + btnSize_withDstns * 3
        else:
            bbt_s = 65
            center = (11 - len(word)) // 2
            x_cell = x + btnSize_withDstns * center
            y_cell = y + btnSize_withDstns * 3
        tt2.up()
        tt2.goto(x_cell, y_cell)
        for i in range(len(word)):
            tempx = tt2.xcor()
            tempy = tt2.ycor()
            # print(x_cell, y_cell)
            if len(word) <= 11 and word[i] != "*":
                textS = 50
                dis_x = 20
                dis_y = 10
            if len(word) <= 11 and word[i] == "*":
                textS = 72
                dis_x = 20
                dis_y = -23
            if len(word) >= 11 and word[i] != "*":
                textS = 30
                dis_x = 12
                dis_y = 6
            if len(word) >= 11 and word[i] == "*":
                textS = 19
                dis_x = 17
                dis_y = 5
            tt2.goto(tempx + dis_x, tempy + dis_y)
            tt2.down()
            tt2.write(word[i], font=("Arial", textS, "normal"))
            tt2.up()
            tt2.goto(tempx, tempy)
            tt2.forward(bbt_s)

    def background(self, penalties):
        bgpic(f"img/pic{penalties}.gif")

    def printSign(self, isWinner = True):
        up()
        goto(150,-40)
        down()
        if isWinner:
            text = "You win!"
            color("Green")
        else:
            text = "You loose..."
            color("Red")
        write(text, font=("Arial", 100, "bold"), move=False, align='center')
        onscreenclick(self.newGameFunc)

if __name__ == "__main__":
    def fp(someFunc):
        someFunc("hjdsgvjh")

    def ng(x,y):
        view.newGame("***new***")

    def f(letter):
        fp(print)
        print(">>>>", letter)


    view = View(f, ng)
    view.newGame("**dffg**")
    view.printSign()
    #view.newGame("abc***")
    view.run()