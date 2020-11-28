import swampy
from swampy.TurtleWorld import *
import math

print("Turtle Demo")

world = TurtleWorld()
bob = Turtle()


def draw_square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)


def draw_polygon(t, n, l):
    angle = 360.0 / n
    for i in range(n):
        fd(t, l)
        lt(t, angle)


def draw_circle(t, r):
    circumference = 2 * math.pi * r
    steps = 50
    length = circumference / steps
    draw_polygon(t, steps, length)


def demo_draw_polygon():
    print("Draw polygon using turtle")
    num_side = int(input())
    length = 50
    draw_polygon(bob, num_side, length)


def demo_draw_circle():
    print("Drawing Circle..")
    radius = 100
    draw_circle(bob, radius)


# draw_square(bob)

# demo_draw_polygon()

demo_draw_circle()


wait_for_user()

print(bob)
