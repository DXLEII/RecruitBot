import requests 
import time 
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')

# Constant from dotenv

GITHUB_API_URL_COMMITS = "https://api.github.com/repos/{owner}/{repo}/commits"
GITHUB_API_URL_REPO = "https://api.github.com/repos/{owner}/{repo}"
OWNER = os.getenv("OWNER")
REPO = os.getenv("REPO")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))  # Default to 60 seconds if not set in .env
STAR_INCREMENT = int(os.getenv("STAR_INCREMENT", 10))  # Default to 10 stars if not set in .env

#github personal access token for secure auth
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


# functions to pull the data for number of stars and commit history. 
def get_latest_commit_sha():
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    response = requests.get(GITHUB_API_URL_COMMITS.format(owner=OWNER, repo=REPO), headers=headers)
    response.raise_for_status()
    commits = response.json()
    return commits[0]['sha']

def get_stars_count():
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    response = requests.get(GITHUB_API_URL_REPO.format(owner=OWNER, repo=REPO), headers=headers)
    response.raise_for_status()
    repo_info = response.json()
    return repo_info['stargazers_count']

def main():
    last_commit_sha = None
    last_star_count = get_stars_count()
    next_star_milestone = last_star_count + STAR_INCREMENT

    while True:
        try:
            # Check for new commits
            latest_commit_sha = get_latest_commit_sha()
            if last_commit_sha is not None and latest_commit_sha != last_commit_sha:
                print(f"New commit detected: {latest_commit_sha}")
                last_commit_sha = latest_commit_sha
            else:
                print("No new commit.")
                last_commit_sha = latest_commit_sha

            # Check for new stars and celebrate every X stars!
            current_star_count = get_stars_count()
            if current_star_count >= next_star_milestone:
                print(f"Milestone reached: {current_star_count} stars")
                next_star_milestone = current_star_count + STAR_INCREMENT
            else:
                print(f"Current star count: {current_star_count}")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()