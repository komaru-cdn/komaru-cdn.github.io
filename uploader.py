import os
import subprocess
import shutil

repo_path = "C:\\Users\\winbo\\winbo-cdn.github.io\\" # put the path to your local repo here, note that you need to use 2 backslashes instead of 1. if youre on linux, normally use a slash

def upload_file_using_git(repo_path, file_path, commit_message="cdn: Add file via uploader"):
    if not os.path.exists(file_path):
        print(f"The file '{file_path}' you tried to upload doesn't exist.")
        return

    if not os.path.isdir(os.path.join(repo_path, ".git")):
        print(f"The repo directory '{repo_path}' you specified is not a valid Git repository.")
        return

    file_name = os.path.basename(file_path)
    
    destination_path = os.path.join(repo_path, "public", file_name)
    
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    shutil.copy(file_path, destination_path)

    subprocess.run(["git", "add", destination_path], cwd=repo_path)

    subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path)

    subprocess.run(["git", "push"], cwd=repo_path)

    print(f"File '{file_name}' uploaded successfully to the 'public' folder in the repository.")

file_path = input("Enter the path to the file to upload: ")

upload_file_using_git(repo_path, file_path)
