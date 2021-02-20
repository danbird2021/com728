def run():
    # a program to count up the number of even and odd numbers

    print("Please enter the first number:")
    first_number = int(input())

    print("Please enter the second number:")
    second_number = int(input())

    print("Please enter the third number:")
    third_number = int(input())

    odd_count = int(0)
    even_count = int(0)

    # if statements using modulo operator to determine if each number is odd or even and adding a 1 to the relevent count
    if first_number % 2 != 0:
        odd_count = odd_count + 1
    else:
        even_count = even_count + 1

    if second_number % 2 != 0:
        odd_count = odd_count + 1
    else:
        even_count = even_count + 1

    if third_number % 2 != 0:
        odd_count = odd_count + 1
    else:
        even_count = even_count + 1

    # display the result of counting odd and even numbers
    print(f"There were {even_count} even numbers and {odd_count} odd numbers.")