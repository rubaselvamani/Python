'''
Plan of approach:
Dice rolling game will only end if the user inputs "No" to rolling the dice.

1.Hence, infinite loop should be created.
2.The loop should break if the user input is No.
3.Random number generation function should be used.
4.User inputs might not be case-sensitive. This should be handled inside the script
5.Dice value should be 1 through 6

Optional Enhancements:
• Modify the program so the user can specify how many dice they want to roll.
• Add a feature that keeps track of how many times the user has rolled the dice
during the session. This will require a counter that increments each time the
dice are rolled.
'''

import random

single_counter = 0
double_counter = 0

while True:
    dice_roll = input("Roll the dice (y/n): ").lower()
    if dice_roll == 'y':
        dice_roll_number = int(input("how many dice do you want to roll (1/2)? "))
        if dice_roll_number == 1:
            single_counter += 1
            print(random.randint(1, 6))
        elif dice_roll_number == 2:
            double_counter += 1
            print(random.randint(1,6),random.randint(1,6))
        else:
            print("Invalid Choice!")
    elif dice_roll == 'n':
        print("Thanks for playing!")
        if single_counter >0 or double_counter >0:
            print(f"you've rolled single dice {single_counter} times and double dice {double_counter} times")
        break
    else:
        print("Invalid Choice!")



