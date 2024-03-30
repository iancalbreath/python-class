# Mac Littlefield's class
# Objective: write program containing 2 functions, main() and isprime(arg)
# IanCalbreath-Hwrk5A.py
# Ian Calbreath

# Defining my name
myname = "Ian Calbreath"

# isprime() is designed to:
#   test argument sent to it to see if it is a prime num
#   check that num is not divisible by any number less than the value of num


def isPrime(number):
        if int(number) == 2 or int(number) == 3: return True
        if number < 2 or number%2 ==0:
                return False
        if number%3 == 0: return False
        f = 3
        while f*f <= number:
                if number % k == 0:
                                return False
                k += 2
                return True
        


# main() is designed to:
#   print "My Name's Prime Number Checker"
#   prompt user input for an integer
#   check that the integer is equal to or greater than the integer 2. if not, re-prompt
#   call function isprime(num) which returns T or F (lines 27, 28, 29, 30, 31)
#   encased in while loop to test more integers (lines 18, 19, 33, 34, 35)

def main():
        test_another = 'y'
        while test_another == 'y':

                print(f"{myname}'s Prime Number Checker")
                userint = input("Enter an integer: ")
                while int(userint) < 2:
                        print("You can only use integers greater than or equal to 2.: ")
                        userint = input("Enter an integer: ")
                        isPrime(userint)
                if isPrime(userint) == True:
                        print(f"{userint} is Prime.")
                else:
                        print(f"{userint} is not Prime.")


                test_another = input('Do you want to check a different integer? (Enter y for yes, n to exit.): ')
                if test_another.lower() == "n":
                        break
main()


        
