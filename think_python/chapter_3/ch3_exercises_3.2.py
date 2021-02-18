# A program to call functions within functions.

def do_twice(f,v):
    f(v)
    f(v)

def print_spam(v):
    print(v)

do_twice(print_spam,"spam")

def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)

do_four(print_spam,"Dan")