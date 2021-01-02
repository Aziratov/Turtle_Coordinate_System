from turtle import Turtle, Screen
import random

screen = Screen()
race_started = False


screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet",
                            prompt="Which turtle will win? Pick your color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for i in range(0, 6):

  new_turtle = Turtle(shape="turtle")
  new_turtle.color(colors[i])
  new_turtle.penup()
  new_turtle.goto(x=-230, y=y_pos[i])
  all_turtles.append(new_turtle)

if user_bet:
    race_started = True

while race_started:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      race_started = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You won! The {winning_color} turtle is the winner!")
      else: 
        print(f"You've lost! The {winning_color} turtle is the winner!")
    rand_dist = random.randint(0, 10)
    turtle.forward(rand_dist)

screen.exitonclick()
