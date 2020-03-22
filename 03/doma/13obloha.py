
from turtle import forward, left, right, exitonclick, shape, penup, pendown, goto
from random import randrange

#mesic
left(30)
for mesic in range(30):
    forward(3)
    right(180-(180*(1-(2/40))))
right(120)
for mesicnibrisko in range(14):
    forward(3)
    left(180-(180*(1-(2/30))))


for obloha in range(35):#vyber mista hvezdy
    x = randrange (-280,280) 
    y = randrange (-280,280)    
    if ((x <-40 or x > 40)and (x < -200 or x > -100)) and ((y < -40 or y > 40) and (y < 70 or y > 160)): #kromě oblasti měsíce a rakety
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

#raketa
penup()

goto(-150, 100) #tělorakety
pendown()
right(135)
forward(30)
left (45)
forward(15)
left (90)
forward(15)
left(45)
forward(30)
goto(-150, 100)

left(180) #pravékřidýlkorakety
forward(15)
right(150)
forward (10)
right(30)
forward (15)
right (150)
forward (10)
left(60)

forward(((2**(1/2))*15)/2) #středníkřidýlkorakety
right(90)
forward(15)
right(180)
forward(20)
right(180)
forward(5)

left(90) #levékřidýlkorakety
forward(((2**(1/2))*15)/2)
right(90)
forward(15)
left(150)
forward(10)
left(30)
forward(15)
left(150)
forward(10)
right(150)

penup() #trysky
forward(10)
pendown()
forward(10)
penup()

left(90)
forward((2**(1/2))*15)
left(90)
pendown()
forward(10)
penup()
left(90)

forward(((2**(1/2))*15)/4)
pendown()
left(90)
forward(15)
penup()
right(90)

forward(((2**(1/2))*15)/2)
pendown()
right(90)
forward(15)
penup()
right(90)

forward(((2**(1/2))*15)/4)
right(90)
pendown()
forward(25)

exitonclick()