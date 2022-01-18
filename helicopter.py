import turtle
import random
import sys

print("You can use the mouse or the arrow keys to play.")

score = 0
lives = 3
fire_count = 0
T_fire_count = 0
A_fire_count = 0

bullet_speed = 0
tank_B_speed = 0
anti_B_speed = 0

wn = turtle.Screen()
wn.title("Helicopter game")
wn.bgcolor("#0097db")
wn.bgpic("Sky_Grad.gif")
wn.setup(width = 600, height = 490)
wn.register_shape("Heli-bit.gif")
wn.register_shape("BHeli-B.gif")
wn.register_shape("Heli-bit2.gif")
wn.register_shape("BHeli-B2.gif")
wn.register_shape("cloud.gif")
wn.register_shape("Tank-B.gif")
wn.register_shape("Mountain.gif")
wn.register_shape("Balloon.gif")
wn.register_shape("Projectile.gif")
wn.register_shape("Anti_Air.gif")
wn.tracer(6)

missile_state = "ready"
bomb_state = "ready"

cloud = turtle.Turtle()
cloud.shape("cloud.gif")
cloud.color("white")
cloud.speed(0)
cloud.penup()
cloud.sety(100)
cloud.dx = -2

mountain = turtle.Turtle()
mountain.shape("Mountain.gif")
mountain.color("gray")
mountain.speed(0)
mountain.penup()
mountain.goto(200, -173)
mountain.dx = -0.4

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.shape("square")
pen.color("black")
pen.goto(0, 200)
font = ("terminal"), 18, "normal"
pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("Heli-bit.gif")
player.setx(-250)
player.dx = 0
player.dy = 0

enemy = turtle.Turtle()
enemy.speed(0)
enemy.penup()
enemy.shape("BHeli-B.gif")
enemy.setx(random.randint(100,300))
enemy.sety(random.randint(-200, 190))
enemy.dx = -0.5
enemy.dy = 0.3

tank = turtle.Turtle()
tank.speed(0)
tank.penup()
tank.shape("Tank-B.gif")
tank.goto(290, -217)
tank.dx = -1

bomb = turtle.Turtle()
bomb.speed(0)
bomb.penup()
bomb.shape("square")
bomb.dy = 0
bomb.hideturtle()
bomb.shapesize(1.2, 0.6)
bomb.goto(-2000, 2000)

missile = turtle.Turtle()
missile.speed(0)
missile.penup()
missile.shape("square")
missile.dx = 0
missile.hideturtle()
missile.shapesize(0.6, 1.2)
missile.goto(-2000, 2000)

balloon = turtle.Turtle()
balloon.speed(0)
balloon.penup()
balloon.shape("Balloon.gif")
balloon.dx = -2

projectile = turtle.Turtle()
projectile.speed(0)
projectile.penup()
projectile.shape("Projectile.gif")
projectile.dx = -8
projectile.setx(2000)

anti_state = "ready"

anti_C = turtle.Turtle()
anti_C.speed(0)
anti_C.penup()
anti_C.shape("Anti_Air.gif")
anti_C.goto(400, -215)
anti_C.dx = -0.65

enemy_B_state = "ready"

enemy_Bullet = turtle.Turtle()
enemy_Bullet.speed(0)
enemy_Bullet.penup()
enemy_Bullet.shape("square")
enemy_Bullet.goto(2000, 2000)
enemy_Bullet.dx = 0
enemy_Bullet.dy = 0
enemy_Bullet.shapesize(0.6, 1.2)
enemy_Bullet.hideturtle()

tank_B_state = "ready"

tank_Bullet = turtle.Turtle()
tank_Bullet.speed(0)
tank_Bullet.penup()
tank_Bullet.shape("square")
tank_Bullet.goto(2000, 2000)
tank_Bullet.dx = 0
tank_Bullet.dy = 0
tank_Bullet.shapesize(0.6, 1.2)
tank_Bullet.hideturtle()

