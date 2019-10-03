#   a117_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
#make horizontal turtle and add it to list
	ht = trtl.Turtle(shape=s)
	horiz_turtles.append(ht)
	ht.penup()
	new_color = horiz_colors.pop()
	ht.fillcolor(new_color)
	ht.goto(-350, tloc)
	ht.setheading(0)
#same thing but for vertical turtle
	vt = trtl.Turtle(shape=s)
	vert_turtles.append(vt)
	vt.penup()
	new_color = vert_colors.pop()
	vt.fillcolor(new_color)
	vt.goto( -tloc, 350)
	vt.setheading(270)
  
	tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

steps = 0
while steps < 50:
	steps = steps + 1
	for htrtl in horiz_turtles:
		for vtrtl in vert_turtles:
			htrtl.forward(10)
			vtrtl.forward(10)
			hx = htrtl.xcor()
			hy = htrtl.ycor()
			vx = vtrtl.xcor()
			vy = vtrtl.ycor()
			if(abs(hx-vx)<20 and abs(hy-vy)<20):
				htrtl.fillcolor("grey")
				vtrtl.fillcolor("grey")
				horiz_turtles.remove(htrtl)
				vert_turtles.remove(vtrtl)


wn = trtl.Screen()
wn.mainloop()
