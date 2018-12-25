import time
import sys

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

def play_again():
    again = input(print_slow("Would you like to play again? y/n:"))

    if again == "y":
        main_game()
    elif again == "n":
        print_slow("Alright, maybe another time!\n")
        return
    else:
        print_slow("Sorry, didn't quite catch that...\n")
        play_again()