anti_Bullets = []

for _ in range(2):
    anti_Bullet = turtle.Turtle()
    anti_Bullet.speed(0)
    anti_Bullet.penup()
    anti_Bullet.shape("square")
    anti_Bullet.goto(2000, 2000)
    anti_Bullet.shapesize(0.6, 1.2)
    anti_Bullet.hideturtle()
    anti_Bullets.append(anti_Bullet)

def up():
    pass
    player.dy += 3
    if player.dy > 3:
        player.dy = 3

def down():
    player.dy -= 3
    if player.dy < -3:
        player.dy = -3

def right():
    player.dx += 2
    if player.dx > 3:
        player.dx = 3

def left():
    player.dx -= 2
    if player.dx < -2:
        player.dx = -2

def reset_speed():
    player.dx = 0
    player.dy = 0

walkcount = 0
def anim_loop1():
    global walkcount
    if walkcount == 0:
        player.shape("Heli-bit.gif")
        
    walkcount += 1

    if walkcount == 9:
        player.shape("Heli-bit2.gif")

    if walkcount == 9:
        walkcount = 0
        
walkcount2 = 0

def anim_loop2():
    global walkcount2
    if walkcount2 == 0:
        enemy.shape("BHeli-B.gif")

    walkcount2 += 1

    if walkcount2 == 9:
        enemy.shape("BHeli-B2.gif")

    if walkcount2 == 9:
        walkcount2 = 0

def fire_missile():
    global missile_state
    if missile_state == "ready":
        missile_state = "fire"
        missile.showturtle()
        missile.goto(player.xcor() + 40, player.ycor())
        missile.dx += 13
        if missile.dx > 13:
            missile.dx = 13

def fire_bomb():
    global bomb_state
    if bomb_state == "ready":
        bomb_state = "fire"
        bomb.showturtle()
        bomb.goto(player.xcor(), player.ycor() - 40)
        bomb.dy -= 2.5
        if bomb.dy < -2.5:
            bomb.dy = -2.5

def follow_player():
    global bullet_speed
    enemy_Bullet.setheading(enemy_Bullet.towards(player))
    bullet_speed += 8
    if bullet_speed > 8:
        bullet_speed = 8

def enemy_fire():
    global enemy_B_state

    if enemy_B_state == "ready":
        enemy_B_state = "fire"
        enemy_Bullet.showturtle()
        enemy_Bullet.goto(enemy.xcor() - 40, enemy.ycor())
        follow_player()

def tank_fire():
    global tank_B_state
    global tank_B_speed

    if tank_B_state == "ready":
        tank_B_state = "fire"
        tank_Bullet.showturtle()
        tank_Bullet.goto(tank.xcor() - 40, tank.ycor() + 20)
        tank_Bullet.setheading(135)
        tank_B_speed += 6
        if tank_B_speed > 6:
            tank_B_speed = 6

def anti_fire():
    global anti_state
    global anti_B_speed

    if anti_state == "ready":
        anti_state = "fire"

        for anti_Bullet in anti_Bullets:
            anti_Bullet.showturtle()
            anti_Bullet.goto(anti_C.xcor() - 40, anti_C.ycor() + 20)
            anti_B_speed += 1.6
            if anti_B_speed > 1.6:
                anti_B_speed = 1.6


def fire_Count():
    global enemy_B_state
    global tank_B_state
    global fire_count
    global T_fire_count
    
    fire_count += 1
    T_fire_count += 1

    if fire_count == 150:
        enemy_fire()
        fire_count = 0

    if T_fire_count == 70:
        tank_fire()
        T_fire_count = 0

def FC2():
    global anti_state
    global A_fire_count

    A_fire_count += 1

    if A_fire_count == 90:
        anti_fire()
        A_fire_count = 0

def gamespeed():
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
  wn.update()
    
