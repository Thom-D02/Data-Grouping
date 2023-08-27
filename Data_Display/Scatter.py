#displays the data

import turtle


def point_draw(point, Turtle): #draws a cross at the point
    Turtle.penup()
    Turtle.goto(point[0], point[1])
    Turtle.pendown()
    Turtle.setheading(90)
    Turtle.forward(4)
    Turtle.back(8)
    Turtle.forward(4)
    Turtle.setheading(0)
    Turtle.forward(4)
    Turtle.back(8)
    Turtle.penup()

def circle(centre, radius): #generates a set of points for a circle, to represent groups in a scatter graph
    xs = [x for x in range(-radius, radius+1)]
    ys = [(radius**2 - x**2)**0.5 for x in xs]
    points = []
    for X in range(len(xs)): #adding points for the top of the circle
        points.append([xs[X] + centre[0], ys[X] + centre[1]])
    for X in range(len(xs)-1, -1, -1): #adding points for the bottom of the circle
        points.append([xs[X] + centre[0], centre[1] - ys[X]])
    return points

def draw_group(points, Turtle):
    for point in points:
        point_draw(point, Turtle)

if __name__ == "__main__":
    Turtle = turtle.Turtle()
    Turtle.color("Blue")
    Turtle.penup()
    points = circle([0,50], 25)
    Turtle.goto(points[0][0], points[0][1])
    Turtle.pendown()
    for X in range(0, len(points), 5):
        point_draw(points[X], Turtle)
    turtle.ht()

