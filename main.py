import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Helicopter game")
wn.setup(730, 550)
wn.tracer(0)

seperation = turtle.Turtle()
seperation.color("white")
seperation.shape("square")
seperation.speed(0)
seperation.penup()
seperation.sety(190)
seperation.shapesize(0.3, 20)

seperation2 = turtle.Turtle()
seperation2.color("white")
seperation2.shape("square")
seperation2.speed(0)
seperation2.penup()
seperation2.sety(240)
seperation2.shapesize(0.3, 20)

pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.speed(0)
pen2.penup()
pen2.shape("square")
pen2.color("white")
pen2.goto(0, 200)
font2 = ("terminal"), 18, "normal"
pen2.write("Helicopter game", align="center", font=font2)

pen3 = turtle.Turtle()
pen3.hideturtle()
pen3.speed(0)
pen3.penup()
pen3.shape("square")
pen3.color("red")
pen3.goto(0, 0)
font2 = ("terminal"), 18, "normal"
pen3.write("(Press 'Space' To Begin)", align="center", font=font2)

pen4 = turtle.Turtle()
pen4.hideturtle()
pen4.speed(0)
pen4.penup()
pen4.shape("square")
pen4.color("white")
pen4.goto(0, 100)
font3 = ("terminal"), 18, "normal"
pen4.write("Arrow Keys or Mouse For Movement", align="center", font=font3)

pen5 = turtle.Turtle()
pen5.hideturtle()
pen5.speed(0)
pen5.penup()
pen5.shape("square")
pen5.color("white")
pen5.goto(0, -100)
font4 = ("terminal"), 10, "normal"
pen5.write("Helicopter = 50pts, Tank = 50pts, Anti-Aircraft = 50pts, Bullet = 15pts, Balloon = 100pts", align="center", font=font4)

pen6 = turtle.Turtle()
pen6.hideturtle()
pen6.speed(0)
pen6.penup()
pen6.shape("square")
pen6.color("white")
pen6.goto(0, 160)
font5 = ("terminal"), 10, "normal"

pen7 = turtle.Turtle()
pen7.hideturtle()
pen7.speed(0)
pen7.penup()
pen7.shape("square")
pen7.color("white")
pen7.goto(0, 70)
font6 = ("terminal"), 18, "normal"
pen7.write("Press 'Space' for Missile and 'B' for Bomb", align="center", font=font6)

def start():
    seperation2.hideturtle()
    seperation.hideturtle()
    seperation.color("black")
    seperation2.color("black")
    pen2.clear()
    pen3.clear()
    pen4.clear()
    pen5.clear()
    pen6.clear()
    pen7.clear()
    import helicopter

turtle.listen()
turtle.onkey(start,"space")

wn.mainloop()
