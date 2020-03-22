#kolecko
from turtle import forward, left, right, exitonclick, shape, penup, pendown

shape('turtle')

for pohyb in range(500):
    forward(1)
    left(180-(180*(1-(2/500))))

exitonclick()