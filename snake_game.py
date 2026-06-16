import turtle
import time
import random

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("red")
wn.setup(width=600, height=600)
wn.tracer(0)

# Score
score = 0

try:
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())

except:
    high_score = 0

    with open("high_score.txt", "w") as file:
        file.write("0")
game_started = False
paused = False
game_over = False
difficulty = 0.10
difficulty_name = "Medium"

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    f"Score: {score}  High Score: {high_score}",
    align="center",
    font=("Arial", 16, "bold")
)
start_pen = turtle.Turtle()
start_pen.speed(0)
start_pen.color("white")
start_pen.penup()
start_pen.hideturtle()

start_pen.goto(0, -50)

pause_pen = turtle.Turtle()
pause_pen.speed(0)
pause_pen.color("yellow")
pause_pen.penup()
pause_pen.hideturtle()

game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.color("white")
game_over_pen.penup()
game_over_pen.hideturtle()

def show_game_over():
    global game_over

    if game_over:
        return

    game_over = True

    game_over_pen.clear()
    game_over_pen.goto(0, 0)

    game_over_pen.write(
        f"GAME OVER\n\nScore: {score}\n\nPress SPACE to Restart",
        align="center",
        font=("Arial", 20, "bold")
        
    )
    print("GAME OVER TRIGGERED")
   

def restart_game():
    global score, game_over,game_started

    if not game_over:
        return

    game_over = False

    game_over_pen.clear()

    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)

    segments.clear()

    score = 0
    food.goto(0, 100)

    pen.clear()
    pen.write(
        f"Score: {score}  High Score: {high_score}",
        align="center",
        font=("Arial", 16, "bold")
    )
    game_started = True

def update_start_screen():
    start_pen.clear()

    start_pen.goto(0, -50)

    start_pen.write(
        f"SNAKE GAME\n\n"
        f"1 - Easy\n"
        f"2 - Medium\n"
        f"3 - Hard\n\n"
        f"Current: {difficulty_name}\n\n"
        f"Press SPACE to Start",
        align="center",
        font=("Arial", 20, "bold")
    )

update_start_screen()


# Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)

segments = []


def start_game():
    global game_started

    game_started = True
    start_pen.clear()
def pause_game():
    global paused

    if paused:
        return

    paused = True

    pause_pen.goto(0, 0)

    pause_pen.write(
        "PAUSED\n\nPress R to Resume",
        align="center",
        font=("Arial", 20, "bold")
    )
def resume_game():
    global paused

    if not paused:
        return

    pause_pen.clear()
    paused = False

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 10)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 10)       # 
def easy():
    global difficulty, difficulty_name

    if game_started:
        return

    difficulty = 0.15
    difficulty_name = "Easy"

    update_start_screen()


def medium():
    global difficulty, difficulty_name

    if game_started:
        return

    difficulty = 0.10
    difficulty_name = "Medium"

    update_start_screen()  
def hard():
    global difficulty, difficulty_name

    if game_started:
        return

    difficulty = 0.05
    difficulty_name = "Hard"

    update_start_screen()


def space_handler():
    if game_over:
        restart_game()
    else:
        start_game()


# Keyboard controls
wn.listen()
wn.onkeypress(go_up, "8")
wn.onkeypress(go_down, "2")
wn.onkeypress(go_left, "4")
wn.onkeypress(go_right, "6")
wn.onkeypress(space_handler, "space")
wn.onkeypress(pause_game, "p")
wn.onkeypress(resume_game, "r")
wn.onkeypress(easy, "e")
wn.onkeypress(medium, "m")
wn.onkeypress(hard, "h")
# Main game loop
while True:
    wn.update()
    if not game_started:
        time.sleep(0.1)
        continue

    if paused:
        time.sleep(0.1)
        continue
    if game_over:
       time.sleep(0.1)
       continue

    # Border collision
    if (head.xcor() > 290 or head.xcor() < -290 or
    head.ycor() > 290 or head.ycor() < -290):

     show_game_over()
    

    

    # Food collision
    if head.distance(food) < 20:

        x = random.randint(-28, 28) * 10
        y = random.randint(-28, 28) * 10
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()

        segments.append(new_segment)

        score += 10

        if score > high_score:
         high_score = score

         with open("high_score.txt", "w") as file:
          file.write(str(high_score))

        pen.clear()
        pen.write(
            f"Score: {score}  High Score: {high_score}",
            align="center",
            font=("Arial", 16, "bold")
        )

    # Move body
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Body collision
    for segment in segments:
        if segment.distance(head) < 10:

           show_game_over()

    time.sleep(difficulty)

wn.mainloop()