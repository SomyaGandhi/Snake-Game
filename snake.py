import turtle
import time
import random

# Turtle module slows down as the size of snake increases.
# So, to make the challenge tougher, we decrease delay(so increasing speed)
# everytime snake eats food

delay = 0.1
segments = []

# Score
score = 0
high_score = 0

# Set up screen
wn = turtle.Screen()
wn.title("Snake Game by Somya")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # stops updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.color("black")
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0,100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("Score : 0 | High Score: 0",align="center", font=("Courier",24,"normal"))


# Functions

def go_up():
    if(head.direction!="down" or len(segments)==0): # so that when snake moving down, it cant move up | Done so that if we reverse then we will get out as head touches segment
        head.direction="up"

def go_down():
    if (head.direction != "up" or len(segments)==0):
        head.direction="down"

def go_left():
    if (head.direction != "right" or len(segments)==0):
        head.direction="left"

def go_right():
    if (head.direction != "left" or len(segments)==0):
        head.direction="right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Keyboard Bindings

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main Loop
while True:
    wn.update()

    # Check for collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide segments
        for segment in segments:
            segment.hideturtle()
            segment.clear()
        segments.clear()

        # Reset Delay
        delay = 0.1

        # Reset Score
        score = 0
        pen.clear()
        pen.write("Score : {} | High Score: {}".format(score, high_score) ,align="center", font=("Courier",24,"normal"))

    if head.distance(food) < 20: # inbuilt function to find distance b/w two turtle objects
        # Move food to random position
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Decrease Delay
        delay -=0.001

        # Increase Score
        score += 10
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score : {} | High Score: {}".format(score, high_score) ,align="center", font=("Courier",24,"normal"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()

    # Checking for collision of head with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide segments
            for segment in segments:
                segment.hideturtle()
                segment.clear()
            segments.clear()

            # Decrease Delay
            delay -=0.001

            # Reset Score
            score = 0
            pen.clear()
            pen.write("Score : {} | High Score: {}".format(score, high_score) ,align="center", font=("Courier",24,"normal"))


    time.sleep(delay)

wn.mainloop()
