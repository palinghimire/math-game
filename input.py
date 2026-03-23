import random
#funchtions


name = input("what is your name?:")
maxnumber = input(f"{name}how high of a number can you multiply/add/divied/minus?: ")
question_amount = input(f"{name} how many questions whould you like?:")

def yes_no(question):

    """checks if it outputs yes or no"""

    while True:


        response = input(f"{name} do you need instructions: ").lower()

        #yes or nah
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return("no")
        else:
            print("yes or no?") 


def instructions():
    """prints instructions"""

    print("""
*** instructions ***
      
you will be given a set of math questions
and you are to awnser how ever many you picked
and at the end you will be given you results
    """)

#main routine

#ask user if they need help(check if it says yes)
help = yes_no("do you want help? ")

#display the if the user want to see instructions
if help == "yes":
    instructions()

print()
print("program continues")

roll_one = random.randint(1, 6)
roll_two = random.randint(1, 6)



total_points = roll_one + roll_two
print(" roll 1: {roll_one} and roll 2: {roll_two} for a total of {total_points}")