import turtle 
import math 

# Setup the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.hideturtle()

# Function to draw the heart using lines
def draw_heart_lines():
    # Set up the start and end position to from the heart with lines
    for i in range(0, 200):
        angle = math.radians(i * 1.8)
        x = 160 * math.sin(angle)  ** 3
        y = 130 * math.cos(angle) - 50 * math.cos(2 * angle) - 20 * math.cos(3 * angle) - 10 * math.cos(4 * angle)

        # Move to the calculation point
        pen.penup()
        pen.goto(0, - 100)
        pen.pendown()
        pen.goto(x, y)

# Call the function to draw the heart with lines
draw_heart_lines()

#End the program when clicked
screen.exitonclick()