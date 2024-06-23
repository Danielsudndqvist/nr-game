# Nr-game


## Features
- Interactive number guessing game.
- Score tracking and saving to Google Sheets.
- Display of top scores from the Google Sheet.
- User-friendly interface with colored console output for better readability.

## Installation
1. Clone the repository or download the project files.
2. Ensure you have Python installed on your system.
3. Install the required libraries by running: pip install gspread openpyxl colorama
4. 4. Set up a Google Cloud Project and enable the Google Sheets API.
5. Create a `creds.json` file with your Google Service Account credentials and ensure it's placed in the project directory.

## Usage
1. Run the script.
2. Follow the on-screen instructions to play the game, view high scores, or exit the game.

### Prerequisites
- Python >= 3.8
- Google Cloud Platform account
- A Google Sheet for storing scores (`creds.json` should contain the path to this sheet).

## Bugs
# Solved bugs
A large number of bugs was accidentally created during development and had to be fixed. Fixes included:

looking through code line by line
using print() statements to see what was acctually going on
review commit history
search google for possible solutions
a lot of trial and error
# Unfixed bugs
None


## Testing
### Code validator 
![image](https://github.com/Danielsudndqvist/nr-game/assets/163173315/3e31b3c7-c5d3-476b-bfcb-ad57cb6ddf87)




## Depoyment

Deployment to Heroku
Log in (or sign up) to Heroku. ( https://www.heroku.com/ )
From the dashboard, create a "new app" and follow the instructions.
When created go to the settings tab.
Add a Config Var with PORT as the key and 8000 as value.
Add 2 buildpacks, python and nodejs (in that order).
Go to the deployment tab.
Select GitHub as deployment method.
Connect app to the correct repository.
Choose to deploy either manully or enable automatic deploys.
Changes to the code
If changes has been made in local development, the requirements.txt might need to be updated.

It is done by entering the following command in the terminal: 'pip3 freeze > requirements.txt'
Updated file must then be commited and pushed to GitHub.
Local development
Forking the project
Log in (or sign up) to Github.
Go to the repository for this project, Dream Achiever.
Click the Fork button in the top right corner.
Cloning the project
Log in (or sign up) to Github.
Go to the repository for this project, Dream Achiever.
Click on the code button, select whether you would like to clone with HTTPS, SSH, or GitHub CLI, and copy the link shown.
Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory. Type 'git clone' into the terminal and then paste the link you copied in step 3.
Press enter.


## Credits

### Websites & Programs
Chatgpt - Used to help identify problems in code and possible way to solve them.
Github - Created repository and stored files here after commits.
Heroku - For deploying.
Gitpod - Wrote code and did commits to Github from here.
W3 School Read and used as a guide for some code.


