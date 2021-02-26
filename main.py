import turtle as t


tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
screen = t.Screen()


tim.shape("arrow")
for i in range(20):
    tim.forward(10)
    tim.penup()
    tim.forward(5)
    tim.pendown()
screen.exitonclick()
