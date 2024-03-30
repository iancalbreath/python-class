# This program gets a numeric score from the user and displays the corresponding letter grade

# Ian Calbreath's Grading Program with Input Validation and Repetition using while loops
print("Ian Calbreath's Grading Program with Input Validation and Repetition")
# Mac Littlefield's class

# Setting score variables
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# minmax score variables
MAX_SCORE = 100
MIN_SCORE = 0

# while loop 1 to test additional scores
test_another = 'y'
while test_another == 'y':
        # Setting input to declare score value 
        score = int(input('Enter your test score: '))

        # while loop 2
        while score > MAX_SCORE or score < MIN_SCORE:
                print("Sorry, that's not a valid number.")
                score = int(input('Please enter a valid test score (0-100): '))
    
        if score >= A_score:
                print('Your grade is A.')
        elif score >= B_score:
                print('Your grade is B.')
        elif score >= C_score:
                print('Your grade is C.')
        elif score >= D_score:
                print('Your grade is D.')
        else:
                print('Your grade is F.')

        test_another = (input('Do you want to test another score? (Enter y for yes, n to exit.): '))
        if test_another.lower() == "n":
                break
