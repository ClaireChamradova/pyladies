#okno se zelvou po pridani inputu zustava v liste, nevyskakuje tak, aby jej uzivatel videl. Proč? :(

from turtle import forward, left, right, exitonclick, shape, penup, pendown

cislo = int(input('Kolikatiúhelník chceš, aby ti želva vykreslila? (zadej číslo): '))
uhel = 180-(180*(1-(2/cislo)))

shape('turtle')

for pohyb in range(cislo):
    forward(50)
    left(uhel)

exitonclick()