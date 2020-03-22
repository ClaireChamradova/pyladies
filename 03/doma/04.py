
from turtle import forward, left, right, exitonclick, shape, penup, pendown

shape('turtle')

#pravoúhlá spirála
for pohyb in range(20):
    forward(pohyb*5)
    left(90)

#osmiúhlá spirála
for pohyb in range(60):
    forward(pohyb*2)
    left(180-(180*(1-(2/8))))

#spirála, torchu potíž, hodně pokus omyl
for pohyb in range(500):
    forward(pohyb/15)
    left(180-(180*(1-(2/(30)))))

exitonclick()