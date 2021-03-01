# A program to display the information about the current working directory.

# Import os module
import os


def cwd():

"""
Retrieve the file path of the current working directory and place it into the variable 'path',
using the getcwd method of module os. Display path back to user.
Using a for loop and listdir method of module os, retrieve and display to user the
content of the current working directory.
"""
 path = os.getcwd()
 print(f"The current working directory: {path}")
 print("The directory contains the following files:")
 for file in os.listdir(path):
  print(file)

def run():
 """
 Display to user processing message and call cwd function.
 :return:
 """
 print("Processing...")
 cwd()

# Call run function.
run()