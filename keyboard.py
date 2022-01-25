from turtle import *

setup(1400,800)
width(3)
speed(0)
delay(0)
btnSize = 50
btnSize_withDstns = int(btnSize *1.3)
distance = btnSize_withDstns - btnSize
font = int(btnSize/3.3)
x_alph= int(btnSize/2.3)
y_alph= int(btnSize/3.1)
al= "abcdefghijklmnopqrstuvwxyz"

def keyboard(x,y):
    count = 0
    for w in range(2): 
        up()
        goto(x, y - (btnSize_withDstns*w))
        down()
        for l in range(13):
            for i in range(4):
                forward(btnSize)
                left(90)            
            tempx = xcor() 
            tempy = ycor()
            up()
            goto(tempx + x_alph,tempy + y_alph)
            write(al[count], font =("Arial",font,"normal"))
            goto(tempx,tempy)
            forward(65)
            down()
            count +=1
        
         
    
x = -200
y = -150
keyboard(x,y)



def btnclick(xclick,yclick):
    if xclick < x or xclick > x + (13* btnSize_withDstns) - distance:
        return
    dx = abs(xclick - x)
    if dx % btnSize_withDstns > btnSize:
        return
    
    
    if yclick > y+btnSize or yclick < y - btnSize_withDstns:
        return    
    dy = abs(yclick - (y + btnSize))
    if dy % btnSize_withDstns > btnSize:
        return

    
    x1= int(dx//btnSize_withDstns)
    y1= int(dy//btnSize_withDstns)
    #print(x1,y1)
    
    res = 11 * y1 + x1
    #print(res)
    print(al[res])
    
    Grayed_Out_X= x + x1 * btnSize_withDstns
    Grayed_Out_Y= y - y1 * btnSize_withDstns
    #print(Grayed_Out_X, Grayed_Out_Y)
    up()
    goto(Grayed_Out_X, Grayed_Out_Y)
    down()
    color("black","grey")
    begin_fill()
    for i in range(4):
        forward(btnSize)
        left(90)
    end_fill()
    up()
    goto(Grayed_Out_X + x_alph,Grayed_Out_Y + y_alph)
    down() 
    write(al[res], font =("Arial",font,"normal"))
    up()  
    goto(Grayed_Out_X, Grayed_Out_Y)
    


    
onscreenclick(btnclick,1)
done()