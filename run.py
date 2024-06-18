import gspread
import random
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]



def scoreboard():
    
    pass

def number_guessing_game():
    num = random.randint(1, 100)
    guesses = 0
    while guesses < 7:
        answer = int(input("Guess a number between 1 and 100\n"))
        guesses += 1
        if answer == num:
            print("You won!")
            print(f"Do you want to save your score? You guessed {guesses} out of 7 times correctly.")
            save_score = str(input("\nEnter your score (yes/no): ").lower())
            if save_score == "yes":
                scoreboard()
            elif save_score == "no":
                print("Press run to play again.")
                return  # Exit the function to restart the game
            break
        elif answer < num:
            print("Try Higher\nYou have used", int(guesses), "out of 7 guesses.")
        elif answer > num:
            print("Try Lower\nYou have used", int(guesses), "out of 7 guesses.")
    else:
        print("You have no guesses left, the number was", num)
        play_again = input("Do you want to try again? (yes/no): ").lower()
        if play_again == "yes":
            number_guessing_game()

number_guessing_game()
