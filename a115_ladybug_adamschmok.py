#   a115_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# Draw legs
legCount = 6
legRepeat = 0
ladybug.pensize(5)
while (legRepeat < 3):
  legRepeat += 1
  ladybug.penup()
  ladybug.goto(0,-35)
  ladybug.pendown()
  ladybug.setheading(((180/legCount)*legRepeat)+120)
  ladybug.forward(50)

while (legRepeat < 6 ):
  legRepeat += 1
  ladybug.penup()
  ladybug.goto(0,-35)
  ladybug.pendown()
  ladybug.setheading(((180/legCount)*legRepeat)-150)
  ladybug.forward(50)

# and body
ladybug.penup()
ladybug.setheading(0)
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 0
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots < 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)
    #position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()