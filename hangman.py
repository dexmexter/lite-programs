import getpass #TODO add for 2p version
import string

import game_functions as core

def strikes_art(n):
    strike0 = "   ___    \n\
  /   |   \n\
      |   \n\
      |   \n\
      |   \n\
      |   \n\
----------\n"

    strike1 = "   ___    \n\
  /   |   \n\
  o   |   \n\
      |   \n\
      |   \n\
      |   \n\
----------\n"

    strike2 = "   ___    \n\
  /   |   \n\
  o   |   \n\
  |   |   \n\
      |   \n\
      |   \n\
----------\n"

    strike3 = "   ___    \n\
  /   |   \n\
  o   |   \n\
 /|   |   \n\
      |   \n\
      |   \n\
----------\n"

    strike4 = "   ___    \n\
  /   |   \n\
  o   |   \n\
 /|\  |   \n\
      |   \n\
      |   \n\
----------\n"

    strike5 = "   ___    \n\
  /   |   \n\
  o   |   \n\
 /|\  |   \n\
 /    |   \n\
      |   \n\
----------\n"

    strike6 = "   ___    \n\
  /   |   \n\
  o   |   \n\
 /|\  |   \n\
 / \  |   \n\
      |   \n\
----------\n"

    drawings = [strike0, strike1, strike2, strike3, strike4, strike5, strike6]
    return drawings[n]

def main_game():
    guess_pool = list(string.ascii_lowercase)
    
    target = getpass.getpass("What is the target word?\n") # TODO add for 2p version
    #target = "cat" # TODO get random word from list of common hangman words
    target_list = list(target)
    letters_remaining = []

    for i in target:
        if i not in letters_remaining:
            letters_remaining.append(i)
    
    check_word = "*" * len(target) # TODO allow for target with multiple words
    check_list = list(check_word)
    
    core.print_slow("Welcome to Hangman, good luck guessing the word!\n")

    strikes = 0
    while strikes < 6:
        core.print_slow(strikes_art(strikes))
        core.print_slow("".join(check_list) + "\n")
        user_guess = input(core.print_slow("\nYour guess:")) # TODO won't print slow

        if user_guess not in guess_pool:
            core.print_slow("That guess is either not valid or has already been used, please guess again.\n")
        
        elif user_guess not in letters_remaining:
            strikes += 1
            core.print_slow("You have %s incorrect guesses remaining.\n" %(str(6 - strikes)))
        
        elif user_guess in letters_remaining:
            guess_pool.remove(user_guess)
            letters_remaining.remove(user_guess)
        
            store_index = [i for i, x in enumerate(target_list) if x == user_guess]
            for i in store_index:
                check_list[i] = user_guess

        if len(letters_remaining) == 0:
            core.print_slow("".join(check_list) + "\n")
            return core.print_slow("You've won!\n")

    core.print_slow(strikes_art(strikes))
    return core.print_slow("Sorry you ran out of tries! The word you were trying to guess was: \n%s\n" %(target))
    
def main():
    main_game()
    core.play_again(main_game)

if __name__ == "__main__":
    main()