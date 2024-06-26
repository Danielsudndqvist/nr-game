import gspread  # Google Sheets API client library
import random   # Random number generation
import datetime  # Date and time operations
from google.oauth2.service_account import Credentials  # For Google APIs
from colorama import Fore, Style, init  # Color formatting for terminal output

# Initialize colorama for colored console output
init(autoreset=True)

# Define scopes for accessing Google Sheets and Drive APIs
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# Authenticate using service account credentials
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Scores')


def sort_scores():
    """
    Sorts the scores in ascending order and updates the Google Sheet with the
    sorted scores.
    """
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
    """
    Adds a new score entry to the specified worksheet and sorts the scores.
    """
    print(Fore.BLUE + "Updating scoreboard...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    worksheet_to_update.append_row([username, score, now])
    print(Fore.GREEN + "Scoreboard updated successfully\n")
    sort_scores()


def number_guessing_game():
    """
    Implements a number guessing game where the player has to guess a number
    between 1 and 100 within 5 attempts.
    """
    num = random.randint(1, 100)
    guesses = 0
    max_attempts = 5
    while guesses < max_attempts:
        answer = None
        while True:
            try:
                answer = int(input(Fore.YELLOW + f"Guess a number "
                             f"between 1 and 100: "))
                break
            except ValueError:
                print(Fore.RED + "Please enter a valid integer.")
                continue
        guesses += 1
        if answer == num:
            print(Fore.GREEN + "You won!")
            print(Fore.YELLOW + f"Do you want to save your score?"
                                f"You guessed correctly in "
                                f"{guesses} out of {max_attempts} attempts.")
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
            print(Fore.GREEN + f"Try Higher\nYou have used {guesses}"
                  f" out of {max_attempts} guesses.")
        elif answer > num:
            print(Fore.GREEN + f"Try Lower\nYou have used"
                  f" {guesses} out of {max_attempts} guesses.")
    print(Fore.RED + f"You have no guesses left. The correct number was {num}")
    play_again()


def play_again():
    """
    Asks the player if they want to play another round after finishing the
    current one.
    """
    while True:
        play_again_choice = input(Fore.YELLOW + "Do you want"
                                  f" to try again? (yes/no): ").lower()
        if play_again_choice == "yes":
            number_guessing_game()
        elif play_again_choice == "no":
            print(Fore.RED + "Closing game...")
            quit()
        else:
            print(Fore.RED + "Invalid option, please try again.")
            play_again()


def welcome_message():
    """
    Displays the main menu allowing the player to start a new game, view high
    scores, or quit the game.
    """
    print(Fore.CYAN + "Hello!\nThis is a game where the goal is "
          f"to guess the correct number between 1 and 100.")
    print("You have 5 guesses, and if you win, "
          f"you have the option to save your score.")
    print("Menu:")
    print("Start game press :1")
    print("Top 5 highscores press :2")
    print("Quit game press :3")
    while True:
        try:
            ready = int(input(Fore.YELLOW + "Enter your choice: "))
            if ready == 1:
                number_guessing_game()
            elif ready == 2:
                highscore()
                quit()
            elif ready == 3:
                print(Fore.RED + "Closing game...")
                quit()
            else:
                print(Fore.RED + "Invalid option, please try again.")
        except ValueError:
            print(Fore.RED + "Please enter a valid choice.")


def highscore():
    """
    Displays the top 5 high scores from the sorted scores list.
    """
    print("Loading highscores...")
    sorted_scores = sort_scores()
    print(Fore.CYAN + "Top 5 High Scores:")
    for i, score in enumerate(sorted_scores[:5], start=1):
        username, score_value, date = score
        print(f"{i}. {username}: {score_value} on {date}")


welcome_message()