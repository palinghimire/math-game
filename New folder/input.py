import random
from random import*
import operator
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
import random

# Initialize score and choose a random operator
# ... (your name and instruction code above) ...

# 1. Initialize the score outside the loop
u = 0 

# 2. Use a 'for' loop to repeat the questions
for i in range(question_amount):
    op = random.choice(['+', '-', '*'])
    a = random.randint(2, 9)
    b = random.randint(2, 9)

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    else:
        result = a * b

    # 3. Ask the question (indented so it's inside the loop)
    answer = float(input(f"Question {i+1}: What is {a} {op} {b}? "))

    if answer == result:
        u = u + 1
        print("Correct!")
    else:
        print(f"Wrong answer. The correct answer was {result}")

# 4. Print the final score after the loop finishes
print(f"Game Over! You got {u} out of {question_amount} right.")
# 1. Add this BEFORE your loop starts
history = []
score = 0

# 2. Inside your loop, after the user answers, add this:
if answer == result:
    score += 1
    feedback = "Correct"
else:
    feedback = f"Incorrect (Correct: {result})"

# This saves the result to your list
history.append(f"Q{i+1}: {a} {op} {b} = {answer} | {feedback}")

# 3. Paste this at the very END of your code (outside the loop)
print("\n--- GAME HISTORY ---")
for line in history:
    print(line)
print(f"\nFinal Score: {score}/{question_amount}")
