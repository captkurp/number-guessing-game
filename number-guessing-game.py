import random

def main():
    welcome_message()
    repeat = True
    while repeat == True:
        win_con = 0
        number = generate_number()
        num_of_guesses = difficulty_select()
        while num_of_guesses >= 0 and win_con == 0:
            user_num = prompt_user()
            win_con = evaluate_guess(number, user_num, win_con)
            print(f"main wincon {win_con}")
            print_guesses(num_of_guesses)
            num_of_guesses -= 1
            if win_con == 1:
                print("          Great job you won with {num_of_guesses} guesses left!")
        repeat = play_again()

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
    while True:
        if difficulty == "1":
            return 9
        elif difficulty == "2":
            return 4
        elif difficulty == "3":
            return 2
        else:
            difficulty = input("          Invalid option, please select a difficulty: ")

def evaluate_guess(number, user_num, win_con):
    if user_num > number:
        print(f"          Too high, the number is less than {user_num}!")
        return win_con
    elif user_num < number:
        print(f"          Too low, the number is greater than {user_num}!")
        return win_con
    else:
        print("runnign")
        win_con = 1
        return win_con

def play_again():
    while True:
        choice = input("           Would you like to play again? Y or N :")
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("          Unrecognized input, please try again")

def print_guesses(num_of_guesses):
    print(f"          You have {num_of_guesses} guesses left!")

if __name__ == "__main__":
    main()
