from turtle import *
speed(7) # fastest
side = 8
for i in range(side):
    for i in range(side):
        for i in range(side):
            fd(50)
            lt(360/side)
            dot(2)
        fd(50)
        lt(360/side)
    fd(100)
    lt(360/side)
hideturtle()
mainloop()
