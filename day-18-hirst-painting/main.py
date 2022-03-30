import turtle
from turtle import Turtle, Screen
import random as r

# 10 x 10 dots. each dot is 20 size and spaced around 50
color_list = [(211, 154, 98), (241, 248, 246), (236, 241, 245), (53, 107, 131), (177, 78, 34), (199, 142, 34),
              (116, 156, 171), (123, 80, 98), (124, 175, 157), (226, 197, 130), (190, 88, 110), (55, 38, 19),
              (12, 49, 63), (43, 168, 128), (51, 126, 121), (197, 124, 143), (166, 21, 31), (222, 93, 79),
              (243, 163, 160), (38, 32, 35), (4, 25, 24), (80, 147, 168), (161, 26, 23), (19, 79, 92), (233, 167, 172),
              (175, 207, 187), (101, 127, 158), (165, 203, 210)]

screen = Screen()

ptr = Turtle()
ptr.speed('fastest')
screen.colormode(255)
ptr.penup()
ptr.hideturtle()
ptr.goto(-200, -200)
position = ptr.position()




def draw_hirst_spot_painting(size, dot_size, space):
    for steps in range(1, size):
        for _ in range(size):
            ptr.dot(dot_size, r.choice(color_list))
            ptr.pu()
            ptr.fd(space)
            ptr.pd()
        ptr.pu()
        ptr.goto(position)
        ptr.left(90)
        ptr.fd(space * steps)
        ptr.right(90)


draw_hirst_spot_painting(15, 20, 30)
screen.exitonclick()
