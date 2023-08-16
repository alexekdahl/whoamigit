#!/usr/bin/env python3
import os
import re

def find_git_config():
    """Return the path to the .git/config file if it exists, None otherwise."""
    git_config_path = os.path.join(".git", "config")
    if os.path.exists(git_config_path):
        return git_config_path
    return None

def extract_user_details(content):
    """Extract user name and email from .git/config content if exists."""
    user_name_match = re.search(r'name\s*=\s*(.+)', content)
    user_email_match = re.search(r'email\s*=\s*([\S@.]+)', content)

    user_name = user_name_match.group(1).strip() if user_name_match else None
    user_email = user_email_match.group(1).strip() if user_email_match else None

    return user_name, user_email

def override_user_info_in_config(git_config_path, new_name, new_email):
    """Override the existing user info in the .git/config file."""
    with open(git_config_path, 'r') as file:
        content = file.read()

    # Replace the existing user details
    content = re.sub(r'name\s*=\s*.+', f'name = {new_name}', content)
    content = re.sub(r'email\s*=\s*[\S@.]+', f'email = {new_email}', content)

    with open(git_config_path, 'w') as file:
        file.write(content)

def main():
    git_config_path = find_git_config()

    if not git_config_path:
        print("Not a git repository or you're not in the root directory of the repo.")
        return

    with open(git_config_path, 'r') as file:
        content = file.read()

    user_name, user_email = extract_user_details(content)

    if user_name and user_email:
        print(f"Existing user name: {user_name}")
        print(f"Existing user email: {user_email}")
        answer = input("Do you want to override the existing user details? (yes/no): ")
        if answer.lower() not in ["yes", "y"]:
            return

    new_name = "AlexEkdahl"
    new_email = "77007088+AlexEkdahl@users.noreply.github.com"

    override_user_info_in_config(git_config_path, new_name, new_email)
    print("User details overridden successfully!")

if __name__ == "__main__":
    main()
