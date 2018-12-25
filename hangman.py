import string

import game_functions as core

def main_game():
    lives = 7
    guess_pool = list(string.ascii_lowercase)
    word = list("montypython") # TODO get random English word from list of common hangman words
    display_word = 

    while lives < 0:
        for i in display_word:



        for i in display_word:
            core.print_slow("")

        user_guess = core.print_slow(input("Your guess:"))

        if user_guess in word:
            pass
        
        elif user_guess not in word:
            core.print_slow("Sorry, that letter isn't in the word... \
            Please guess again.")
            
            lives -= 1
        

    
    core.print_slow("Sorry you ran out of tries! The word you were \
    trying to guess was: \n%s" %(word))
    
    core.play_again()
    
    
    if again == "y":
        print("Cool, let's go again then!")
    elif again == "n":
        print("That's alright, another time perhaps.")
    else:
        print("")



    """ 
    Welcome to the game
    
    Display word with hidden letters _ _ _ _
    
    Ask for guess letter
    
    Check if valid or already used and reask if not

    Check if guess matches letter in word

    If True, display word with proper "_" revealed

    If False, show how many tries they have left and ask for new letter

    Check if word is complete, if so, display win, if not, ask for another letter

    If tries = 0 display loss, reveal full word, ask if they want to play again
"""

# TODO: def __main__():