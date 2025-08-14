import turtle

screen =turtle.Screen()
screen.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.up()

black = (0, 0, 0)
purple = (131, 8, 175)
steps = 100
half = steps // 2
height = 300
width = 200

step_height = height / steps

def interpoiate_color(c1, c2, factor):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * factor) for i in range(3))

for i in range(steps):
    factor = i / (steps - 1)
    color = interpoiate_color(black, purple, factor)
    y = -height // 2 + i * step_height
    t.goto(-width//2, y)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(step_height)
        t.left(90)
    t.end_fill()
    
#рамка
t.up()
t.goto(-160, 150)
t.down()
t.color("#0a0e48")
t.begin_fill()
for i in range(2):
    t.fd(260)
    t.left(90)
    t.fd(60)
    t.left(90)
t.end_fill()

t.right(90)
t.begin_fill()
for i in range(2):
    t.fd(300)
    t.left(90)
    t.fd(60)
    t.left(90)
t.end_fill()

t.fd(300)

t.begin_fill()
for i in range(2):
    t.fd(60)
    t.left(90)
    t.fd(320)
    t.left(90)
t.end_fill()

t.up()
t.left(90)
t.fd(320)
t.left(90)
t.down()

t.begin_fill()
for i in range(2):
    t.fd(360)
    t.left(90)
    t.fd(60)
    t.left(90)
t.end_fill()

t.hideturtle()
screen.mainloop()