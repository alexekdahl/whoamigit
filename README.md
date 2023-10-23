# Git User Switcher Script

## Description
This Python script allows you to switch between different git users for a specific git project. It's useful for managing contributions from multiple accounts (e.g., personal and work).

## Features
- Fetches the current git user for the active project.
- Allows switching between predefined git users.
- Updates the local git configuration for the active project.
- User-friendly prompt for git user selection.

## Dependencies
- Python 3.x
- os
- inquirer

## How to Use
1. Ensure git is installed and you are inside a git project directory.
2. Open a terminal window and navigate to the folder containing the script.
3. Run `python <script_name>.py`.
4. Follow the on-screen prompt to select the git user for this project.

## Code Explanation
- get_git_user(): Fetches the current git user's name and email from the local git configuration.
- set_git_user(name, email): Sets the git user's name and email in the local git configuration.
- main(): Displays the current git user, presents a prompt to switch users, and updates the git configuration accordingly.

## License
MIT License

## See also:
- Git Configuration: https://www.google.com/search?q=Git+Configuration
- Python inquirer: https://www.google.com/search?q=Python+inquirer
