import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(7)
t.pensize(2)

#рамка
t.up()
t.goto(0, 300)
t.down()
t.color("black")
t.begin_fill()
for i in range(2):
	t.fd(200)
	t.left(90)
	t.fd(30)
	t.left(90)
	t.end_fill()
		
t.right(90)
t.begin_fill()
for i in range(2):
	t.fd(400)
	t.left(90)
	t.fd(30)
	t.left(90)
t.end_fill()
	
t.fd(400)
t.left(90)
t.fd(30)

screen.mainloop()