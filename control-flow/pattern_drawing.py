# pattern_drawing.py
# A program to draw a square pattern of asterisks using nested loops

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # For loop to print asterisks in one row
    for col in range(size):
        print("*", end="")
    # After finishing one row, print a newline
    print()
    # Move to the next row
    row += 1
