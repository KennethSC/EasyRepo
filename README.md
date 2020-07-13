## Description

This small python script takes in one argument (your desired Repo name) and uses the Github API to create a repository with that name using an access token from your account. It then initializes the repository in a user specified directory, creates a README file, adds, commits, and then pushes the README to your newly created repo. The purpose of this script is to automate the process of creating and initializing a git repository so that now all you have to do is type one line in your terminal.

## Requirements

__Github API:__

To install the Github API (for Mac users) use this command in your Terminal: **pip install PyGithub**


You will also need an access token from your Github account to create your repo using the Github API.


## Usage

Run the script Create_Repo.py giving it one argument which would be what you want your new Repo to be called. You could also put this script in your home directory and even add a "." to the beginning of the file name to make it a hidden file if you'd like. This way you could just open your terminal and run the script from your home directory.
