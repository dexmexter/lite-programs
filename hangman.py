import getpass #TODO add for 2p version
import string

import game_functions as core

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
    
    core.print_slow("Welcome to Hangman, good luck guessing the word!\nHere is the word you need to solve:\n")
    core.print_slow("".join(check_list) + "\n")

    lives = 6
    while lives > 0:
        user_guess = input(core.print_slow("Your guess:")) # TODO won't print slow

        if user_guess not in guess_pool:
            core.print_slow("That guess is either not valid or has already been used, please guess again.\n")
        
        elif user_guess not in letters_remaining:
            core.print_slow("That letter isn't in the word... Please guess again.\n")
            
            lives -= 1
            core.print_slow("You have %s guesses remaining.\n" %(str(lives)))
        
        elif user_guess in letters_remaining:
            guess_pool.remove(user_guess)
            letters_remaining.remove(user_guess)
        
            store_index = [i for i, x in enumerate(target_list) if x == user_guess]
            for i in store_index:
                check_list[i] = user_guess
        
        core.print_slow("".join(check_list) + "\n")

        if len(letters_remaining) == 0:
            return core.print_slow("You've won!\n")

    return core.print_slow("Sorry you ran out of tries! The word you were trying to guess was: \n%s\n" %(target))
    
def main():
    main_game()
    core.play_again(main_game)

if __name__ == "__main__":
    main()