import time
import random
import sys
import game_functions as core

score = {"wins":0, "losses":0}

def main_game():
    triangle = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    user_choice = input(core.print_slow("Welcome to the game. Please choose either rock, paper or scissors:"))
    valid_choice = list(triangle.keys())

    while user_choice not in triangle.keys():
        user_choice = input(core.print_slow("Sorry, that isn't a valid choice, please choose rock, paper, or scissors: "))

    core.print_slow("You chose: " + user_choice + "\n")

    cpu_choice = random.choice(valid_choice)
    result_states = {"w":"You win!", "l":"Sorry, you lost this time...", "t":"Tie game!"}
    result = ""

    if triangle[user_choice] == cpu_choice:
        result = result_states["w"]
        score["wins"] += 1

    elif user_choice == cpu_choice:
        result = result_states["t"]
    
    elif triangle[cpu_choice] == user_choice:
        result = result_states["l"]
        score["losses"] += 1

    core.print_slow("Your opponent chose:\n")
    core.print_slow(". . .\n", 0.5)
    core.print_slow(cpu_choice + "\n")
    core.print_slow(result + "\n")
    core.print_slow("The score is: ")
    print(score)

# TODO: Import game_functions instead of defining locally
def main():
    main_game()
    core.play_again(main_game)

if __name__ == "__main__":
    main()