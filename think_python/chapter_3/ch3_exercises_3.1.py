# A program using a function and the len function to retrieve a string and
# display the last character of this string on character 70.


def right_justify(s):
    print (' ' * (70 - (len(s))),s)

# Run Function right_justify with variable Dan
right_justify('Dan')