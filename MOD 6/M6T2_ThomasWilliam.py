# CTI-110
# M6T2: Feet to Inches
# William Thomas
# 7 December 2017
# Program to convert feet to inches.


# Set number of inches per foot.
INCHES_PER_FOOT = 12

# set main function.
def main():
    # Get user input for number of feet.
    feet = int(input('Enter a number of feet: '))

    # Convert feet to inches.
    print(feet, 'feet equals', feet_to_inches(feet), 'inches.')

# Convert feet to inches using feet_to_inches function.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Call main function.
main()

