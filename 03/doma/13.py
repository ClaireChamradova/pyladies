#nocni obloha

from turtle import forward, left, right, exitonclick, shape, penup, pendown

#mesic
left(30)
for mesic in range(30):
    forward(3)
    right(180-(180*(1-(2/40))))
right(120)
for mesicnibrisko in range(14):
    forward(3)
    left(180-(180*(1-(2/30))))

penup()
forward(60)
pendown()
left(100)

#hvezda
for hvezdy in range(1):
    for prvnikolohvezd in range(4): #okolo mesice
        for hvezda in range(6): #jedna hvezda
            forward(10)
            left(120)
            forward(10)
            right(60)
        pocet = prvnikolohvezd
        #print (pocet)
        penup()
        forward(130+(pocet*20))
        left(90)
        pendown()
    for druhekolohvezd in range(5):
        for hvezda in range(6):
            forward(10)
            left(120)
            forward(10)
            right(60)
        pocet = prvnikolohvezd + druhekolohvezd + 1
        #print (pocet)
        penup()
        forward(130+(pocet*20))
        left(180-(180*(1-(2/5))))
        pendown()


exitonclick()