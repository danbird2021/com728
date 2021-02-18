# A program that uses the turtle module in Python to draw a square

# Import turtle.
import turtle
bob = turtle.Turtle()

# Display turtle object (bob).
print(bob)

# Create square using turtle.
for sides in range(4):
    # Use turtle forward (fd) method to draw a line 100 pixels long.
    bob.fd(100)
    # Use the turtle left turn (lt) method to turn the turtle pen 90 degrees.
    bob.lt(90)


# Display Hello four times.
for i in range(4):
    print('Hello')



turtle.mainloop()
