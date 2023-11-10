# Importing the turtle module for graphics
import turtle
# Importing the randint function from random module for generating random numbers
from random import randint

# Printing the authors' names
print("By:\nRalph Joshua Seromines and Hedjara Darapa. \n")

# Input the racer names
print('Please Enter Names')
name1 = input("Name for Racer 1: ")
name2 = input("Name for Racer 2: ")

# Input for betting on a racer
bet = input(f"Pick one player for your bet? \n      [{name1}] or [{name2}]\nJust type the name of your bet: ")

# Variables for customization (colors, dimensions, etc.)
# I'm using variable for changing section.
# here you can change the colors, coordinates, title and the shape easily, so that I can find and edit it easily.
screen_title = 'TURTLE DRAG RACE'
t1_border = 'SkyBlue'
t1_fill = 'Black'
t2_border = 'Pink'
t2_fill = 'Black'
BgColor = 'Black'
font = 'Lucida Sans Typewriter'

width = 650  # Width of the window
height = 180  # Height of the window
turtle_shape = 'turtle'  # Shape of the turtle graphics

# Setting up the turtle screen
display = turtle.Screen()   # Creating a turtle screen
display.setup(width, height)  # Setting the dimensions of the screen
display.bgcolor(BgColor)   # Setting the background color

# Finish Line Setup
# Creating a finish line using square shapes as stamps
fin_line = turtle.Turtle()
fin_line.speed(0)
fin_line.color('White')
fin_line.shape('square')
fin_line.penup()

# Creating the finish line stamps
distance = 250
y_position = 85

# Create the finish line using stamps
# I'm using loops to stamp the square to where i positioned it.
for i in range(5):
    fin_line.goto(distance, y_position - i * 40)
    fin_line.stamp()

for j in range(4):
    fin_line.goto(distance + 20, y_position - 20 - j * 40)
    fin_line.stamp()

# The Onscreen title
title = turtle.Turtle()
title.goto(0, 47)
title.pencolor('yellow')
title.write(screen_title, align='center', font=("Castellar", 15, "normal"))
title.hideturtle()

# Create two turtle objects
T1 = turtle.Turtle()
T2 = turtle.Turtle()

# Setup for displaying racer names
R1 = turtle.Turtle()
R1.hideturtle()
R1.penup()
R1.goto(-290, 10)
R1.color(t1_border, t1_fill)
R1.write(name1, font=(font, 15, "normal",))

# Racer 1's turtle object setup
T1.shape(turtle_shape)
T1.color(t1_border, t1_fill)
T1.penup()
T1.goto(-200, 20)
T1.penup()

# Racer 2 name Setup
R2 = turtle.Turtle()
R2.hideturtle()
R2.penup()
R2.goto(-290, -30)
R2.color(t2_border, t2_fill)
R2.write(name2, font=(font, 15, "normal"))

# Racer 2's turtle object setup
T2.shape(turtle_shape)
T2.color(t2_border, t2_fill)
T2.penup()
T2.goto(-200, -20)
T2.penup()

# Simulate the race by moving racers randomly
for i in range(250):
    T1.forward(randint(1, 5))
    T2.forward(randint(1, 5))

    if T1.xcor() >= distance or T2.xcor() >= distance:
        break

# Display winner and loser
# Determine the winner and display the result
# This section checks the positions of the racers and compares them to determine the winner
# It also checks the bet made by the user and displays the appropriate message
# Finally, it prints the winner's name in the console
if T1.xcor() >= distance and T2.xcor() >= distance:
    winner_message = "It's a tie!"
    color = 'White'

# Conditions for racer 1 winning
# Checks if the bet matches the winner and updates the winner message accordingly
elif T1.xcor() >= distance:

    if bet == name1:
        winner_message = f"Congratulations! You won against {name2}.\nYou've successfully won the bet.!"
        color = 'Green'
    elif bet == name2:
        winner_message = f"{name1} wins, and you lost your bet."
        color = 'Red'
    else:
        winner_message = "YOU BET WHO?!\nPlease Try Again."
        color = 'Red'

# Conditions for racer 2 winning
# Checks if the bet matches the winner and updates the winner message accordingly
elif T2.xcor() >= distance:
    if bet == name2:
        winner_message = f"Congratulations! You won against {name1}.\nYou've successfully won the bet."
        color = 'Green'
    elif bet == name1:
        winner_message = f"{name2} wins, and you lost your bet."
        color = 'Red'
    else:
        winner_message = "YOU BET WHO?!\nPlease Try Again."
        color = 'Red'
else:
    winner_message = "Please Try Again."
    color = 'White'

# Display the winner message on the screen
result = turtle.Turtle()
result.goto(0, -15)
result.color(color)
result.write(winner_message, align="center", font=(font, 13, "normal"))
result.hideturtle()

# Print the winner's name in the console
if bet == name1:
    print(f"\nThe winner is {name1}, Congratulations!")
else:
    print(f"\nThe winner is {name2}, Congratulations!")

print("\nRace and Bet again!\n  Enjoy the Game!!")


# Close the turtle graphics window when clicked
turtle.exitonclick()
turtle.done()
