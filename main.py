from turtle import Turtle, Screen
timmy_the_turtle = Turtle()
screen = Screen()


def move_forward():
    timmy_the_turtle.forward(10)


def move_backwards():
    return 'a'


def move_counter_clockwise():
    return 'a'


def move_clockwise():
    return 'a'


screen.listen()
screen.onkey(key='a', fun=move_forward())
screen.exitonclick()



