import turtle

turtle_screen = turtle.Screen()

monte = turtle.Turtle()
monte.shape("turtle")

def move_forward():
    monte.forward(30)

def turn_left():
    monte.left(45)

def turn_right():
    monte.right(45)

def exit():
    turtle_screen.bye()

def clear():
    monte.clear()

def run_to_position(x,y):
    monte.goto(x, y)

turtle_screen.onkey(move_forward, "Up")
turtle_screen.onclick(run_to_position)
turtle_screen.onkey(turn_left, "Left")
turtle_screen.onkey(turn_right, "Right")
turtle_screen.onkey(exit, "q")
turtle_screen.onkey(exit, "Escape")
turtle_screen.onkey(clear, "c")

turtle_screen.listen()
turtle_screen.mainloop()