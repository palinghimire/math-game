import random


            ### this is where i get the users name so i can make the message more personalised ###
while True:
                name = input("whats your name:")
                if name == "":
                    print("please enter a valid name")
                else:
                    break


                if name == "" or name == " ":
                    print ("please enter a name")
                    continue

while True:

                        help =input(f"{name} do you need help: ").lower()

                        #yes or nah
                        if help == "yes" or help == "y":
                            print("""
                        *** instructions ***
                            
                        you will be given a set of math questions
                        and you are to awnser how ever many you picked
                        and at the end you will be given you results
                            """)
                            break
                        elif help == "no" or help == "n":
                            print("you dont need help")
                            break
                        else:
                            print("yes or no?") 
                            continue
while True:
                    eqation = input("pick one + - * /")
                    if eqation == "+":
                        continue

                    else: break
                    
                                        
                            # random question genarator import random

                        # intialise rounds points
                    first_number = 0
                    second_number = 0

                        # Roll the dice for the user and note if they got a duble
                    random_number1 = random.randint(1, 6)
                    random_number2 = random.randint(1, 6)

                        #update the user and computer points
                    first_number += random_number1 + random_number2
                    awnser = first_number

                        #output the results
                        # let the user know what they rolled and if they got a double
                    print("\nInitial points")

                    usersawnser = input (f"{random_number1} + {random_number2} : ")
                    

                    if eqation == "/":
                        continue
                                        
                            # random question genarator import random

                        # intialise rounds points
                    first_number = 0
                    second_number = 0

                        # Roll the dice for the user and note if they got a duble
                    random_number1 = random.randint(1, 6)
                    random_number2 = random.randint(1, 6)

                        #update the user and computer points
                    first_number += random_number1 / random_number2
                    awnser = first_number

                        #output the results
                        # let the user know what they rolled and if they got a double
                    print("\nInitial points")

                    usersawnser = input (f"{random_number1} / {random_number2} : ")
                    if eqation == "-":
                        continue
                                        
                            # random question genarator import random

                        # intialise rounds points
                    first_number = 0
                    second_number = 0

                        # Roll the dice for the user and note if they got a duble
                    random_number1 = random.randint(1, 6)
                    random_number2 = random.randint(1, 6)

                        #update the user and computer points
                    first_number += random_number1 - random_number2
                    awnser = first_number

                        #output the results
                        # let the user know what they rolled and if they got a double
                    print("\nInitial points")

                    usersawnser = input (f"{random_number1} - {random_number2} : ")
                    if eqation == "*":
                        continue
                                        
                            # random question genarator import random

                        # intialise rounds points
                    first_number = 0
                    second_number = 0

                        # Roll the dice for the user and note if they got a duble
                    random_number1 = random.randint(1, 6)
                    random_number2 = random.randint(1, 6)

                        #update the user and computer points
                    first_number += random_number1 * random_number2
                    awnser = first_number

                        #output the results
                        # let the user know what they rolled and if they got a double
                    print("\nInitial points")

                    usersawnser = input (f"{random_number1} * {random_number2} : ")