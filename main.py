import os
import sys
from github import Github
from dotenv import load_dotenv

load_dotenv()

path = os.getenv("FILEPATH")
username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

def main():
    folderName = str(sys.argv[1])
    if not os.path.exists(folderName): #Checks if folder already exists
        os.makedirs(path + str(folderName)) 
        user = Github(username, password).get_user()
        repo = user.create_repo(folderName)
        print("Succesfully created repository {}".format(folderName))
    else:
        print("Project/Repo already exist")
    
    
main()
