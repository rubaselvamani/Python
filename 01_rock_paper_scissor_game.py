'''
Write a program to simulate a game of Rock, Paper, Scissors.

The game will prompt the player to choose rock, paper, or scissors by typing 'r',
'p', or 's'. The computer will randomly select its choice. The game will then display
both choices using emojis and determine the winner based on the rules.

--Rules--
1. Rock beats Scissors
✊ crushes ✌️
2 . Scissors beat Paper
✌️ cuts 📄
3. Paper beats Rock
📄 covers 🪨
'''

import random

# assign emojis
def assign_emoji(play_game,random_choice):
    #use a dictionary instead of an if clause
    emoji_dict = {'r':'🪨 Rock',
                  'p':'📄 paper',
                  's':'✂️ scissor'}
    return(emoji_dict.get(play_game),emoji_dict.get(random_choice))

# winning_rule
def winning_rule(play_game,random_choice):
    rule_dict = { 'r':{'r': 'It’s a draw!','s':'You won the game', 'p': 'You lost the game'},
                  'p': {'p': 'It’s a draw!', 's': 'You won the game', 'r': 'You lost the game'},
                  's': {'s': 'It’s a draw!', 'p': 'You won the game', 'r': 'You lost the game'}
                  }
    return(rule_dict[play_game][random_choice])

# play the game
def play_game():
   while True:
        play_game = input("Rock,paper or scissors? (r/p/s): ").lower()
        if play_game in ["r", "s", "p"]:
            random_choice = random.choice(["r", "s", "p"])
            play_game_e, random_choice_e = assign_emoji(play_game, random_choice)
            print (f"your choice: {play_game_e}")
            print(f"computer choice: {random_choice_e}")
            result = winning_rule(play_game,random_choice)
            print(f"Result: {result}")
            return
        else:
            print("Invalid choice.Choose among (r/p/s)")

# initiate 🪨 Rock 📄 paper ✂️ scissor game
def main():
    print("Welcome to 🪨 Rock 📄 paper ✂️ scissor game")

    while True:
        ready = input("Are you ready to play the game? (y/n): ").lower()
        if ready in ['y', 'n']:
            break
        print("Invalid Choice")

    while ready == 'y':
        play_game()
        while True:
            ready = input("Continue? (y/n):").lower()
            if ready in ['y', 'n']:
                break
            print("Invalid Choice")
    print("Exiting the game. Thank you!")


# Run the main program
if __name__ == "__main__":
    main()
