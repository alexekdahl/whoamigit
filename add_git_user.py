#!/usr/bin/env python3
import os
import re

def find_git_config():
    """Return the path to the .git/config file if it exists, None otherwise."""
    git_config_path = os.path.join(".git", "config")
    if os.path.exists(git_config_path):
        return git_config_path
    return None

def extract_user_name(content):
    """Extract user name from .git/config content if exists."""
    user_match = re.search(r'\[user\].*?name\s*=\s*(\S+)', content, re.DOTALL)
    return user_match.group(1) if user_match else None

def add_user_info_to_config(git_config_path, user_info):
    """Prepend the given user info to the .git/config file."""
    with open(git_config_path, 'r+') as file:
        content = file.read()
        file.seek(0)
        file.write(user_info + content)

def main():
    git_config_path = find_git_config()

    if not git_config_path:
        print("Not a git repository or you're not in the root directory of the repo.")
        return

    with open(git_config_path, 'r') as file:
        content = file.read()

    user_name = extract_user_name(content)

    if user_name:
        print(f"Existing user name: {user_name}")
        return

    user_info = """[user]
name = AlexEkdahl
email = 77007088+AlexEkdahl@users.noreply.github.com
"""
    add_user_info_to_config(git_config_path, user_info)

if __name__ == "__main__":
    main()
