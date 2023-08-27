import data_generation as generate
import mean_grouping as group
from Data_Display import Scatter
from random import randint
import turtle

scatterTurtle = turtle.Turtle()

data = generate.generate_uncorrelated(100, [-100,-100], [100,100],2)
data = group.split(data, 5)
scatterTurtle.color("blue")
Scatter.draw_group(data[0], scatterTurtle)
scatterTurtle.color("yellow")
Scatter.draw_group(data[1], scatterTurtle)
scatterTurtle.color("red")
Scatter.draw_group(data[2], scatterTurtle)
scatterTurtle.color("Orange")
Scatter.draw_group(data[3], scatterTurtle)
scatterTurtle.color("purple")
Scatter.draw_group(data[4], scatterTurtle)
input()
scatterTurtle.clear()
for i in range(20):
    averages = group.find_averages(data,2)
    data = group.reassign(data, averages)
    data = group.remove_groups(data)
scatterTurtle.color("black")
Scatter.draw_group(group, scatterTurtle)
turtle.colormode(255)
for group in data:
    scatterTurtle.color(randint(0,255),randint(0,255),randint(0,255))
    Scatter.draw_group(averages, scatterTurtle)
input()
