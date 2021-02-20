# Olly's Calculator
print("\nHello Olly :-), welcome to your own calculator!")
print("\nPlease enter your first number:")
sum1 = int(input())
print("Would you like to Add + , Minus -, Times * or Divide ÷ ?")
operator = input()
print("Please enter your second number:")
sum2 = int(input())



if operator == "+":
    answer = sum1 + sum2
elif operator == "-":
    answer = sum1 - sum2
elif operator == "*":
    answer = sum1 * sum2
elif operator == "/":
    answer = sum1 / sum2
else:
    print("Sorry, symbol not recognised!")

if answer == 11:
   print("Answer = Nutella!!!")
else:
   print("Answer = 11")
