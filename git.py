import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint

repo_path = "/home/svds90/Docs"


def get_repo_list(repo_path: str) -> list:

    command = f'find {repo_path} -type d -name ".git" 2>/dev/null'
    result = subprocess.run(command, capture_output=True, shell=True, text=True)

    if result.returncode != 0 or not result.stdout.strip():
        print("Repos not found")
        return []

    repo_dirs = [repo.removesuffix('/.git') for repo in result.stdout.splitlines()]

    return repo_dirs


def get_git_status(repo_path: str):
    command = 'git status'
    result = subprocess.run(command, capture_output=True, shell=True, text=True, cwd=repo_path)

    return result.stdout


pprint(get_repo_list(repo_path))

pprint(get_git_status("/home/svds90/Docs/repo/waybar-git"))
