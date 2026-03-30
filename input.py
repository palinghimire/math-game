import random
from random import*
#funchtions

name = input("what is your name?:")
while True:

    question_amount = int(input(f"{name} how many questions whould you like?:"))

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
    break

def random_problem():
    operators:{
        '+' : operators.add,
        '-' : operators.sub,
        '*' : operators.multi,
        '/' : operators.div,
    }


        #veriable

u = 0
for i in range (question_amount):

        num1 = randint(2,9)
        num2 = randint(2,9)
        awnserforplus = num1 + num2
        awnser = int(input(f"what is {num1} + {num2}?: " ))
        if awnser == awnserforplus:
            u = u+1
        else :
            print("wrong awnser")
print (f"you got {u} awnser right")