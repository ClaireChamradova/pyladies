
from turtle import forward, left, right, exitonclick, shape, penup, pendown, goto
from random import randrange


for obloha in range(30):#vyber mista hvezdy
    x = randrange (-280,280) 
    y = randrange (-280,280)    
    if ((x <-40 or x > 40)and (x < -200 or x > -100)) and ((y < -40 or y > 40) and (y < 70 or y > 160)):
        penup()
        goto(x, y)
        pendown()
        for hvezda in range(6): #jedna hvezda
            forward(4)
            left(120)
            forward(4)
            right(60)
    else:
        continue
exitonclick()
