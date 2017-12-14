# CTI-110
# M3LAB - Debugging (elif version)
# William Thomas
# 10 Oct 2017
# Program to take a number grade and output a letter grade.

def main():
    # Define letter grades.
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    # Get user input for score, and determine letter grade with if/else statements.    
    score = int (input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your grade is: D')
    elif score < D_score:
        print('Your grade is: F')

# program start
main()
