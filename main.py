import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def move_left():
    tim.left(20)


def move_rigth():
    tim.right(20)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="b", fun=move_backward)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_rigth)
screen.exitonclick()