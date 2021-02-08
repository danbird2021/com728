#Review of everything learned in week 1

# user enters their name
print("Hello human what is your name?")
# place users name entered into variable 'name'
name = input()

# set 'spaces' variable count to 1 space
spaces = ' '
# set character space count to 1 space
char_space = ' '

# display Ascii robot saying hello to user and ask how many spaces to move right
print(f"""
{spaces}       ###
{spaces}   ##########     ______________________________________________
{spaces}   #  +   + #   _| Hello {name}!{char_space * (37 - len(name))} |
{spaces}   #    #   #  / | how many spaces to the right should I move?  |
{spaces}   #  \__/  #_/   ----------------------------------------------
{spaces}   ##########
{spaces}      +++     
{spaces}       #    
{spaces}###############
{spaces}       #
{spaces}       #
{spaces}       #
{spaces}       #
{spaces}       #
{spaces}      # #
{spaces}     #   #
{spaces}    #     #
{spaces}   #       #
 """)
# ask user for number of spaces to be inputted
print("Number of spaces (max 80):")
# store users answer in variable 'spaces' and convert variable from a string to an integer
spaces = int(input())

# if user enters more than 80 for spaces to the right then spaces equals 80 to keep ascii robot on visible screen
if spaces > 80:
    spaces = 80

# display ascii robot moved to the right by the number spaces entered by user and ask them for a new character for the tie pattern
print(f"""\n
{spaces * ' '}       ###
{spaces * ' '}   ##########     ___________________________________________________________________
{spaces * ' '}   #  +   + #   _| I moved {spaces} spaces to the right.                                  |
{spaces * ' '}   #    #   #  / | Please choose a new character for my bow tie pattern:            |
{spaces * ' '}   #  \__/  #_/   -------------------------------------------------------------------
{spaces * ' '}   ##########
{spaces * ' '}      +++     
{spaces * ' '}       #    
{spaces * ' '}###############
{spaces * ' '}       #
{spaces * ' '}       #
{spaces * ' '}       #
{spaces * ' '}       #
{spaces * ' '}       #
{spaces * ' '}      # #
{spaces * ' '}     #   #
{spaces * ' '}    #     #
{spaces * ' '}   #       #
 """)

# ask user for bow tie character
print("Bow tie character (max 1):")
# store user's answer in bow_tie_char variable
bow_tie_char = input()


# display ascii robot with new bow tie character being used for bow tie
print(f"""\n
{spaces * ' '}       ###
{spaces * ' '}   ##########     _______________________________
{spaces * ' '}   #  +   + #   _| Very stylish {name}!{char_space * (15 - len(name))}|
{spaces * ' '}   #    #   #  / |                              |
{spaces * ' '}   #  \__/  #_/   -------------------------------
{spaces * ' '}   ##########
{spaces * ' '}      {bow_tie_char[0] * 3}     
{spaces * ' '}       #    
{spaces * ' '}###############
{spaces * ' '}       #
{spaces * ' '}       #
{spaces * ' '}       #
{spaces * ' '}       #
{spaces * ' '}       #
{spaces * ' '}      # #
{spaces * ' '}     #   #
{spaces * ' '}    #     #
{spaces * ' '}   #       #
 """)

