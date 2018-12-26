import time
import sys


def print_slow(str, value = None):
    if value == None:
        wait_time = 0.03
    else:
        wait_time = value
    
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(wait_time)
    
    return "\n"

def play_again(game_function):
    again = input(print_slow("Would you like to play again? y/n:"))

    if again == "y":
        game_function() # TODO This won't call unless main_game() defined.
        #return True 
    elif again == "n":
        print_slow("Alright, maybe another time!\n")
        return #False
    else:
        print_slow("Sorry, didn't quite catch that...\n")
        play_again()

def main():
    pass

if __name__ == "__main__":
    main()