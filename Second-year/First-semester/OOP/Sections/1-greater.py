"""
Object Oriented Programming (OOP) >> (CS213).

Description: Ask usre for 2 numbers "num1", "num2" and compare them, if num2
is greater than num2 display the appropriate message other wise display another
one





"""

# Get the user input and split in spaces >> split(" ")
userinput = input("Enter Two number separated by spaces: ").split(" ")

# User formatted string (f" ") to print the output to the user
print(f"{max(userinput)} is greater that {min(userinput)}.")
