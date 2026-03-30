#import
from random import randint

#veriable
while True:
    num1 = randint (2,9)
    num2 = randint (2,9)
    awnserforplus = num1 + num2
    response = input(f"what is {num1} + {num2}?: " )
    if not response:
        break
    try:
        ans = int(response)
        print("great" if ans == awnserforplus else "wrong")
    except ValueError:
        print (f"{awnserforplus}")

        
    #ask if they want + - * / 

    #how many games


    #