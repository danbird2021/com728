# A program to display a grid 3 x 2 using functions within functions.

def print_horizontal():
    print("+ - - - - + - - - - +")

def print_vertical():
    print("|         |         |\n" * 3, end="")
    print("|         |         |")

def print_twice():
    print_horizontal()
    print_vertical()

print_twice()
print_twice()
print_horizontal()