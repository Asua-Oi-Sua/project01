#Program to draw spiral circles in Python Turtle
import turtle
  
t = turtle.Turtle()
for i in range(1000):
  t.circle(10+(i/10), 5)