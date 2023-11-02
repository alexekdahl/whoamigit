#!/usr/bin/env python3

import os
import inquirer


def get_git_user():
    name = os.popen("git config user.name").read().strip()
    email = os.popen("git config user.email").read().strip()
    return name, email


def set_git_user(name, email):
    os.system(f'git config user.name "{name}"')
    os.system(f'git config user.email "{email}"')


def main():
    current_name, current_email = get_git_user()

    if current_name and current_email:
        print(f"Current git user for this project:\nName: {current_name}\nEmail: {current_email}\n")
    else:
        print("No local git user set for this project.\n")

    questions = [
        inquirer.List(
            "user",
            message="Which git user do you want to use for this project?",
            choices=["Personal", "Work"],
        ),
    ]

    answers = inquirer.prompt(questions)

    # Check if answers is None (user canceled the prompt)
    if answers is None:
        return

    if answers["user"] == "Personal":
        set_git_user("alexekdahl", "77007088+alexekdahl@users.noreply.github.com")
        print("Set to Personal git user for this project.")
    elif answers["user"] == "Work":
        set_git_user("Work Name", "work@email.com")
        print("Set to Work git user for this project.")


if __name__ == "__main__":
    main()