turtle.listen()
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")
turtle.onkeyrelease(reset_speed, "Up")
turtle.onkeyrelease(reset_speed, "Down")
turtle.onkeyrelease(reset_speed, "Right")
turtle.onkeyrelease(reset_speed, "Left")
turtle.onkey(fire_missile, "space")
turtle.onkey(fire_bomb, "b")
player.ondrag(player.goto)

while True:
    enemy_Bullet.forward(bullet_speed)
    tank_Bullet.forward(tank_B_speed)
    
    for anti_Bullet in anti_Bullets:
        anti_Bullet.forward(anti_B_speed)
        anti_Bullet.setheading(anti_Bullet.towards(player))
    
    player.goto(player.dx + player.xcor(), player.dy + player.ycor())
    cloud.setx(cloud.dx + cloud.xcor())
    tank.setx(tank.dx + tank.xcor())
    anti_C.setx(anti_C.dx + anti_C.xcor())
    missile.setx(missile.dx + missile.xcor())
    bomb.sety(bomb.dy + bomb.ycor())
    mountain.setx(mountain.dx + mountain.xcor())
    balloon.setx(balloon.dx + balloon.xcor())
    projectile.setx(projectile.dx + projectile.xcor())
    enemy.goto(enemy.dx + enemy.xcor(), enemy.dy + enemy.ycor())
    
    if cloud.xcor() < -450:
        cloud.sety(random.randint(0, 220,))
        cloud.setx(450)

    if mountain.xcor() < -428:
        mountain.setx(419)

    if player.xcor() < -275:
        player.dx = 0
        player.setx(-275)

    if player.xcor() > 275:
        player.dx = 0
        player.setx(275)

    if player.ycor() > 229:
        player.dy = 0
        player.sety(229)

    if player.ycor() < -210:
        player.dy = 0
        player.sety(-210)

    if missile.xcor() > 325:
        missile.hideturtle()
        missile.setx(-2000)
        missile.sety(2000)
        missile_state = "ready"

    if enemy_Bullet.xcor() < -325:
        enemy_Bullet.setx(2000)
        enemy_Bullet.sety(20000)
        enemy_B_state = "ready"

    if tank_Bullet.xcor() < -325:
        tank_B_state = "ready"

    if enemy_Bullet.ycor() < -200:
        enemy_Bullet.setx(2000)
        enemy_Bullet.sety(-20000)
        enemy_B_state = "ready"

    if enemy_Bullet.ycor() > 200:
        enemy_Bullet.setx(2000)
        enemy_Bullet.sety(20000)
        enemy_B_state = "ready" 
        
    if tank.xcor() < -380:
        tank.setx(random.randint(330, 1000))

    if balloon.xcor() < -380:
        balloon.setx(600)
        balloon.sety(random.randint(-100, 200))

    if enemy.xcor() < 100 or enemy.xcor() > 360:
        enemy.dx *= -1

    if enemy.ycor() < -200 or enemy.ycor() > 170:
        enemy.dy *= -1
        
    if missile.distance(enemy) < 37:
        missile.setx(-2000)
        missile.sety(2000)
        missile.hideturtle()
        missile_state = "ready"
        enemy.sety(random.randint(-150, 160))
        enemy.setx(360)
        pen.clear()
        score += 50
        fire_count = 0
        pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    if bomb.ycor() < -260:
        bomb.hideturtle()
        bomb.setx(-2000)
        bomb.sety(88888888888888)
        bomb_state = "ready"

    if bomb.distance(tank) < 35:
        bomb.setx(-2000)
        bomb.sety(88888888888888)
        bomb.hideturtle()
        bomb_state = "ready"
        tank.setx(random.randint(330, 1000))
        pen.clear()
        score += 50
        T_fire_count = 0
        pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    if missile.distance(tank) < 35:
        missile.setx(-2000)
        missile.sety(88888888888888)
        tank.setx(random.randint(330, 1000))
        missile.hideturtle()
        missile_state = "ready"
        pen.clear()
        score += 50
        T_fire_count = 0
        pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    if missile.distance(balloon) < 27:
        missile.setx(-2000)
        missile.sety(88888888888888)
        missile.hideturtle()
        missile_state = "ready"
        balloon.setx(600)
        balloon.sety(random.randint(-100, 200))
        pen.clear()
        score += 100
        pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    if bomb.distance(balloon) < 27:
        bomb.setx(-2000)
        bomb.sety(88888888888888)
        bomb.hideturtle()
        balloon.setx(600)
        balloon.sety(random.randint(-100, 200))
        bomb_state = "ready"
        pen.clear()
        score += 100
        pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    if bomb.distance(enemy) < 37:
        bomb.setx(-2000)
        bomb.sety(88888888888888)
        bomb.hideturtle()
        bomb_state = "ready"
        enemy.sety(random.randint(-150, 160))
        enemy.setx(360)
        pen.clear()
        score += 50
        fire_count = 0
        pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    if projectile.distance(player) < 37:
        projectile.setx(2000)
        projectile.sety(player.ycor())
        pen.clear()
        score -= 10
        lives -= 1
        pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    if projectile.xcor() < -380:
        projectile.setx(2000)
        projectile.sety(player.ycor())

    if projectile.xcor() == 1000:
        projectile.sety(player.ycor())

    if enemy_Bullet.distance(player) < 37:
        enemy_Bullet.sety(-2000)
        enemy_Bullet.setx(20000000)
        enemy_Bullet.hideturtle()
        enemy_B_state = "ready"
        pen.clear()
        score -= 10
        lives -= 1
        pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    for anti_Bullet in anti_Bullets:
        if missile.distance(anti_Bullet) < 20:
            anti_Bullet.sety(-2000)
            anti_Bullet.setx(20000000)
            anti_Bullet.hideturtle()
            anti_B_speed = 0
            anti_state = "ready"
            pen.clear()
            score += 5
            pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    for anti_Bullet in anti_Bullets:
        if bomb.distance(anti_Bullet) < 20:
            anti_Bullet.sety(-2000)
            anti_Bullet.setx(20000000)
            anti_Bullet.hideturtle()
            anti_B_speed = 0
            anti_state = "ready"
            pen.clear()
            score += 5
            pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    if anti_C.xcor() < -380:
        anti_C.setx(random.randint(400, 500))

    for anti_Bullet in anti_Bullets:
        if anti_Bullet.distance(player) < 37:
            anti_Bullet.sety(-2000)
            anti_Bullet.setx(20000000)
            anti_Bullet.hideturtle()
            anti_B_speed = 0
            anti_state = "ready"
            pen.clear()
            score -= 10
            lives -= 1
            pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    if missile.distance(anti_C) < 37:
        missile.setx(-2000)
        missile.sety(88888888888888)
        anti_C.setx(random.randint(330, 1000))
        missile.hideturtle()
        missile_state = "ready"
        pen.clear()
        score += 50
        A_fire_count = 0
        pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    if bomb.distance(anti_C) < 37:
        bomb.setx(-2000)
        missile.sety(88888888888888)
        anti_C.setx(random.randint(330, 1000))
        bomb.hideturtle()
        bomb_state = "ready"
        pen.clear()
        score += 50
        A_fire_count = 0
        pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)        
    
    if tank_Bullet.distance(player) < 37:
        tank_Bullet.hideturtle()
        tank_B_state = "ready"
        tank_Bullet.sety(20000)
        pen.clear()
        score -= 10
        lives -= 1
        pen.write("Score: {}      Lives {}".format(score, lives), align="center", font=font)

    if lives <= 0:
        player.hideturtle()
        pen.clear()
        pen.color("#F00000")
        pen.write("---GAME  ___  OVER---".format(score, lives), align="center", font=font)
        sys.exit()
        
    anim_loop1()
    anim_loop2()
    fire_Count()
    FC2()

wn.mainloop()
