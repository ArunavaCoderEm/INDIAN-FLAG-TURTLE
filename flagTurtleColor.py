import turtle
turtle.getscreen().bgcolor("burlywood")
godard = turtle.Turtle()
godard.speed(5)
godard.color('red','#400d00')
turtle.title("Coloured Indian Flag")
godard.hideturtle()

# stick
godard.penup()
godard.right(90)
godard.forward(200)
godard.right(90)
godard.forward(200)
godard.left(90)
godard.pendown()
godard.begin_fill()
godard.left(180)
godard.forward(480)
godard.right(90)
godard.forward(30)
godard.right(90)
godard.forward(480)
godard.right(90)
godard.forward(30)
godard.end_fill()
# first block
godard.color('black','#c43400')
godard.penup()
godard.right(180)
godard.forward(30)
godard.left(90)
godard.forward(480)
godard.pendown()
godard.begin_fill()
godard.right(90)
godard.forward(350)
godard.right(90)
godard.forward(100)
godard.right(90)
godard.forward(350)
godard.pendown()
godard.end_fill()
# second block
godard.color('black','white')
godard.begin_fill()
godard.left(90)
godard.forward(100)
godard.left(90)
godard.forward(350)
godard.left(90)
godard.forward(100)
godard.end_fill()
# 3rd block
godard.penup()
godard.left(180)
godard.forward(100)
godard.pendown()
godard.color('black','green')
godard.begin_fill()
godard.forward(100)
godard.right(90)
godard.forward(350)
godard.right(90)
godard.forward(100)
godard.end_fill()
#chakra
godard.penup()
godard.forward(100)
godard.right(90)
godard.forward(125)
godard.right(90)
godard.forward(50)
godard.pendown()
r = 50
godard.circle(r)
godard.left(90)
godard.color('blue')
for i in range (0,50):
    godard.forward(100)
    godard.left(170)

# name
godard.speed(20)
godard.left(60)
godard.penup()
godard.forward(300)
godard.pendown()
godard.right(25)
godard.forward(70)
godard.penup()
godard.left(180)
godard.forward(70)
godard.pendown()
godard.right(70)
godard.forward(40)
godard.right(90)
godard.forward(70)
godard.penup()
godard.right(180)
godard.forward(35)
godard.pendown()
godard.left(70)
godard.forward(50)
godard.penup()
godard.right(180)
godard.forward(65)
godard.pendown()
godard.right(70)
godard.forward(35)
godard.left(180)
godard.forward(70)
godard.circle(-20,290)
godard.right(210)
godard.forward(70)
godard.penup()
godard.left(60)
godard.forward(25)
godard.pendown()
godard.left(90)
godard.forward(70)
godard.left(90)
godard.forward(20)
godard.right(180)
godard.forward(55)
godard.right(90)
godard.forward(70)
godard.right(100)
godard.forward(55)

turtle.done()
