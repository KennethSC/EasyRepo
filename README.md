## Description

This small python script uses the Github API to create a repository using an access token from your account. It then initializes the repository in a user specified directory, creates a README file, adds, commits, and then pushes the README to your newly created repo. The purpose of this script is to automate the process of creating and initializing a git repository so that now all you have to do is type one line in your terminal.

## Requirements

__Github API:__

To install the Github API (for Mac users) use this command in your Terminal: pip install PyGithub


You will also need an access token from your Github account to create your repo using the Github API.


## Usage

Put the python script .Create_Repo.py in your home directory, it won't show up if use the 'ls' command due to the '.' in front of the file name, and type the command: python3 .Create_Repo.py NAME_OF_YOUR_REPO

To modify this file from the terminal go to the directory you placed it in and type 'vi .Create_Repo.py' or 'nano .Create_Repo.py'.
