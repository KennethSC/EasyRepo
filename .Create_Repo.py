from github import Github
import time
import sys
import os

Github_username = "YOUR GITHUB USERNAME HERE"
access_token = "YOUR ACCESS TOKEN HERE"
Repo_name = str(sys.argv[1])

# Make sure to enter the full path of the directory in which 
# you want to creat the repository in correctly
# EX: "/Users/your_name/Desktop/Projects/"
path_to_Projects = "FULL PATH THAT YOUR REPO WILL BE MADE IN"


def create():

    # Creates Repo with specified name
    account = Github(access_token)
    user = account.get_user()
    repo = user.create_repo(Repo_name)

    print("Creating Repo....\n")
    time.sleep(2)

    # Navigates to designated path
    os.makedirs(path_to_Projects + str(Repo_name))
    os.chdir(path_to_Projects + str(Repo_name))

    # Creates a README.md file to push
    with open("README.md", "w") as text_file:
        print("Pass")
    
    # Initialize Repo, adds, commits, and pushes README.md
    os.system("git init")
    os.system("git remote add origin https://github.com/{}/{}.git".format(Github_username, Repo_name))
    os.system("git add .")
    os.system("git commit -m \"Initial Commit\"")
    os.system("git push -u origin master")

    # Print success message
    print(f"Successfully created {Repo_name} repository.")


if __name__ == '__main__':
    create()
