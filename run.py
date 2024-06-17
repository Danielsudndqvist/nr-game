import random
def number_guessing_game():
    num = random.randint(1, 100)
    guesses = 0
    while guesses<5:
        answer = int(input("Guess a number between 1 and 100\n"))
        guesses += 1
        if answer == num:
            print("You won!!!")
            break
        elif answer < num:
            print("Try Higher\nYou have used",int(guesses),"out of 5 guesses.")
        elif answer > num:
            print("Try Lower\nYou have used",int(guesses),"out of 5 guesses.")
    else:
        print("You have no guesses left, the number was",num)

