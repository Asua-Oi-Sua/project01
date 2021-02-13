import turtle
import array 

FONT = ("Arial", 8, "bold")

pos  = []

t = turtle.Turtle()
# draw big circle
t.circle(50)
# t.up() 
# t.setpos(0, -5)
# t.down()
# t.circle(5)

t.up() 
# move back to mid point
t.setpos(0,50)
# turn right 120 degree
t.right(120)
# forward radius
t.forward(50)
t.down()
pos.append(t.pos())
t.circle(5)

t.up() 
# move back to mid point
t.setpos(0,50)
# turn right 120 degree
t.right(120)
# forward radius
t.forward(50)
t.down()
pos.append(t.pos())
t.circle(5)

t.up() 
# move back to mid point
t.setpos(0,50)
# turn right 120 degree
t.right(120)
# forward radius
t.forward(50)
t.down()
pos.append(t.pos())
t.circle(5)

print(pos)

# write label
num=0
for x in pos:
    t.up()
    t.setpos(x)
    t.write(str(num+1), font=FONT)
    num = num + 1
    t.down()

# draw line

t.up()
t.setpos(pos[0])
t.down()
t.goto(pos[1])

t.up()
t.setpos(pos[1])
t.down()
t.goto(pos[2])

t.up()
t.setpos(pos[2])
t.down()
t.goto(pos[0])


input("Press Enter to continue...")