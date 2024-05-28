from turtle import *
 
#paint a house

speed(20)
width(7)
color("green")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square


forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

begin_fill()
color("light blue")
penup()
goto(10, 140)
pendown()
left(120)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()

begin_fill()
penup()
goto(190, 180)
pendown()
forward(40)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
end_fill()


exitonclick()

print("lesson1.py")