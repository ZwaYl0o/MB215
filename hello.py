#Activity 1
from datetime import date

Name = input("What is your name? ")
Age = int(input("How old are you? "))
Current_Year = date.today().year
Birth_year = date.today().year - Age
print(f"Greetings {Name} you were born in {Birth_year} years old.")

#Activity 2
Length = float(input("What is the length of rectangle?: "))
Width = float(input("What is the width of rectangle?: "))
Area = Length * Width
print(f"The area of the rectangle is {Area}.")

#Activity 3
print(f"Tell me about yourself in three parts")
string1 = input('tell me about yourself part 1:')
string2 = input('tell me about yourself part 2:')
string3 = input('tell me about yourself part 3:')
Full_Sentnence = string1 + string2 + string3
print(f"The full sentence is {Full_Sentnence}")

#Activity 4
import pandas as pd


def create_formatted_table():
    print("Welcome to the Data Table Formatter!")

    # Collect column titles
    print("Enter column titles for your table (max 20 characters each). Type 'done' when finished.")
    columns = []
    while True:
        column = input("Enter column title (or type 'done' to finish): ").strip()
        if column.lower() == "done":
            break
        if len(column) > 20:
            column = column[:20]  # Truncate to 20 characters
        columns.append(column)

    if not columns:
        print("No columns were provided. Exiting program.")
        return

    # Ask the user for the number of rows
    try:
        num_rows = int(input("How many rows of data would you like to enter? "))
    except ValueError:
        print("Invalid number of rows. Exiting program.")
        return

    rows = []
    for i in range(num_rows):
        print(f"\nEntering data for row {i + 1}:")
        row = []
        for column in columns:
            value = input(f"Enter value for '{column}' (max 20 characters): ").strip()
            if len(value) > 20:
                value = value[:20]  # Truncate to 20 characters
            row.append(value)
        rows.append(row)

    # Create a DataFrame and print the formatted table
    table = pd.DataFrame(rows, columns=columns)
    print("\nFormatted Table:")
    print(table)


# Run the function
create_formatted_table()

#Activity 5
PI = 3.14
Radius = float(input("Please enter the radius of the circle: "))
Area_of_Circle = PI * Radius ** 2
print(f"The area of the circle is {Area_of_Circle}")

#Activity 6
A = float(input("Please enter number A: "))
B = float(input("Please enter number B: "))
Addition = A + B
Subtraction = A - B
Multiplication = A * B
Division = A / B
integer_division = A // B
remainder = A % B
exponent = A ** B
print(f"The Addition is {Addition}.")
print(f"The Subtraction is {Subtraction}.")
print(f"The Multiplication is {Multiplication}.")
print(f"The Division is {Division}.")
print(f"the integer_division is {integer_division}.")
print(f"The remainder is {remainder}.")
print(f"The exponent is {exponent}.")

#Activity 7
import turtle
import tkinter.simpledialog as simpledialog

# Set up the window
window = turtle.Screen()
window.title("Turtle BOIIII")
window.bgcolor("Blue")

# Create a turtle
my_turtle = turtle.Turtle()

# Set pen size to 3
my_turtle.pensize(3)

# Set drawing color to blue
my_turtle.color("blue")

# Move the turtle forward by 100 units
my_turtle.forward(100)

# Turn the turtle right by 90 degrees
my_turtle.right(90)

# Move the turtle forward by 50 units
my_turtle.forward(50)

# Turn the turtle left by 90 degrees
my_turtle.left(90)

# Lift the pen up – no drawing when moving
my_turtle.penup()

# Move the turtle to a specific location
my_turtle.goto(-60, -20)

# Put the pen down – drawing when moving
my_turtle.pendown()

# Draw a circle with radius of 25
my_turtle.circle(25)

# Draw a dot with diameter 10
my_turtle.dot(10)

# Set the turtle heading to 0 (East)
my_turtle.setheading(0)

# Change the turtle color
my_turtle.color("Black")

# Draw a filled shape
my_turtle.begin_fill()
my_turtle.circle(50)
my_turtle.end_fill()

# Clear the drawing
my_turtle.clear()

# Reset the turtle's state
my_turtle.reset()

# Hide the turtle
my_turtle.hideturtle()

# Display the turtle
my_turtle.showturtle()

# Set the animation speed (0:fastest, 1:slowest, 10:normal)
my_turtle.speed(5)

# Display text
my_turtle.write("Hello, Turtle!", align="center", font=("Arial", 16, "bold"))

# Get input with a dialog box
user_input = simpledialog.askstring("Input", "Enter a message for the turtle:")

# Respond to user input
if user_input:
    my_turtle.clear()
    my_turtle.write(user_input, align="center", font=("Arial", 16, "bold"))

# Filling a shape with color
my_turtle.color("red")
my_turtle.begin_fill()
my_turtle.circle(40)
my_turtle.end_fill()

# Close the window on a click
window.exitonclick()

#Activity 8
Hours_Worked = float(input("How many hours worked? "))
Hourly_wage = float(input("Your hourly rate? "))
Gross_Pay = Hours_Worked * Hourly_wage
print(f'This is your Gross pay: {Gross_Pay}')



