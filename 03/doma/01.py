from turtle import forward, left, right, exitonclick, shape, penup, pendown

shape('turtle')
k = 50*(2**(1/2))

for vesnice in range(5):
    for pohyb in range(4):
        forward(50)
        left(90)
    left(45)
    forward(k)
    for vnitrnicary in range(2):
        left(90)
        forward(k/2)
    left(90)
    forward(k)
    left(45)
    forward(20)

exitonclick()