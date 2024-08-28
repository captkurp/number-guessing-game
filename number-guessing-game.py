import random
#import random to generate a number


#main function includes the welcome message and the main logic loop, the variable "win_con" detects if the player has guessed the number
def main():
    welcome_message()
    repeat = True
    while repeat == True:
        win_con = 0
        number = generate_number()
        guesses_remaining = difficulty_select()
        #this while loop allows the user to continue guessing until they either run out of guesses or satisfy the win condition
        while guesses_remaining >= 0 and win_con == 0:
            user_num = prompt_user()
            win_con = evaluate_guess(number, user_num, win_con)
            if win_con == 1:
                #this logic is only run once the win_con is met, the continue at the end of the run kicks the loop back up to evaluate line 14, and finds that line 14 is no longer true, thus moving to line 23 to prompt for a repeat
                print(f"          Great job you won with {guesses_remaining} guesses left!")
                continue
            print_guesses(guesses_remaining)
            guesses_remaining -= 1
        repeat = play_again()

#generate the number between 1 and 100
def generate_number():
    return random.randint(1, 100)

def welcome_message():
    print("""
          Welcome to the number guessing game! \n
          I am thinking of a number between 1 and 100 \n
          Please choose a difficulty level:
        """)

def prompt_user():
    user_num = input("          Enter your guess: ")
    return int(user_num)

def difficulty_select():
    print("          1. Easy (10 guesses)")
    print("          2. Medium (5 guesses)")
    print("          3. Hard (3 guesses)\n")
    difficulty = input("          Please select a difficulty: ")
    #loop to determine difficulty chosen, since the loop in main is >= 0, the return is the number of guesses the user gets after their initial guess, to allow a user to guess even with 0 guesses remaining, variable was renamed to guesses_remaining for clarity
    while True:
        if difficulty == "1":
            return 9
        elif difficulty == "2":
            return 4
        elif difficulty == "3":
            return 2
        else:
            difficulty = input("          Invalid option, please select a difficulty: ")

#evaluate function to check if the users number was too high or too low, returns the win win con
def evaluate_guess(number, user_num, win_con):
    if user_num > number:
        print(f"          Too high, the number is less than {user_num}!\n")
        return win_con
    elif user_num < number:
        print(f"          Too low, the number is greater than {user_num}!\n")
        return win_con
    else:
        win_con = 1
        return win_con

def play_again():
    while True:
        choice = input("          Would you like to play again? Y or N :")
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("          Unrecognized input, please try again")

def print_guesses(guesses_remaining):
    print(f"          You have {guesses_remaining} guesses left!\n")

if __name__ == "__main__":
    main()
