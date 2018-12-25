import time
import random
import sys

score = {"wins":0, "losses":0}

def rps_game(score):
    triangle = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    user_choice = input(print_slow("Welcome to the game. Please choose either rock, paper or scissors:"))
    valid_choice = list(triangle.keys())

    while user_choice not in triangle.keys():
        user_choice = input(print_slow("Sorry, that isn't a valid choice, please choose rock, paper, or scissors: "))

    print_slow("You chose: " + user_choice + "\n")

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

    print_slow("Your opponent chose:\n")
    print_slow(". . .\n", 0.5)
    print_slow(cpu_choice + "\n")
    print_slow(result + "\n")
    
    play_again(score)

def play_again(score):
    print_slow("The current score is: Wins(%d) Losses(%d)\n" %(score["wins"], score["losses"]))
    again = input(print_slow("Would you like to play again? y/n:"))

    if again == "y":
        rps_game(score)
    elif again == "n":
        print_slow("Alright, maybe another time!\n")
        return
    else:
        print_slow("Sorry, didn't quite catch that...\n")
        play_again()

def print_slow(str, value = None):
    if value == None:
        wait_time = 0.05
    else:
        wait_time = value
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(wait_time)
    return "\n"

rps_game(score)

# TODO: Import game_functions instead of defining locally