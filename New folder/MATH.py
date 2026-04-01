import random

# --- Functions ---
def yes_no(name):
    while True:
        response = input(f"{name}, do you need instructions? ").lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please answer with 'yes' or 'no'.")

def instructions():
    print("""
    *** instructions ***
    You will be given a set of math questions.
    Answer as many as you picked, and at the end
    you will be given your results.
    """)

# --- Main Routine ---
name = input("What is your name?: ")

# Instruction Check
if yes_no(name) == "yes":
    instructions()

question_amount = int(input(f"{name}, how many questions would you like?: "))

# 1. Initialize score and history BEFORE the loop
u = 0 
history = []

# 2. The Game Loop
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

    # 3. Handle empty/random inputs (The "Barking" fix)
    while True:
        user_input = input(f"Question {i+1}: What is {a} {op} {b}? ").strip()
        if user_input == "":
            print("Don't leave it blank!")
            continue
        try:
            answer = float(user_input)
            break 
        except ValueError:
            print("That's not a number! Try again.")

    # 4. Check Answer & Record History
    if answer == result:
        u += 1
        feedback = "Correct"
        print("Correct!")
    else:
        feedback = f"Incorrect (Ans: {result})"
        print(f"Wrong answer. The correct answer was {result}")

    # Add this specific question to the history list
    history.append(f"Q{i+1}: {a} {op} {b} = {answer} | {feedback}")

# 5. Print the final results and history at the very end
print(" GAME HISTORY ")
for line in history:
    print(line)

print(f"nFinal Score: {u} out of {question_amount} right.")
