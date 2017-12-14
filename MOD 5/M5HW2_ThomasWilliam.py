# CTI-110
# M5HW2 - Running Total
# William Thomas
# 10 October 2017
# Program to take numbers from user input and output a running total.

def runtot():
# Set running total to zero.
    runtot = 0
# Get user input for first number.
    newnum = float(input('Enter the first number: '))
# Set conditions for loop.
    while newnum > 0:
        runtot += newnum
# Get user input for next number.
        newnum = float(input('Enter the next number (or a negative number to end): '))
# Print the total of all added numbers after one empty line.
    print()
    print('The total of all the positive numbers entered is: ',runtot )
# Run Program
runtot()
