import turtle
import random
from turtle import Screen

print('The wierd Triangle thingy')
# Triangle Co-ordinates
a = (-250, -300)
b = (0, 300)
c = (250, -300)
triangle_cor = [a, b, c]
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# Create Turtle Screen
screen = Screen()

# Create turtle
tim = turtle.Turtle()
# tim.hideturtle()
tim.shape('turtle')


def get_triangle_cor():
    tim.penup()
    tim.goto(a)
    tim.dot()
    tim.goto(b)
    tim.dot()
    tim.goto(250, -300)
    tim.dot()


def get_midpoint(tri_point: tuple, ran_point: tuple):
    new_point_x = (tri_point[0] + ran_point[0])/2
    new_point_y = (tri_point[1] + ran_point[1])/2

    new_point = (new_point_x, new_point_y)
    return new_point


# Random Point
d = (-30, 100)
tim.speed(0)

# Begin Process
get_triangle_cor()

tim.goto(d)
tim.dot()

for i in range(25000):
    tim.color(random.choice(colours))
    print(i)
    # select random point from triangle
    ran_tri = random.choice(triangle_cor)
    # print(ran_tri)
    rotating_point = get_midpoint(ran_tri, d)
    tim.goto(rotating_point)
    tim.dot()
    d = rotating_point


screen.exitonclick()
