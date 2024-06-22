import gspread
import random
import datetime
from google.oauth2.service_account import Credentials
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Scores')

def sort_scores():
    worksheet = SHEET.worksheet('Sheet1')
    data = worksheet.get_all_values()
    
    scores_data = []
    for row in data[1:]:
        try:
            username = row[0]
            score = int(row[1])
            date = row[2]
            scores_data.append([username, score, date])
        except ValueError:
            print(Fore.RED + f"Skipping invalid score entry: {row}")
            continue
    
    sorted_scores = sorted(scores_data, key=lambda x: x[1])
    worksheet.clear()
    worksheet.append_row(data[0])
    for row in sorted_scores:
        worksheet.append_row(row)
    
    return sorted_scores

def fill_scoreboard(username, score, worksheet='Sheet1'):
    print(Fore.BLUE + "Updating scoreboard...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    worksheet_to_update.append_row([username, score, now])
    print(Fore.GREEN + "Scoreboard updated successfully\n")
    sort_scores()

def number_guessing_game():
    num = random.randint(1, 100)
    print(num)  # For debugging purposes; remove this line in production
    guesses = 0
    max_attempts = 5
    while guesses < max_attempts:
        answer = None
        while True:
            try:
                answer = int(input(Fore.YELLOW + "Guess a number between 1 and 100: "))
                break
            except ValueError:
                print(Fore.RED + "Please enter a valid integer.")
                continue
                
        guesses += 1
        if answer == num:
            print(Fore.GREEN + "You won!")
            print(Fore.YELLOW + f"Do you want to save your score? You guessed correctly in {guesses} out of {max_attempts} attempts.")
            save_score = input("(yes/no): ").lower()
            if save_score == "yes":
                username = input("Enter your name: ")
                fill_scoreboard(username, guesses)
                play_again()
            elif save_score == "no":
                print(Fore.RED + "Closing game, thanks for playing.")
                return
            else:
                print(Fore.RED + "Invalid option, restarting game...")
                welcome_message()
        elif answer < num:
            print(Fore.GREEN + f"Try Higher\nYou have used {guesses} out of {max_attempts} guesses.")
        elif answer > num:
            print(Fore.GREEN + f"Try Lower\nYou have used {guesses} out of {max_attempts} guesses.")
    
    print(Fore.RED + f"You have no guesses left. The correct number was {num}")
    play_again()

def play_again():
    while True:
        play_again_choice = input(Fore.YELLOW + "Do you want to try again? (yes/no): ").lower()
        if play_again_choice == "yes":
            number_guessing_game()
        elif play_again_choice == "no":
            print(Fore.RED + "Closing game...")
            return
        else:
            print(Fore.RED + "Invalid option, please try again.")

def welcome_message():
    print(Fore.CYAN + "Hello!\nThis is a game where the goal is to guess the correct number between 1 and 100.")
    print("You have 5 guesses, and if you win, you have the option to save your score.")
    while True:
        ready = input(Fore.YELLOW + "Do you want to play? (yes/no): ").lower()
        if ready == "yes":
            number_guessing_game()
        elif ready == "no":
            print(Fore.RED + "Closing game...")
            quit()
        else:
            print(Fore.RED + "Invalid option, please try again.")

def highscore():
    sorted_scores = sort_scores()
    print(Fore.CYAN + "Top 5 High Scores:")
    for i, score in enumerate(sorted_scores[:5], start=1):
        username, score_value, date = score
        print(f"{i}. {username}: {score_value} on {date}")

# Uncomment the line below to start the game with a welcome message
# welcome_message()

# To display high scores
highscore()

