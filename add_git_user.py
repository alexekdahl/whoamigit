#!/usr/bin/env python3

import os
import re

class GitConfigHandler:

    def __init__(self, config_path=".git/config"):
        self.config_path = config_path

    def _get_content(self):
        try:
            with open(self.config_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"'{self.config_path}' not found.")
        except Exception as e:
            raise Exception(f"An error occurred while reading '{self.config_path}': {str(e)}")

    def find_git_config(self):
        """Return the path to the .git/config file if it exists, None otherwise."""
        return self.config_path if os.path.exists(self.config_path) else None

    def extract_user_details(self):
        """Extract user name and email from .git/config content if exists."""
        content = self._get_content()
        user_name_match = re.search(r'name\s*=\s*(.+)', content)
        user_email_match = re.search(r'email\s*=\s*([\S@.]+)', content)

        user_name = user_name_match.group(1).strip() if user_name_match else None
        user_email = user_email_match.group(1).strip() if user_email_match else None

        return user_name, user_email

    def override_user_info_in_config(self, new_name, new_email):
        """Override the existing user info in the .git/config file."""
        content = self._get_content()

        # Replace the existing user details
        content = re.sub(r'name\s*=\s*.+', f'name = {new_name}', content)
        content = re.sub(r'email\s*=\s*[\S@.]+', f'email = {new_email}', content)

        try:
            with open(self.config_path, 'w') as file:
                file.write(content)
        except Exception as e:
            raise Exception(f"An error occurred while writing to '{self.config_path}': {str(e)}")


def main():
    handler = GitConfigHandler()

    try:
        git_config_path = handler.find_git_config()
        if not git_config_path:
            print("Not a git repository or you're not in the root directory of the repo.")
            return

        user_name, user_email = handler.extract_user_details()
        if user_name and user_email:
            print(f"Existing user name: {user_name}")
            print(f"Existing user email: {user_email}")
            answer = input("Do you want to override the existing user details? (yes/no): ")
            if answer.lower() not in ["yes", "y"]:
                return

        new_name = "AlexEkdahl"
        new_email = "77007088+AlexEkdahl@users.noreply.github.com"

        handler.override_user_info_in_config(new_name, new_email)
        print("User details overridden successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
