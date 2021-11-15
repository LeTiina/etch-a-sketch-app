from turtle import Turtle, Screen
timmy_the_turtle = Turtle()
screen = Screen()


def move_forward():
    timmy_the_turtle.forward(10)


def move_backwards():
    timmy_the_turtle.backward(10)


def move_counter_clockwise():
    timmy_the_turtle.left(10)


def move_clockwise():
    timmy_the_turtle.right(10)

def clear_screen():
    screen.resetscreen()

screen.listen()
screen.onkey(key='d', fun=move_forward)
screen.onkey(key='w', fun=move_clockwise)
screen.onkey(key='s', fun=move_counter_clockwise)
screen.onkey(key='a', fun=move_backwards)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()



