import gspread
import random
import datetime
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Scores')

def fill_scoreboard(username, score, worksheet='Sheet1'):
    print(f"Updating scoreboard...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    worksheet_to_update.append_row([username, score, now])
    print("Scoreboard updated successfully\n")

def number_guessing_game():
    num = random.randint(1, 100)
    guesses = 0
    max_attempts = 7
    while guesses < max_attempts:
        print(num)
        answer = None
        while True:
            try:
                answer = int(input("Guess a number between 1 and 100\n"))
                break
            except ValueError:
                print("Please enter a valid integer.")
        
        guesses += 1
        if answer == num:
            print("You won!")
            print(f"Do you want to save your score? You guessed {guesses} out of {max_attempts} times correctly.")
            save_score = input("(yes/no): \n").lower()
            if save_score == "yes":
                username = input("Enter your name: ")
                fill_scoreboard(username, guesses)
                play_again()
            elif save_score == "no":
                print("Closing game, thanks for playing.")
                return
            else:
                print("Invalid option, restarting game...")
        elif answer < num:
            print("Try Higher\nYou have used", int(guesses), "out of {max_attempts} guesses.")
        elif answer > num:
            print("Try Lower\nYou have used", int(guesses), "out of {max_attempts} guesses.")
    print("You have no guesses left, the number was", num)
    play_again()

def play_again():
    play_again = input("Do you want to try again? (yes/no): ").lower()
    if play_again == "yes":
        number_guessing_game()
    elif play_again == "no":
        quit()
    else:
        print("Invalid option, game restarting...")
        play_again()

def welcome_message():
    print("Hello!\nThis is a game where the goal is to guess the correct number between 1 and 100.")
    print("You have 7 guesses and if you win you have the option to save your score ")
    print("Do you want to play?")
    ready = input("(yes/no): \n").lower()
    if ready == "yes":
        number_guessing_game()
    elif ready == "no":
        print("Closing game...")
        quit()
    else:
        print("Invalid option, restarting...")
        welcome_message()

welcome_message()
