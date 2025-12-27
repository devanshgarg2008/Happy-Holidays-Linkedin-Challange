import turtle
import random
import os

# To SCREEN SETUP
screen = turtle.Screen()
# screen.setup(1000, 1000)
screen.title("Christmas Snow Scene")

# To add the background image (safe path)
screen.bgpic(os.path.join(os.path.dirname(__file__), "trees.png"))

turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0)

#USING THE FUNCTIONS
def position(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def star(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def light(size, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

#TO ADD THE DECORATION
# AND THE Star on tree ALSO
position(-50, 230)
star(50, "yellow")

# Tree lights
colors = ["red", "blue", "yellow", "cyan", "pink"]
for _ in range(20):
    x = random.randint(-220, 220)
    y = random.randint(-50, 250)
    position(x, y)
    light(8, random.choice(colors))

#TO ADD THE SNOWFALL ----------------
snowflakes = []

for _ in range(50):
    snow = turtle.Turtle()
    snow.hideturtle()
    snow.shape("circle")
    snow.color("white")
    snow.penup()
    snow.goto(random.randint(-500, 500), random.randint(0, 500))
    snow.speed(0)
    snowflakes.append(snow)

#ANIMATION LOOP
while True:
    for snow in snowflakes:
        snow.sety(snow.ycor() - random.uniform(0.5, 2))
        if snow.ycor() < -500:
            snow.goto(random.randint(-500, 500), 500)

    turtle.update()
