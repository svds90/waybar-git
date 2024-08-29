import git
import json
import subprocess
from pprint import pprint

dirs = ""

dirs_list = [path.strip() for path in dirs.split(',')]

data = {}


def get_repo_list(dirs_list: list) -> list:

    all_finded_repos = []

    for dir in dirs_list:

        command = f'find {dir} -type d -name ".git" 2>/dev/null'
        result = subprocess.run(command, capture_output=True, shell=True, text=True)

        if result.returncode != 0 or not result.stdout.strip():
            print("Repos not found")
            return []

        finded_repos = [repo.removesuffix('/.git') for repo in result.stdout.splitlines()]
        all_finded_repos.extend(finded_repos)

    return all_finded_repos


def get_git_status(finded_repos: list):

    for repo_dir in finded_repos:
        repo = git.Repo(repo_dir)
        status = repo.git.status(porcelain=True)

        if status:
            print('*' * 15)
            print(repo_dir)
            print(status)


get_git_status(get_repo_list(dirs_list))
