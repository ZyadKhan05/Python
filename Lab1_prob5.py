#Question 5
#Inform the User about the program
print('Hello, this program will draw out the Irish Flag out using turtle')

import turtle

#setting the turtle up
turtle.speed(0)
turtle.setup(750, 500)

# Move to starting position
turtle.penup()
turtle.goto(-375, 250)
turtle.pendown()

#Fill in the Green
turtle.color("green")
turtle.begin_fill()
turtle.forward(250)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(250)
turtle.end_fill()

#Reset pen back to next starting spot
turtle.right(180)
turtle.forward(250)

#Fill in the White (even though you can skip it)
turtle.color("white")
turtle.begin_fill()
turtle.left(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(500)
turtle.end_fill()

#Reset pen back to next starting spot
turtle.left(90)

#Fill in the orange
turtle.color("orange")
turtle.begin_fill()
turtle.forward(250)
turtle.left(90)
turtle.forward(500)
turtle.left(90)
turtle.forward(250)
turtle.end_fill()

#Hide the pointer
turtle.hideturtle()
turtle.done()
