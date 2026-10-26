'''
Number Guessing Game:

Write a program to have the computer randomly select a number between 1 and
100, and then prompt the player to guess the number. The program should give
hints if the guess is too high or too low.

Optional Enhancements:

• Allow the user to specify the minimum and maximum values for the number
range before the game starts. This gives the player more control over the
difficulty level.
• Implement a feature that limits the number of guesses a player can make. If
the player runs out of attempts, the game should end, and the correct number
should be revealed.
• Add a feature that keeps track of the fewest attempts it took to guess the
number correctly. The program should display this "best score" at the end of
each game.

Note: Question reference - codewithmosh

'''

import random

#initialize the numbers
def init_random_number():
    while True:
        try:
            min_val = int(input("Select the minimum number:"))
            max_val = int(input("Select the maximum number:"))
            if min_val >max_val:
                print("select min value less than max value")
            else:
                random_number = random.randint(min_val, max_val)
                print(f"random number: {random_number}")
                return min_val,max_val,random_number
        except ValueError:
            print(" Invalid input")

#success notification
def success_notify (counter,best_score_list):
    best_score_list.append(counter)
    if counter == 1:
        print("Congratulations! You guessed it correctly in the first attempt itself!")
    else:
        print(f"Congratulations! You guessed it correctly in {counter} attempts. The best score is {min(best_score_list)} attempt(s)!")

#handle the guessed number
def guess_number_handle(min_val,max_val):
    while True:
        try:
            guess = int(input(f"Guess the number between {min_val} and {max_val}: "))
            if max_val >= guess >=min_val:
                return guess
            else:
                print(f"Guess the number between {min_val} and {max_val} range")
                continue

        except ValueError:
            print("Invalid input!")

#play the game guessing the number
def play_game(best_score_list,max_attempts =5):
    counter = 0
    min_val,max_val,random_number = init_random_number()

    while counter < max_attempts:
    #call initialize, min, max, and random function
        guess = guess_number_handle(min_val,max_val)
        counter += 1
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        elif guess == random_number:
            success_notify(counter, best_score_list)
            return

    print(f"You reached {max_attempts} attempts")

# main program
def main():
    print("Welcome to Number Guessing Game")
    ready = input("Are you ready to play Number Guessing Game? (y/n): ").lower()
    best_score_list =[]
    while True:

        if ready == 'n':
            #print("Exiting the game. Thank you for playing")
            break
        elif ready == 'y':
            print("Start the game")
            play_game(best_score_list)
            ready = input("Do you want to play another Number Guessing Game? (y/n): ")
            if ready =='n':
                break
        else:
            print("Invalid choice! PLease enter 'y' or 'n'.")
            ready = input("Are you ready to play Number Guessing Game? (y/n): ").lower()


    print("Exiting the game. Thank you for playing")

# Run the game
if __name__ == "__main__":
    main()
