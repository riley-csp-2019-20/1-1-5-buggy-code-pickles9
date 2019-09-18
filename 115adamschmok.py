#   a115_buggy_image.py
import turtle as trtl

#create body
drawer = trtl.Turtle()
drawer.pensize(40)
drawer.penup()
drawer.goto(0,-20)
drawer.pendown()
drawer.circle(20)

#configure legs
legs = 8
length = 100
leg_angle = 180 / legs
drawer.pensize(5)
counter = 0
drawer.penup()
eye = 0
drawer.goto(10,20)
while (eye < 0):
eye = eye + 1
drawer.pencolor("red")
drawer.pendown()
drawer.circle(5)
drawer.pencolor("black")
drawer.penup()
drawer.goto(-10,20)
#draw legs
while (counter < (legs/2)):
  drawer.goto(0,0)
  drawer.pendown()
  drawer.setheading((leg_angle*counter)-leg_angle)
  drawer.forward(length)
  counter = counter + 1
while (counter < legs):
  drawer.goto(0,0)
  drawer.setheading((leg_angle*counter)-leg_angle+65)
  drawer.forward(length)
  counter = counter + 1

drawer.penup()

drawer.hideturtle()
wn = trtl.Screen()
wn.mainloop() 