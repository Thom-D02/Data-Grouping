#A program for displaying points in a line graph.
import turtle
t1 = turtle.Turtle()
from random import randint
import math


#Line subroutine for all lines
#Parameters:
# - lines: an array containing all the dictionaries for all lines
# - xMax: an integer defining the length of the positive X axis
# - yMax: an integer defining the length of the positive Y axis
#
#Return: None
#
#Purpose:
# Draws all the lines held in the lines parameter on the same axis (and scale)
#Process:
#For each line in line:

def lines(lines, xMax, yMax): #draws all lines
    trueXMax = 0
    trueXMin = 0
    trueYMax = 0
    trueYMin = 0
    for oneLine in lines:
        if trueXMax < max(oneLine.keys()):
            trueXMax = max(oneLine.keys())
        if trueXMin > min(oneLine.keys()):
            trueXMin = min(oneLine.keys())
        if trueYMax < max(oneLine.values()):
            trueYMax = max(oneLine.values())
        if trueYMin > min(oneLine.values()):
            trueYMin = min(oneLine.values())
    xRatio, yRatio = scale(xMax, yMax, trueXMax, trueYMax)
    axis(trueXMax, trueYMax, trueXMin, trueYMin, xRatio, yRatio)
    for oneLine in lines:
        red = randint(0,255)
        blue = randint(0,255)
        green = randint(0,255)
        line(oneLine, xRatio, yRatio, red, blue, green)

def scale(xMax, yMax, pointXMax, pointYMax): #calculates the x and y scales for user defined size
    xRatio = xMax/pointXMax
    yRatio = yMax/pointYMax
    return xRatio, yRatio

def line(points, xRatio, yRatio, red, blue, green): #draws one line
    turtle.colormode(255)
    t1.penup()
    t1.color((red, blue, green))
    t1.goto(min(points.keys())*xRatio, points[min(points.keys())]*yRatio)
    t1.pendown()
    for X in points.keys():
        t1.goto(X*xRatio, points[X]*yRatio)
    t1.ht()

def axis(pointXMax, pointYMax, pointXMin, pointYMin, xRatio, yRatio):
    t1.penup()
    t1.goto(pointXMax*xRatio, 0)
    t1.pendown()
    t1.write(pointXMax)
    t1.goto(pointXMin*xRatio,0)
    t1.write(pointXMin)
    t1.goto(0,0)
    t1.goto(0,pointYMax*yRatio)
    t1.write(pointYMax)
    t1.goto(0,pointYMin*yRatio)
    t1.goto(0,0)

#line({1:1,2:4,3:8,4:5,5:20,6:21, 7:20, 8:16}, 200, 100)

def eqcalc(eqfunc, n1, n2):
    if n1 < n2:
        lower = n1
        upper = n2
    else:
        lower = n2
        upper = n1
    points = {}
    for x in range(lower, upper+1):
        points[x] = eqfunc(x)
    return points

def quadratic(x):
    return x**2

def trochaic(x):
    result = (x**3) - 3*x**2 + 4*x + 5
    return result

def exponential(x):
    result = 2**x
    return result

def sine0(x):
    line0 = math.sin(math.radians(x/2))
    line1 = math.sin(math.radians(x))*2
    #line2 = math.sin(math.radians(x*16))/8
    result = line0 + line1# + line2
    return result*10

def sine1(x):
    n1 = math.sin(math.radians(x))
    n2 = math.sin(math.radians(x*2))
    result = n1 + n2
    return result*10# + randint(-10,10)

def sine2(x):
    result = math.sin(math.radians(x*2)) + math.sin(math.radians(x/2))
    return result * 10

def sine3(x):
    result = sine1(x) + sine2(x)
    return result

def sine4(x):
    result = sine3(x/2) - sine0(x/2)
    return result/2.5 + 20

def diff0(x):
    result = sine0(x) - sine0(x-1)
    return result

def exp0(x):
    result = x**x
    return result


if __name__ == "__main__":
    points0 = eqcalc(sine0, 0, 1000)
    points1 = eqcalc(sine1, 0, 1000)
    points2 = eqcalc(sine2, 0, 500)
    points3 = eqcalc(sine3, 0, 500)
    points4 = eqcalc(sine4, 0, 500)
    points5 = eqcalc(diff0, 0, 1000)
    points6 = eqcalc(sine4, 0, 1000)
    t1.ht()
    #points2 = eqcalc(quadratic, -10, 10)
    lines([points6, points5, points0, points1],300,300)
    input()
